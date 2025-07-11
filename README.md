# DWHomework-2



ขั้นตอนที่ 1: โคลนโปรเจกต์จาก GitHub
git clone https://github.com/narinthakan/DWHomework-2.git

cd DWHomework-2

ขั้นตอนที่ 2: สร้าง Virtual Environment
python3 -m venv venv

ขั้นตอนที่ 3: ติดตั้ง Dependencies
pip install -r requirements.txt

ขั้นตอนที่ 4: ตั้งค่าและตรวจสอบการเชื่อมต่อกับฐานข้อมูล
python manage.py migrate

รันเซิร์ฟเวอร์ Django
python manage.py runserver


ข้อมูลที่ใช้ Geo Data using the Cell Tower Dataset

สร้างฐานข้อมูลเพื่อทำการรองรับข้อมูลใน Clickhouse

ทำการ insert ข้อมูลผ่านคำสั่ง https://clickhouse.com/docs/getting-started/example-datasets/cell-towers

เมื่อทำการเพิ่มข้อมูลเสร็จสิ้น ให้ทำการเปิด server clickhouse ด้วยคำสั่ง clickhouse server 

สร้างไฟล์ views.py เพื่อทำการเชื่อมต่อและดึงข้อมูลมาแสดงผล ด้วย html hw04.html

จากนั้น รันคำสั่ง python manage.py runserver
