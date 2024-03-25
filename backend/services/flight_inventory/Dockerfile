FROM python:3.8-slim
WORKDIR /app 

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y iputils-ping 

COPY . . 

EXPOSE 5000 

CMD ["python", "run.py"] 