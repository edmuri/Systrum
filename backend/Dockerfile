FROM python:3.11-slim

WORKDIR /app

# copy requirements first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy backend code
COPY app ./app

WORKDIR /app/app

# environment variables
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV PYTHONUNBUFFERED=1

# initialize db then run flask
CMD python init_db.py && flask --app main.py --debug run --host=0.0.0.0