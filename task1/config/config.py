audioConfig = {
    "encoding": "LINEAR16",
    "sample_rate_hertz": 8000,
    "num_channels": 1
}
'''
Настройка возвращаемых значений в зависимости от этапа и результата распознавания
stage1 - 1 этап 
ao - если в аудио записи распознан автоответчик
man - если человек

stage2 - 2 этап 
negative - если в ответе есть отрицательные слова (“нет”, “неудобно” и т.п.)
positive - если положительные (“говорите”, “да конечно” и т.п.)
'''
returnValues ={
    'stage1': {
        'ao': 0,
        'man': 1
    },
    'stage2': {
        'positive': 1,
        'negative': 0
    }
}


