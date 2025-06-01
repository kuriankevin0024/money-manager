import logging
import uvicorn
import utils.configuration as config
from utils.logger import ApplicationLogger

application_logger: ApplicationLogger = ApplicationLogger(application_name=config.APPLICATION_NAME)
logger: logging.Logger = application_logger.get_logger()

from persistence.db import initialize_db
from cliapp.controllers.expense_controller import application


def validate_prerequisites():
    pass


if __name__ == '__main__':
    print(f"application '{config.APPLICATION_NAME}' starting...")
    validate_prerequisites()
    logger.info(f"application '{config.APPLICATION_NAME}' starting...")
    initialize_db()
    uvicorn.run('cliapp.cliapp_main:application', host='127.0.0.1', port=8000, reload=True)
    logger.info(f'application execution completed')
