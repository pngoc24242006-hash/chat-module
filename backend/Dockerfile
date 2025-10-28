# Base image Python
FROM python:3.13-slim

WORKDIR /app

# Cài đặt dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code
COPY ./app /app

# Expose cổng
EXPOSE 8000

# Run FastAPI bằng uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
