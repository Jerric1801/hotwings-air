# FROM mongo

# COPY flight_inventory.json /flight_inventory.json
# CMD mongoimport --uri mongodb://root:example@host.docker.internal:27017/reach-engine -c flight_inventory --type json --file /flight_inventory.json --jsonArray


FROM python:3.8-slim 
WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt   
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"] 

