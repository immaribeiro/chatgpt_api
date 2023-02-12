import openai
import os
import json
import time

from utils.logger import get_logger

prompt_code = 'test'

def get_code(prompt_code):
    logger = get_logger(__name__, 'utils/get_code.log')
    try:
        os.makedirs('output/code/', exist_ok=True)
        model_engine = 'davinci-codex'
        #max_tokens = 128
        #temperature = 0.1
        #top_p = 0.9
        frequency_penalty = 0.1
        presence_penalty = 0.1
        max_tokens=1024
        n=1
        stop=None
        temperature=0.5

        response = openai.Completion.create(
                engine=model_engine,
                prompt=prompt_code,
                max_tokens=max_tokens,
                n=n,
                stop=stop,
                #top_p=top_p,
                temperature=temperature,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
            )

        #selecting only the first result to print
        code = response.choices[0].text
        #writing to file all the results
        current_time = str(int(time.time()))
        prompt_code_short = prompt_code[:min(len(prompt_code), 30)]
        filename = prompt_code_short.replace(" ", "_") + '_' + current_time +'.json'
        with open('output/code/' + filename, 'wb') as f:
                f.write(json.dumps(response).encode())
        logger.info('New code request made successfuly and saved in file ' + filename)
        return code

    except Exception as e:
        logger.debug(f'An error occurred while generating code: {str(e)}')
get_code(prompt_code)