
FROM python:3.8-slim 
WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt   
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"] 

