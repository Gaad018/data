import re

def recognition(text, stage, config):
    """
    recognition(text, stage)
    Функция распознавания текста в зависимости от выбранного этапа

    :param text: string
    :param stage: int
    :return: string
    """

    print(config)

    if stage == 1:
        if re.findall(r'(автоответчик)', text) != []:
            response = config['stage1']['ao']
        else:
            response =  config['stage1']['man']
    elif stage == 2:
        if re.findall(r'(неудобно|нет)', text) != []:
            response = config['stage2']['negative']
        else:
            response = config['stage2']['positive']
    return response