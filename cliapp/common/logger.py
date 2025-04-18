import sys
import logging
import common.configuration as configuration

class MaxLevelFilter(logging.Filter):
    def __init__(self, max_level):
        super().__init__()
        self.max_level = max_level

    def filter(self, record):
        return record.levelno <= self.max_level

formatter: logging.Formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')

log: logging.Logger = logging.getLogger(name=configuration.APPLICATION_NAME)
log.setLevel(level=configuration.ROOT_LOG_LEVEL)

stdout_handler: logging.StreamHandler = logging.StreamHandler(stream=sys.stdout)
stdout_handler.setLevel(level=configuration.STDOUT_LOG_LEVEL)
stdout_handler.addFilter(filter=MaxLevelFilter(logging.INFO))
stdout_handler.setFormatter(fmt=formatter)
log.addHandler(hdlr=stdout_handler)

stderr_handler: logging.StreamHandler = logging.StreamHandler(stream=sys.stderr)
stderr_handler.setLevel(level=configuration.STDERR_LOG_LEVEL)
stderr_handler.setFormatter(fmt=formatter)
log.addHandler(hdlr=stderr_handler)

file_handler: logging.FileHandler = logging.FileHandler(filename=configuration.LOG_FILE_PATH)
file_handler.setLevel(level=configuration.FILE_LOG_LEVEL)
file_handler.setFormatter(fmt=formatter)
log.addHandler(hdlr=file_handler)
