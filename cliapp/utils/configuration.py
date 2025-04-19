import pathlib
import logging

# ----- application config -----
APPLICATION_NAME: str = 'money_manager'
# ----- ----- ----- ----- -----

# ----- logger config -----
ROOT_LOG_LEVEL: int = logging.DEBUG  # 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'

STDOUT_LOG_LEVEL: int = logging.INFO  # 'DEBUG', 'INFO'
STDERR_LOG_LEVEL: int = logging.WARNING  # 'WARNING', 'ERROR', 'CRITICAL'

LOG_PATH: pathlib.Path = pathlib.Path('/tmp')
LOG_FILE_PATH: pathlib.Path = LOG_PATH / f'{APPLICATION_NAME}.log'
FILE_LOG_LEVEL: int = logging.DEBUG  # 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
# ----- ----- ----- ----- -----
