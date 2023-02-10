import os
import openai
import requests
import json

# model = ''
# max_token = ''
# temperature = ''

image_size='256x256'
image_number=1

file_path = 'output/'

#openai.organization = organization
openai.api_key = os.getenv("OPENAI_API_KEY")

#openai.api_key = api_key
engines_list = openai.Model.list()

    
#prompt = input("What would you like to ask? \n " )
prompt = 'where is lisbon?'
prompt_image = 'bruno nogueira a beijar nuno markl'


def download_images(response):
    image_counter = 0    
    for image in response['data']:
        url = image['url']
        response = requests.get(url)
        image_counter += 1
        with open(file_path + 'image_' + prompt_image.replace(" ", "_") + '_' + str(image_counter) + '.png' , 'wb') as f:
            f.write(response.content)


def openai_chatbot(prompt):
    engine = engines_list.data[0].id
    completion = openai.Completion.create(engine=engine, prompt=prompt)
    print(completion.choices[0].text)
    return completion

#openai_chatbot(prompt)

def get_images(prompt_image):
    response = openai.Image.create(prompt=prompt_image, n=image_number, size=image_size)
    os.makedirs('json_responses', exist_ok=True)

    response_json = json.dumps(response, indent=4)
    with open(file_path + 'images_response_' + prompt_image + '.json' , 'wb') as f:
            f.write(response_json.encode())
    download_images(response)

get_images(prompt_image)

#def create_image_variatoins(json_response):