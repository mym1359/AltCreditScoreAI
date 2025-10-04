FROM python:3.10-slim

WORKDIR /app

# نصب libgomp برای LightGBM
RUN apt-get update && apt-get install -y libgomp1

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN pytest tests/

CMD ["python"]