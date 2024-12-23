# -*- coding: utf-8 -*-

text = """
3 {
<question>История возникновения ОС с 1940-х до 1980-х. Классификация ПО. 1</question>


<answer>40 - 50 годы - ОС отсутствует

Полный доступ к ресурсам ЭВМ на машинном языке, все программы разрабатываются в двоичном коде. Этот период характеризуется высокой стоимостью приобретения и эксплуатации компьютеров и низкой стоимостью труда программистов. Компьютеры использовались в монопольном интерактивном режиме. Основная цель – максимизировать использование аппаратного обеспечения. Основной режим работы компьютера – простой и ожидание каких-либо действий программиста. При этом наблюдается недостаточное использование дорогостоящего вычислительного оборудования.

60-е годы – развитие первых операционных систем 

Важной тенденцией этого периода является создание семейств программно – совместимых машин и операционных систем для них. Примерами семейств программно – совместимых машин, построенных на интегральных микросхемах, являются серии машин IBM/360, IBM/370 и  PDP-11.
Программная совместимость требовала и совместимости операционных систем. Однако такая совместимость подразумевает возможность работы на больших и малых вычислительных системах, с большим и малым количеством разнообразной периферии, в коммерческой области и в области научных исследований. Операционные системы, построенные с намерением удовлетворить всем этим противоречивым требованиям, оказались чрезвычайно сложными. Они состояли из многих миллионов ассемблерных строк, написанных тысячами программистов, и содержали тысячи ошибок, вызывающих нескончаемый поток исправлений. Операционные системы этого поколения были очень дорогими. 

1970-годы – развитие ОС 

важной вехой в истории операционных систем явилось создание ОС UNIX. Особенностью этой системы  являлось то, что она была первой системной программой, которая была написана с использованием языка, отличного от машинного языка. С середины 70-х годов началось массовое использование ОС UNIX. К этому времени программный код для UNIX был на 90% написан на языке высокого уровня С. Широкое распространение эффективных С-компиляторов сделало UNIX уникальной для того времени ОС, обладающей возможностью сравнительно лёгкого переноса на различные типы компьютеров. Поскольку эта ОС поставлялась вместе с исходными кодами, то она стала первой открытой ОС, которую могли совершенствовать простые пользователи.

1980-годы – развитие ОС MS DOS

История DOSа   (Disk Operation System) началась в 1980 году в фирме Seattle Computer Products. Сетевые функции появились у операционных систем персональных компьютеров не сразу. Первая версия наиболее популярной операционной системы раннего этапа развития персональных компьютеров- MS-DOS компании Microsoft – была лишена этих возможностей. Это была однопрограммная однопользовательская ОС с интерфейсом командной строки, способная стартовать с дискеты. 
Недостающие функции для MS-DOS и подобных ей ОС компенсировались внешними программами, предоставлявшими пользователю удобный графический интерфейс(например, Norton Commander) или средства тонкого управления дисками (например,  PC Tools).  </answer>

Три группы :

1.     Системное программное обеспечение (системные программы);  

2.     Прикладное программное обеспечение (прикладные программы);

3.    Инструментальное программное обеспечение (инструментальные системы).</answer>

}
"""

import json
import re

def parse_data(text_content):
    """Парсит текст с HTML-подобными тегами и возвращает JSON."""
    items = {}
    # Разделяем текст на отдельные объекты
    objects = re.findall(r'\d+\s*\{[\s\S]*?\}', text_content)
    for obj in objects:
        # Извлекаем ключ (цифру)
        key = int(re.search(r'\d+', obj).group())
        # Извлекаем вопрос
        question_match = re.search(r'<question>(.*?)</question>', obj, re.DOTALL)
        question = question_match.group(1).strip() if question_match else None
        # Извлекаем ответ
        answer_match = re.search(r'<answer>(.*?)</answer>', obj, re.DOTALL)
        answer = answer_match.group(1).strip() if answer_match else None

        items[key] = {"question": question, "answer": answer}
    return json.dumps(items, indent=2, ensure_ascii=False)

# Получаем текст из файла text.py

# Парсим текст и получаем JSON
json_output = parse_data(text)

# Записываем JSON в файл parsedText.json
with open('parsedText.json', 'w', encoding='utf-8') as outfile:
    outfile.write(json_output)

print("JSON данные записаны в файл parsedText.json")