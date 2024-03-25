CREATE DATABASE IF NOT EXISTS `prices`;

-- Create the database only if it doesn't already exist
GRANT ALL PRIVILEGES ON prices.* TO 'root'@'%' IDENTIFIED BY 'strong_password'; 
FLUSH PRIVILEGES;

USE `prices`;
-- Drop the table if you want a fresh start each time
DROP TABLE IF EXISTS `flight_pricing`; 

CREATE TABLE IF NOT EXISTS `flight_pricing` (
  `pricing_id` int(11) NOT NULL AUTO_INCREMENT,
  `flight_id` varchar(15) NOT NULL, 
  `seat_class` varchar(15) NOT NULL,
  `price` float(10) NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`pricing_id`),
  INDEX (`flight_id`) -- Add an index on flight_id
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Insert a row, letting the database generate the flight_id
INSERT INTO `flight_pricing` (`flight_id`, `seat_class`, `price`) 
VALUES ('HWA550', 'economy', 300.00); 

-- Insert a row, letting the database generate the flight_id
INSERT INTO `flight_pricing` (`flight_id`, `seat_class`, `price`) 
VALUES ('HWA551', 'first', 450.00); 