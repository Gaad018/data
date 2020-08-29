#.env
from dotenv import load_dotenv
load_dotenv()
load_dotenv(verbose=True)

#modules
from tinkoff_voicekit_client import ClientSTT
import uuid, sys, os
sys.path.insert(0, '/task1/module/')
from task1.module import database, recognition as rec, logging as log, input


def main():
    #Грузим данные из конфига
    configData = {}
    exec(open('config/config.py').read(), configData)

    log.logging('Start programm', 'info')
    #Ввод данных из консоли
    data = input.inputData()
    fileLocation = data[0]
    phoneNumber = data[1]
    databaseFlag = data[2]
    recognitionStage = data[3]

    #Настройка параметров и отправка файла на распознавание
    try:
        client = ClientSTT(f'{os.getenv("API_KEY")}', f'{os.getenv("SECRET_KEY")}')
        # recognise method call
        response = client.recognize(fileLocation, configData['audio_config'])
        log.logging('Success recognition', 'info')
    except:
        log.logging('Error at the recognition stage')

    #Подготовка данных и логирование в файл resultLog
    try:
        textAudio = response[0]['alternatives'][0]['transcript']
        id = uuid.uuid1()
        durationCall = response[0]['end_time'][0:-1]
        responseRecognition = rec.recognition(textAudio, recognitionStage)


        log.logging('', 'result', [id, responseRecognition, phoneNumber, durationCall, textAudio])
    except:
        log.logging('Error on the recording result')

    # Работа с базой и удаление файла
    try:
        if databaseFlag == 1:
            database.bd(
                os.getenv("BDNAME"),
                os.getenv("USER"),
                os.getenv("PASSWORD"),
                os.getenv("HOST"),
                id,
                responseRecognition,
                phoneNumber,
                durationCall,
                textAudio
            )

            # Удаление файла
            os.remove(fileLocation)

    except:
        log.logging('Error per data base stage')


if __name__ == "__main__":
    main()