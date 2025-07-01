# realtime/utils/clickhouse_client.py

from clickhouse_connect import get_client

# กำหนดค่าการเชื่อมต่อกับ ClickHouse
client = get_client(host='localhost', username='default', password='', database='default')

def query_clickhouse(sql):
    """
    ฟังก์ชันนี้ทำหน้าที่ส่งคำสั่ง SQL ไปยัง ClickHouse
    :param sql: คำสั่ง SQL ที่จะ query
    :return: ผลลัพธ์จาก query ในรูปแบบของ result_rows
    """
    result = client.query(sql)  # ส่งคำสั่ง SQL ไปยัง ClickHouse
    return result.result_rows  # คืนค่าผลลัพธ์จาก query
