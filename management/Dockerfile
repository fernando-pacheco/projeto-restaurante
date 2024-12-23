FROM python:3.12-slim

WORKDIR /management

RUN apt update && apt install -y libpq-dev gcc python3-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY . .

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8000"]