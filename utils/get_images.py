import requests
import json
import os
import openai

prompt_image = input('\nWhat image do you want? \n')

def download_images(response):
    os.makedirs('images_output/', exist_ok=True)
    images_output_path = 'images_output/'
    image_counter = 0    
    for image in response['data']:
        url = image['url']
        response = requests.get(url)
        image_counter += 1

        with open(images_output_path + 'image_' + prompt_image.replace(" ", "_") + '_' + str(image_counter) + '.png' , 'wb') as f:
            f.write(response.content)


def get_images(prompt_image):
    image_size='256x256'
    image_number=1
    response = openai.Image.create(prompt=prompt_image, n=image_number, size=image_size)
    os.makedirs('json_responses', exist_ok=True)
    response_json = json.dumps(response, indent=4)

    with open('json_responses/' + 'images_response_' + prompt_image + '.json' , 'wb') as f:
            f.write(response_json.encode())
    download_images(response)

get_images(prompt_image)


#def create_image_variatoins(json_response): WIP