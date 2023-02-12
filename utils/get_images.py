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
            with open(images_output_path + prompt_image_short.replace(" ", "_") + '_' + str(image_counter) + current_time +'.png' , 'wb') as f:
                f.write(response.content)
        
        return f
    except Exception as e:
        logger.debug(f'An error occurred while downloading images: {str(e)}')



def get_images(prompt_image):
    try:
        logger = get_logger(__name__, 'utils/get_images.log')
        image_size='256x256'
        image_number=1
        response = openai.Image.create(prompt=prompt_image, n=image_number, size=image_size)
        download_images(response, prompt_image)
        os.makedirs('output/json/images', exist_ok=True)
        response_json = json.dumps(response, indent=4)
        current_time = str(int(time.time()))
        prompt_image_short = prompt_image[:min(len(prompt_image), 30)]
        with open('output/json/images/' + prompt_image_short.replace(" ", "_") + current_time + '.json' , 'wb') as f:
                f.write(response_json.encode())
        return response
    except Exception as e:
        logger.debug(f'An error occurred while generating images: {str(e)}')



#def create_image_variatoins(json_response): WIP