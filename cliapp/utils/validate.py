import os
import re
import pathlib


def is_snake_case(value: str) -> None:
    pattern: re.Pattern = re.compile(pattern=r'^[a-z]+(?:_[a-z]+)*$')
    if not bool(pattern.fullmatch(string=value)):
        raise ValueError(f'not valid snake case. value:{value}')


def is_path_absolute(path: pathlib.Path) -> None:
    if not path.is_absolute():
        raise ValueError(f"path '{path}' is not absolute")


def does_folder_exist(path: pathlib.Path) -> None:
    if not path.exists() or not path.is_dir():
        raise FileNotFoundError(f"folder '{path}' does not exist")


def is_folder_writable(path: pathlib.Path) -> None:
    if not os.access(path=path, mode=os.W_OK):
        raise PermissionError(f"folder '{path}' doesnt have write permissions")


def does_file_exist(path: pathlib.Path) -> None:
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"file '{path}' does not exist")


def is_file_writable(path: pathlib.Path) -> None:
    if not os.access(path=path, mode=os.W_OK):
        raise PermissionError(f"file '{path}' doesnt have write permission")


def _is_path_absolute(path: str) -> None:
    if not os.path.isabs(path):
        raise ValueError(f"path '{path}' is not absolute")


def _does_folder_exist(path: str) -> None:
    if not os.path.exists(path) or not os.path.isdir(path):
        raise FileNotFoundError(f"folder '{path}' does not exist")


def _does_file_exist(path: str) -> None:
    if not os.path.exists(path) or not os.path.isfile(path):
        raise FileNotFoundError(f"file '{path}' does not exist")
