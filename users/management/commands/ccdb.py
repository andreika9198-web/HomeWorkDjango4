from django.core.management import BaseCommand
import pyodbc
from config.settings import USER, PASSWORD, HOST, DRIVER, DATABASE,PAD_DATABASE



class Command(BaseCommand):
    def handle(self, *args, **options):
        ConnectionString = f"""DRIVER={DRIVER};
                            SERVER={HOST};
                            DATABASE={PAD_DATABASE};
                            UID={USER};
                            PWD={PASSWORD}"""
        try:
            conn = pyodbc.connect(ConnectionString)
            conn.autocommit = True
            conn.execute(fr'CREATE DATABASE {DATABASE};')
        except pyodbc.Error as e:
            print(e)
        else:
            print(f'База данных {DATABASE} успешно создана!')
