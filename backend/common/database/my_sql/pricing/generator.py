import json
import random

regions = {
    "Southeast Asia": ["Singapore", "Bangkok", "Kuala Lumpur", "Jakarta", "Manila"],
    "East Asia": ["Tokyo", "Hong Kong"],
    "Oceania": ["Sydney"],
    "Middle East": ["Dubai"],
    "Europe": ["London", "Paris"],
    "North America": ["New York", "Los Angeles"]
}
adjacent_regions = {
    "Southeast Asia": ["East Asia", "Oceania", "Middle East"],
    "East Asia": ["Southeast Asia", "Oceania"],
    "Oceania": ["Southeast Asia", "East Asia", "North America"],
    "Middle East": ["Southeast Asia", "Europe"],
    "Europe": ["Middle East", "North America"],
    "North America": ["Oceania", "Europe"] 
}
distance_tiers = {
    "intraregional": (500,  2000),  # Within the same region
    "interregional_close": (2000, 5000),  # Between neighboring regions
    "interregional_far":  (5000, 9000),  # Between distant regions 
}
seat_classes = {"First":2.5, "Business":1.75, "Premium Economy":1.23, "Economy": 1}
locations = ["Singapore", "Tokyo", "Bangkok", "Sydney", "Hong Kong", "London", "New York", "Kuala Lumpur", "Jakarta", "Manila", "Dubai", "Paris", "Los Angeles"]
tiers = {
    "short": (500, 2000), 
    "medium": (2000, 5000),
    "long": (5000, 10000)
}


def are_regions_adjacent(region1, region2):
    return region2 in adjacent_regions[region1] 

def estimate_distance(origin, destination):
    origin_region = None
    destination_region = None

    # Find the regions of the origin and destination
    for region_name, cities in regions.items():
        if origin in cities:
            origin_region = region_name
        if destination in cities:
            destination_region = region_name

    # Distance estimation
    if origin_region == destination_region:
        distance_tier = "intraregional"
    elif are_regions_adjacent(origin_region, destination_region):  # You'll need to define this
        distance_tier = "interregional_close"
    else:
        distance_tier = "interregional_far"

    # Pick a random distance within the chosen tier (adjust ranges as needed)
    distance = random.randint(*distance_tiers[distance_tier])
    return distance

def generate_sql(flight_code, seat_class, price):
    return f"""
INSERT INTO `flight_pricing` (`flight_number`, `seat_class`, `price`) 
VALUES ('{flight_code}', '{seat_class}', {float(round(price,2))}); 
    """

def generate_prices():
    sql_string = ""
    with open('flights.json', 'r') as infile:
        flight_list = json.load(infile)

    for flight in flight_list["flights"]:
        origin = flight["origin"]
        destination = flight["destination"]
        distance = estimate_distance(origin, destination)
        if tiers["short"][0] <= distance <= tiers["short"][1]:
            base_price = random.randint(100, 300)  # Adjust ranges as needed
        elif tiers["medium"][0] <= distance <= tiers["medium"][1]:
            base_price = random.randint(300, 600)
        else:  # long
            base_price = random.randint(600, 1000) 
        for classes, multiple in seat_classes.items():
            price = base_price * multiple
            sql = generate_sql(flight["flight_number"], classes, price)
            sql_string += sql 
            sql_string += "\n"

    return sql_string

if __name__ == "__main__":
    sql = """
CREATE DATABASE IF NOT EXISTS `prices`;
\n
GRANT ALL PRIVILEGES ON prices.* TO 'root'@'%' IDENTIFIED BY 'strong_password'; 
FLUSH PRIVILEGES;
\n
USE `prices`;
\n
DROP TABLE IF EXISTS `flight_pricing`; 
\n
CREATE TABLE IF NOT EXISTS `flight_pricing` (
`pricing_id` int(11) NOT NULL AUTO_INCREMENT,
`flight_number` varchar(15) NOT NULL, 
`seat_class` varchar(15) NOT NULL,
`price` float(10) NOT NULL,
`created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
`modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (`pricing_id`),
INDEX (`flight_number`) -- Add an index on flight_id
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
\n
"""

    sql += generate_prices()

    with open('../init_db.sql', 'w') as outfile:  # 'w' for write mode..
        outfile.write(sql)
