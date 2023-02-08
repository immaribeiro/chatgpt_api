import openai
import requests

# curl=`cat <<EOS
# curl https://api.openai.com/v1/completions \
#   -H 'Content-Type: application/json' \
#   -H "Authorization: Bearer $BEARER" \
#   -d '{
#   "model": "$MODEL",
#   "prompt": "$PROMPT",
#   "max_tokens": $MAX_TOKEN,
#   "temperature": $TEMPERATURE
# }' \
# --insecure 2>/tmp/chatgpt_err | jq '.choices[]'.text | cut -c 6-
# EOS`
# result=`eval ${curl}`
# exit_code=$?


model = ''
max_token = ''
temperature = ''
organization = 'org-Te0QXojeSCHgbq7jA89nsaRE'
api_key = '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'
size='1024x1024'
number_of_images=4

def authentication(api_key, organization):
    url = 'https://api.openai.com/v1/models'
    headers = 'Authorization: Bearer ' + api_key + ';' + 'OpenAI-Organization: ' + organization

openai.organization = organization
openai.api_key = api_key
engines_list = openai.Model.list()
engines_list.data[0].id

    
#prompt = input("What would you like to ask? \n " )
prompt = 'where is lisbon?'
prompt_image = 'a whitch flying on the back of a puppy'


def download_images(image_data):
    image_counter = 0    
    for image in image_data['data']:
        url = image['url']
        response = requests.get(url)
        image_counter += 1
        with open(f'image_' + prompt_image.replace(" ", "_") + '_' + str(image_counter) + '.png' , 'wb') as f:
            f.write(response.content)


def openai_chatbot(prompt):
    engine = engines_list.data[0].id
    completion = openai.Completion.create(engine=engine, prompt=prompt)
    print(completion.choices[0].text)
    return completion

#openai_chatbot(prompt)

def get_images(prompt_image):
    image_data = openai.Image.create(prompt=prompt_image, n=number_of_images, size=size)
    download_images(image_data)

get_images(prompt_image)



