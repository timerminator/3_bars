import json
import sys
import math


def load_data(filepath='C:\\bars.json') -> 'parsed_data':
    with open(filepath, encoding='utf-8') as file:
        return json.load(file)


def get_biggest_bar(parsed_data) -> str:
    return max(parsed_data['features'],
               key=lambda x: x['properties']['Attributes']['SeatsCount']
               )['properties']['Attributes']['Name']


def get_smallest_bar(parsed_data) -> str:
    return min(parsed_data['features'],
               key=lambda x: x['properties']['Attributes']['SeatsCount'])['properties']['Attributes']['Name']


def get_closest_bar(parsed_data) -> str:
    longitude = float(sys.argv[2]) if sys.argv[2] else 0
    latitude = float(sys.argv[3]) if sys.argv[2] else 0

    def distanse(coordinates): return math.sqrt((coordinates[0] - longitude)**2 + (coordinates[1] - latitude)**2)

    return min(parsed_data['features'],
               key=lambda x: distanse(x['geometry']['coordinates']))['properties']['Attributes']['Name']


if __name__ == '__main__':
    try:
        print('Самый большой бар: ', get_biggest_bar(load_data(sys.argv[1])))
        print('Самый маленький бар: ', get_smallest_bar(load_data(sys.argv[1])))
        print('Самый близкий бар: ', get_closest_bar(load_data(sys.argv[1])))
    except IndexError:
        print('Вы не указали путь к файлу')
    except IOError:
        print('Не удалось открыть файл')
    except json.decoder.JSONDecodeError:
        print('Указанный файл не в формате json')
    except ValueError:
        print('Неверно указаны параметры ширины и долготы')
