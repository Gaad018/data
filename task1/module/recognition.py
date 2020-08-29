import re

def recognition(text, stage):
    """
    recognition(text, stage)
    Функция распознавания текста в зависимости от выбранного этапа

    :param text: string
    :param stage: int
    :return: string
    """
    if stage == 1:
        if re.findall(r'(автоответчик)', text) != []:
            response =  0
        else:
            response =  1
    elif stage == 2:
        if re.findall(r'(неудобно|нет)', text) != []:
            response = 0
        else:
            response = 1
    return response