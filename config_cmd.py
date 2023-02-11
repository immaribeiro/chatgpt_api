import os
import openai
import re
import argparse

from utils.logger import get_logger

parser = argparse.ArgumentParser(description='My ChatGPT app')
parser.add_argument('-i', '--image', dest='image_text', help='Give the prompt to generate an image')
parser.add_argument('-c', '--code', dest='code_text', help='Give the prompt to generate code')

args = parser.parse_args()

def start():
    logger = get_logger(__name__, 'start_cmd.log')

    if args.image_text:
        logger.info('image: ' + args.image_text)
        from utils.get_images import get_images
        get_images(args.image_text)
    elif args.code_text:
        logger.info('code: ' + args.code_text)
        from utils.get_code import get_code
        get_code(args.code_text)    
        print(get_code(args.code_text))
      

    else:
        print('wrong request! \n')
    
start()