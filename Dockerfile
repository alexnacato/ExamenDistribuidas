FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY servidor_chat.py .
EXPOSE 8765

CMD ["python", "servidor_chat.py"]
