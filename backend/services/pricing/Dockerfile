FROM python:3.8-slim 
WORKDIR /app 

COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5002

CMD ["python", "run.py"] 