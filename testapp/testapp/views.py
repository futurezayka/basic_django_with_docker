from django.db import connection
from django.http import JsonResponse


def get_testdata_records():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM testdata')
        records = cursor.fetchall()

    return records


def testdata_view(request):
    records = get_testdata_records()
    context = {'records': records}
    return JsonResponse(context)
