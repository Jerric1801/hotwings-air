FROM mongo

COPY flight_inventory.json /flight_inventory.json
CMD mongoimport --uri mongodb://root:example@host.docker.internal:27017/flight -db reach-engine --collection flight_inventory --type json --file /flight_inventory.json --jsonArray