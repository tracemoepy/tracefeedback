FROM python:3.9-slim-bullseye

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir \
    -U -r requirements.txt
    
CMD ["python3", "main.py"]