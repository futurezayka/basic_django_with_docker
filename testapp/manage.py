import os
import sys
from django.db import connection


def load_test_data():
    sql_file = 'testdata.sql'
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), sql_file)

    with open(file_path, 'r') as f:
        sql_statements = f.read()

    with connection.cursor() as cursor:
        cursor.execute("SELECT to_regclass('public.testdata')")
        table_exists = cursor.fetchone()[0]

        if not table_exists:
            cursor.execute(sql_statements)


if __name__ == "__main__":

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testapp.settings')
    try:
        load_test_data()

        from django.core.management import execute_from_command_line

        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
