import os
import re
import pathlib
import utils.validate as validate

def snake_case(value: str) -> bool:
    pattern: re.Pattern = re.compile(pattern=r'^[a-z]+(?:_[a-z]+)*$')
    return bool(pattern.fullmatch(string=value))

def folder_exists(path: pathlib.Path) -> bool:
    return path.exists()

def folder_write_permissions(path: pathlib.Path) -> bool:
    validate.folder_exists(path=path)
    return os.access(path=path, mode=os.W_OK)

def file_exists(path: pathlib.Path) -> bool:
    return path.is_file()

def file_write_permissions(path: pathlib.Path) -> bool:
    validate.file_exists(path=path)
    return os.access(path=path, mode=os.W_OK)
