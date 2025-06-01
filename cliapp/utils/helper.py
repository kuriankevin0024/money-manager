import os
import pathlib


def get_parent_directory(file: pathlib.Path):
    return file.resolve().parent


def _get_parent_directory(file: str):
    return os.path.dirname(file)
