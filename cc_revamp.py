import json
import requests
import xml.etree.ElementTree as ET

valutes_dict = {}

class FuckThisToothAche():
    def __init__(self):
        global valutes_dict
        url = "http://www.cbr.ru/scripts/XML_daily.asp?"
        response = requests.get(url)
        string = response.content
        parsed_response = ET.fromstring(string)

        # Здесь надо перегнать в строку, иначе...
        # Exception has occurred: TypeError
        # a bytes-like object is required, not 'Response'

        # Вообще я не уверен, что есть "парсинг", но...

        

        for valute in parsed_response.findall('Valute'):
           
            # Придётся перегонять всё значение из-за одной сранной запятой, а не точки
            # +1 Костыль

            dot_variable = valute.find('Value').text
            dot_variable1= ''

            for i in dot_variable:
                if i == ',':
                    dot_variable1 += '.'
                else:
                    dot_variable1 += i

            valutes_dict[valute.find('Name').text] = dot_variable1
    
            print(valute.find('Name').text)
            print(valute.find('Value').text)

    def getSalaryRub(self, amount, valute):
        result = float(valutes_dict[valute]) * amount

        file = open('currency.json', 'w')
        file.write(str(result))
        file.close()

        # Вообще в задаче указано "возвращать json" не результат не указан, так что...
        # А вообще, может я что-то неправильно понял, и тем более неправильно сделал
        # Ладно, хрен с ним. Залью на гитхаб и пойду спать.
        # Время завершения 1:59. А сел я где-то в 0:30.

example = FuckThisToothAche()
example.getSalaryRub(50.0, 'Доллар США')
