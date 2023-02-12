import logging
import os

def get_logger(name, filename):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Log to file
    logs_dir = os.path.join(os.getcwd(), 'logs')
    logs_utils_dir = os.path.join(logs_dir, 'utils')
    os.makedirs(logs_dir, exist_ok=True)
    os.makedirs(logs_utils_dir, exist_ok=True)
    file_handler = logging.FileHandler(os.path.join(logs_dir, filename))
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
