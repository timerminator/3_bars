import json
import sys
import math


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file:
        return json.load(file)


def get_biggest_bar(data):
    return max(data['features'],
               key=lambda x: x['properties']['Attributes']['SeatsCount']
               )['properties']['Attributes']['Name']


def get_smallest_bar(data):
    return min(data['features'],
               key=lambda x: x['properties']['Attributes']['SeatsCount']
               )['properties']['Attributes']['Name']


def get_closest_bar(data, longitude=0, latitude=0):
    def distanse(coordinates):
       return math.sqrt((coordinates[0] - longitude)**2 + (coordinates[1] - latitude)**2)

    return min(data['features'],
               key=lambda x: distanse(x['geometry']['coordinates'])
               )['properties']['Attributes']['Name']


if __name__ == '__main__':
    try:
        print('Самый большой бар: ', get_biggest_bar(load_data(sys.argv[1])))
        print('Самый маленький бар: ', get_smallest_bar(load_data(sys.argv[1])))
        if len(sys.argv) == 4:
            print('Самый близкий бар: ',
                  get_closest_bar(load_data(sys.argv[1]),
                                  float(sys.argv[2]),
                                  float(sys.argv[3])))
        elif len(sys.argv) == 2:
            print('Самый близкий бар: ', get_closest_bar(load_data(sys.argv[1])))
    except IndexError:
        print('Вы не указали путь к файлу')
    except IOError:
        print('Не удалось открыть файл')
    except json.decoder.JSONDecodeError:
        print('Указанный файл не в формате json')
