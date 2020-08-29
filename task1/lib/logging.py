import datetime

def logging(text = '', type = 'error', additionally = []):
    """
    logging(text = '', type = 'error', additionally = [])
    Функция для ведения логов скрипта

    :param text: string
    :param type: string
    :param additionally: list
    """
    # Строка в формате [%d/%m/%Y:%H:%M:%S]
    dateEndTime = f'[{datetime.datetime.today().strftime("%d/%m/%Y:%H:%M:%S")}] '

    if type == 'error' or type == 'info':
        with open('scriptLog.log', 'a', encoding="utf-8") as file:
            file.write(f"{dateEndTime}{type} - {text}\n")

    if type == 'result':
        print(additionally)
        with open('resultLog.log', 'a', encoding="utf-8") as file:
            file.write(f"{dateEndTime}{additionally[0]} -{additionally[1]}-{additionally[2]}-{additionally[3]}-\"{additionally[4]}\"\n")
