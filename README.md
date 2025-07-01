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


