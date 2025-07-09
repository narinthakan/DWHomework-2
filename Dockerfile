# ใช้ Python 3.12 image เป็น base
FROM python:3.12-slim

# ตั้ง working directory
WORKDIR /app

# ติดตั้ง dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกไฟล์โปรเจกต์ทั้งหมด
COPY . .

# สั่ง Django ทำการ migrate แล้วรัน server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
