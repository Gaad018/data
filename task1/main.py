#.env
from dotenv import load_dotenv
load_dotenv()
load_dotenv(verbose=True)

#modules
from tinkoff_voicekit_client import ClientSTT
import uuid, sys, os
sys.path.insert(0, '/task1/lib/')
from task1.lib import database, recognition as rec, logging as log, input


def main():
    #Грузим данные из конфига
    config_data = {}
    exec(open('config/config.py').read(), config_data)

    log.logging('Start programm', 'info')
    #Ввод данных из консоли
    data = input.inputData()
    file_location = data[0]
    phone_number = data[1]
    database_flag = data[2]
    recognition_stage = data[3]

    #Настройка параметров и отправка файла на распознавание
    try:
        client = ClientSTT(f'{os.getenv("API_KEY")}', f'{os.getenv("SECRET_KEY")}')
        # recognise method call
        response = client.recognize(file_location, config_data['audio_config'])
        log.logging('Success recognition', 'info')
    except:
        log.logging('Error at the recognition stage')

    #Подготовка данных и логирование в файл resultLog
    try:
        textAudio = response[0]['alternatives'][0]['transcript']
        id = uuid.uuid1()
        duration_call = response[0]['end_time'][0:-1]
        responseRecognition = rec.recognition(textAudio, recognition_stage)


        log.logging('', 'result', [id, responseRecognition, phone_number, duration_call, textAudio])
    except:
        log.logging('Error on the recording result')

    # Работа с базой и удаление файла
    try:
        if database_flag == 1:
            database.bd(
                os.getenv("BDNAME"),
                os.getenv("USER"),
                os.getenv("PASSWORD"),
                os.getenv("HOST"),
                id,
                responseRecognition,
                phone_number,
                duration_call,
                textAudio
            )

            # Удаление файла
            os.remove(file_location)

    except:
        log.logging('Error per data base stage')


if __name__ == "__main__":
    main()