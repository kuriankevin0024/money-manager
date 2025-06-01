import os
import re
import pathlib


def is_snake_case(value: str) -> bool:
    pattern: re.Pattern = re.compile(pattern=r'^[a-z]+(?:_[a-z]+)*$')
    return bool(pattern.fullmatch(string=value))


def is_path_absolute(path: pathlib.Path) -> bool:
    return path.is_absolute()


def does_folder_exist(path: pathlib.Path) -> bool:
    return path.exists() and path.is_dir()


def is_folder_writable(path: pathlib.Path) -> bool:
    return os.access(path=path, mode=os.W_OK)


def does_file_exist(path: pathlib.Path) -> bool:
    return path.exists() and path.is_file()


def is_file_writable(path: pathlib.Path) -> bool:
    return os.access(path=path, mode=os.W_OK)


def _is_path_absolute(path: str) -> bool:
    return os.path.isabs(path)


def _does_folder_exist(path: str) -> bool:
    return os.path.exists(path) and os.path.isdir(path)


def _does_file_exist(path: str) -> bool:
    return os.path.exists(path) and os.path.isfile(path)
