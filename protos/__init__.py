import sys
import os


def init_protobuf_path():
    current_folder = os.path.dirname(os.path.abspath(__file__))
    print(f'protobuf folder = {current_folder}')
    sub_folders = [f.name for f in os.scandir(current_folder) if f.is_dir()]
    for dir_name in list(sub_folders):
        if not dir_name.startswith('__'):
            path_to_append = os.path.join(current_folder,  dir_name)
            print(f'path to append = {path_to_append}')
            sys.path.append(path_to_append)
    print(f'Python PATH={sys.path}')


init_protobuf_path()
