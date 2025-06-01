import os
import re
import pathlib


def snake_case(value: str) -> None:
    pattern: re.Pattern = re.compile(pattern=r'^[a-z]+(?:_[a-z]+)*$')
    if not bool(pattern.fullmatch(string=value)):
        raise ValueError(f'not valid snake case. value:{value}')


def folder_exists(path: pathlib.Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"folder '{path}' does not exist")


def folder_write_permissions(path: pathlib.Path) -> None:
    folder_exists(path=path)
    if not os.access(path=path, mode=os.W_OK):
        raise PermissionError(f"no write permission for folder '{path}'")


def file_exists(path: pathlib.Path) -> None:
    if not path.is_file():
        raise FileNotFoundError(f"file '{path}' does not exist")


def file_write_permissions(path: pathlib.Path) -> None:
    file_exists(path=path)
    if not os.access(path=path, mode=os.W_OK):
        raise PermissionError(f"no write permission for file '{path}'")
