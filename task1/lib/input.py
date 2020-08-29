import sys
sys.path.insert(0, '/task1/lib/')
from task1.lib import logging as log

def inputData():
    try:
        file_location = input("Введите путь к файлу: ")

        try:
            phone_number = int(input("Введите номер телефона: "))
        except (TypeError, ValueError):
            return

        try:
            database_flag = int(input("Нужно ли добавлять в базу?(1|0):"))
        except (TypeError, ValueError):
            return

        try:
            recognition_stage = int(input("Этап рапознавания(1|2):"))
        except (TypeError, ValueError):
            return
        return [file_location, phone_number, database_flag, recognition_stage]
    except:
        log.logging('error at the input stage')