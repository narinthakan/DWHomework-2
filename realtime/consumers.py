from channels.generic.websocket import AsyncWebsocketConsumer
import json
from clickhouse_connect import get_client

class RealtimeConsumer(AsyncWebsocketConsumer):  
    async def connect(self):
        # Accept WebSocket connection
        await self.accept()

    async def receive(self, text_data):
        # เชื่อมต่อกับ ClickHouse และรันคำสั่ง SQL
        client = get_client(host='localhost')
        result = client.query('SELECT count() FROM events')

        # ส่งผลลัพธ์กลับไปยัง WebSocket client
        await self.send(text_data=json.dumps({
            'count': result.result_rows[0][0]  # ส่งค่า count จากผลลัพธ์
        }))
