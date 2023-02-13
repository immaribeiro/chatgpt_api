import requests
import json
import os
import openai
import time

from utils.logger import get_logger

def download_images(response, prompt_image):
    logger = get_logger(__name__, 'utils/download_images.log')
    try:
        os.makedirs('output/images/', exist_ok=True)
        images_output_path = 'output/images/'
        image_counter = 0    
        for image in response['data']:
            url = image['url']
            response = requests.get(url)
            image_counter += 1
            current_time = str(int(time.time()))
            prompt_image_short = prompt_image[:min(len(prompt_image), 30)]
            filename = prompt_image_short.replace(" ", "_") + '_' + str(image_counter) + '_' + current_time +'.png'
            with open(images_output_path + filename, 'wb') as f:
                f.write(response.content)
            logger.info('New image file downloaded: ' + filename)
        
        return f
    except Exception as e:
        logger.debug(f'An error occurred while downloading images: {str(e)}')

def get_images(prompt=None, number=None, size=None, response_format=None, download=None):
    logger = get_logger(__name__, 'utils/get_images.log')
    try:
        os.makedirs('output/json/images', exist_ok=True)
        os.makedirs('utils/configs/images', exist_ok=True)

        # Load default values from json file
        with open('utils/configs/images/get_images_config.json') as f:
            config = json.load(f)
                
        args = {
            'prompt': prompt or config.get('prompt'),
            'n': number or config.get('number'),
            'size': size or config.get('size'),
            'response_format': response_format or config.get('response_format'),
        }

        args = {k: v for k, v in args.items() if v is not None}
        
        response = openai.Image.create(**args)

        #Download images from url
        if download is None:
            download = config.get('download')
        if download:
            download_images(response, prompt)
        else:
            response_json = json.dumps(response, indent=4)
            current_time = str(int(time.time()))
            prompt_image_short = prompt[:min(len(prompt), 30)]
            filename = prompt_image_short.replace(" ", "_") + '_' + current_time + '.json'
            with open('output/json/images/' + filename , 'wb') as f:
                    f.write(response_json.encode())
            logger.info('New image request successfully created - saved as json file' + filename)
        return response

    except Exception as e:
        logger.debug(f'An error occurred while generating images: {str(e)}')

#def create_image_variatoins(json_response): WIP