FROM python:3.13.1-alpine as base

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "-m", "fastapi", "run", "app/main.py"]
