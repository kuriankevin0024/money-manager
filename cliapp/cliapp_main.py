import utils.configuration as config

import logging
from utils.logger import ApplicationLogger

application_logger: ApplicationLogger = ApplicationLogger(application_name=config.APPLICATION_NAME)
logger: logging.Logger = application_logger.get_logger()


def validate_prerequisites():
    pass


if __name__ == '__main__':
    print(f"application '{config.APPLICATION_NAME}' starting...")
    validate_prerequisites()
    logger.info(f"application '{config.APPLICATION_NAME}' starting...")

    logger.info(f'application execution completed')
