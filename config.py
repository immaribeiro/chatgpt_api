import os
import openai
import re
import sys

from utils.logger import get_logger

def set_api_key():
    logger = get_logger(__name__, 'config.log')

    new_api_key = input('Do you have a new API KEY? (y/n) \n')

    if new_api_key in ['y', 'yes', 'Y']:
        api_key = input('New API Key: ')
        os.environ['OPENAI_API_KEY'] = api_key
        openai.api_key = os.environ['OPENAI_API_KEY']
        print('New API key set!')
        logger.info('New API key set')

    elif new_api_key in ['n', 'no', 'N']:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            logger.error('API key is not set')
            print('API key is not set!')
            set_api_key()
        else:
            openai.api_key = api_key

    else:
        logger.error('Invalid input: %s', new_api_key)
        print('Wrong answer!')

    return openai.api_key


def is_valid_openai_key(api_key):
    pattern = r'^sk-[a-zA-Z0-9]{48}$'
    return bool(re.match(pattern, api_key))


def check_api_key():
    logger = get_logger(__name__, 'config.log')
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or not is_valid_openai_key(api_key):
        print('API key is not set!')
        logger.info('API key is not set! Requesting new one')
        set_api_key()
    else:
        openai.api_key = api_key
        print('API key set from env variable!')


def start():
    logger = get_logger(__name__, 'start.log')

    start = input('Use ChatGPT to generate? \n(1) Image \n(2) Code \n\n')
    if start in ['image', 'Image', 'I', 'i', '1']:
        logger.info('User chose to generate IMAGE')
        from utils.get_images import get_images
        


    elif start in ['code', 'Code', 'C', 'c', '2']:
        logger.info('User chose to generate CODE')
        from utils.get_code import get_code        

    else:
        print('wrong answer! \n')
        sys.exit()

start()
