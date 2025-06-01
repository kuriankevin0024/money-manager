import os
import pathlib
import logging
from enum import StrEnum


class DefaultConfig(StrEnum):
    APPLICATION_NAME = 'money_manager'
    LOG_PATH = '/tmp'
    ROOT_LOG_LEVEL = logging.getLevelName(logging.DEBUG)  # 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
    STDOUT_LOG_LEVEL = logging.getLevelName(logging.INFO)  # 'DEBUG', 'INFO'
    STDERR_LOG_LEVEL = logging.getLevelName(logging.WARNING)  # 'WARNING', 'ERROR', 'CRITICAL'
    FILE_LOG_LEVEL = logging.getLevelName(logging.DEBUG)  # 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'


# ----- application config -----
APPLICATION_NAME: str = os.getenv(DefaultConfig.APPLICATION_NAME.name, DefaultConfig.APPLICATION_NAME.value)
# ----- ----- ----- ----- -----

# ----- logger config -----
ROOT_LOG_LEVEL: int = getattr(logging, os.getenv(DefaultConfig.ROOT_LOG_LEVEL.name, DefaultConfig.ROOT_LOG_LEVEL.value).upper())

STDOUT_LOG_LEVEL: int = getattr(logging, os.getenv(DefaultConfig.STDOUT_LOG_LEVEL.name, DefaultConfig.STDOUT_LOG_LEVEL.value).upper())
STDERR_LOG_LEVEL: int = getattr(logging, os.getenv(DefaultConfig.STDERR_LOG_LEVEL.name, DefaultConfig.STDERR_LOG_LEVEL.value).upper())

LOG_PATH: pathlib.Path = pathlib.Path(os.getenv(DefaultConfig.LOG_PATH.name, DefaultConfig.LOG_PATH.value))
LOG_FILE_PATH: pathlib.Path = LOG_PATH / f'{APPLICATION_NAME}.log'
FILE_LOG_LEVEL: int = getattr(logging, os.getenv(DefaultConfig.FILE_LOG_LEVEL.name, DefaultConfig.FILE_LOG_LEVEL.value).upper())
# ----- ----- ----- ----- -----
