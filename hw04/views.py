from django.http import JsonResponse
from clickhouse_driver import Client
from django.shortcuts import render
def hw04_view(request):
    try:
        client = Client(
            host='localhost',  # หรือ '127.0.0.1'
            port=9000,
            database='your_database_name',
            settings={'socket_timeout': 120}
        )
        

        # ทดสอบการเชื่อมต่อกับ ClickHouse
        client.execute("SELECT 1")
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

    # เขียน query
    query = "SELECT * FROM cell_towers LIMIT 5"
    result = client.execute(query)

    # สร้างข้อมูลที่จะส่งกลับ
    data = []
    for row in result:
        data.append({
            "radio": row[0],
            "mcc": row[1],
            "net": row[2],
            "area": row[3],
            "cell": row[4],
            "unit": row[5],
            "lon": row[6],
            "lat": row[7],
            "range": row[8],
            "samples": row[9],
            "changeable": row[10],
            "created": row[11],
            "updated": row[12],
            "averageSignal": row[13],
        })

    return render(request, 'hw04\hw04.html', {'data': data})
