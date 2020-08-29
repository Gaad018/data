import sys
sys.path.insert(0, '/task1/module/')
from task1.module import logging as log

def inputData():
    try:
        fileLocation = input("Введите путь к файлу: ")

        try:
            phoneNumber = int(input("Введите номер телефона: "))
        except (TypeError, ValueError):
            return

        try:
            databaseFlag = int(input("Нужно ли добавлять в базу?(1|0):"))
        except (TypeError, ValueError):
            return

        try:
            recognitionStage = int(input("Этап рапознавания(1|2):"))
        except (TypeError, ValueError):
            return
        return [fileLocation, phoneNumber, databaseFlag, recognitionStage]
    except:
        log.logging('error at the input stage')