import os
import argparse
import yaml
import re

def test_function(directory, patterns):
    try:
        for pattern in patterns:
            if '/' in pattern:
                raise ValueError
    except ValueError:
        print('An error occurred, script terminated')
    else:
        directory_for_scan = os.path.join(yml_folder, directory)
        try:
            dir_files = [os.path.join(directory_for_scan, i) for i in os.listdir(directory_for_scan)]
            if not dir_files:
                print('No files found')
            else:
                [print(i) for i in dir_files for pattern in patterns if re.search(pattern, i)]
        except FileNotFoundError:
            try:
                raise ValueError
            except ValueError:
                print('An error occurred, script terminated')

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--config', nargs="+")  # Абсолютный путь к файлу конфигурации может содержать пробелы,
# поэтому создаем список, который потом преобразуем в строку
my_namespace = parser.parse_args()
path_to_yml = ' '.join(my_namespace.config)
flag = False
if path_to_yml.endswith('.yml'):
    absolute_path_to_yml = os.path.join(os.path.dirname(__file__), path_to_yml) # Если путь к файлу .yml относительный,
# то поиск происходит относительно каталога, в котором мы находились, когда запускали скрипт. Поэтому назначаем еще одно
# место, относительно которого будет вестись поиск - директорию, в которой находится сам модуль .py (если же path_to_yml
# - абсолютный, то absolute_path_to_yml будет идентичен ему)
    possible_pathes_to_yml = [absolute_path_to_yml, path_to_yml]
    for i in range(2):
        try:
            with open(possible_pathes_to_yml[i]) as file:
                dir_pat = yaml.safe_load(file)
                directory = dir_pat['directory']
                patterns = dir_pat['patterns']
                if i == 0:
                    yml_folder = os.path.dirname(os.path.abspath(absolute_path_to_yml))
                else:
                    yml_folder = os.getcwd()
                flag = True
                break
        except FileNotFoundError:
            if i == 0:
                continue
            else:
                print('Configuration file not found.')
else:
    print('Configuration file not found')
if flag:
    test_function(directory, patterns)














