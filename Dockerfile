FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/app"

RUN python scripts/populate.py

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]