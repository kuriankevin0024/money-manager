import utils.check as check
import utils.validate as validate
import utils.configuration as conf

from utils.logger import log

def prerequisites():
    validate.snake_case(value=conf.APPLICATION_NAME)
    validate.folder_write_permissions(path=conf.LOG_PATH)
    if check.file_exists(path=conf.LOG_FILE_PATH):
        validate.file_write_permissions(path=conf.LOG_FILE_PATH)

if __name__ == '__main__':
    print(f"application '{conf.APPLICATION_NAME}' starting...")
    prerequisites()
    log.info(f"application '{conf.APPLICATION_NAME}' starting...")

    log.info(f'application execution completed')
