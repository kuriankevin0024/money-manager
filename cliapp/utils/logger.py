import sys
import logging
import pathlib
import utils.check as check
import utils.validate as validate
import utils.configuration as config


class LoggerNotInitializedError(RuntimeError):
    pass


class MaxLevelFilter(logging.Filter):
    def __init__(self, max_level):
        super().__init__()
        self.max_level = max_level

    def filter(self, record):
        return record.levelno <= self.max_level


class ApplicationLogger:
    __logger: logging.Logger = None

    def __init__(self, application_name: str, log_file_path: pathlib.Path = None):
        self.__application_name: str = application_name
        self.__log_file_path: pathlib.Path = log_file_path
        if ApplicationLogger.__logger is None:
            ApplicationLogger.__logger = self.__initialize_logger()

    def __initialize_logger(self) -> logging.Logger:
        formatter: logging.Formatter = logging.Formatter(
            fmt='%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s')

        validate.snake_case(value=self.__application_name)
        logger: logging.Logger = logging.getLogger(name=self.__application_name)
        logger.setLevel(level=config.ROOT_LOG_LEVEL)

        stdout_handler: logging.StreamHandler = logging.StreamHandler(stream=sys.stdout)
        stdout_handler.setLevel(level=config.STDOUT_LOG_LEVEL)
        stdout_handler.addFilter(filter=MaxLevelFilter(logging.INFO))
        stdout_handler.setFormatter(fmt=formatter)
        logger.addHandler(hdlr=stdout_handler)

        stderr_handler: logging.StreamHandler = logging.StreamHandler(stream=sys.stderr)
        stderr_handler.setLevel(level=config.STDERR_LOG_LEVEL)
        stderr_handler.setFormatter(fmt=formatter)
        logger.addHandler(hdlr=stderr_handler)

        if self.__log_file_path is not None:
            log_path = self.__log_file_path.resolve().parent
            validate.folder_write_permissions(path=log_path)
            if check.file_exists(path=self.__log_file_path):
                validate.file_write_permissions(path=self.__log_file_path)

            file_handler: logging.FileHandler = logging.FileHandler(filename=self.__log_file_path)
            file_handler.setLevel(level=config.FILE_LOG_LEVEL)
            file_handler.setFormatter(fmt=formatter)
            logger.addHandler(hdlr=file_handler)

        return logger

    @classmethod
    def get_logger(cls) -> logging.Logger:
        if cls.__logger is None:
            raise LoggerNotInitializedError("create instance of ApplicationLogger before calling get_logger()")
        return cls.__logger
