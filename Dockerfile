FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN mkdir templates

RUN mkdir static

COPY templates/ templates/

COPY static/ static/

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]