import openai
import os
import json
import time

from utils.logger import get_logger

def get_code(prompt_code):
    logger = get_logger(__name__, 'utils/get_code.log')
    try:
        os.makedirs('output/code/', exist_ok=True)
        completion = openai.Completion.create(
                engine='davinci-codex',
                prompt=prompt_code,
                max_tokens=128,
                #n=1,
                #stop=None,
                #top_p=0.9,
                temperature=0.1,
                frequency_penalty=0.9,
                presence_penalty=0.6,
                #model="text-davinci-002"
            )

        #selecting only the first result to print
        code = completion.choices[0].text
        #writing to file all the results
        current_time = str(int(time.time()))
        prompt_code_short = prompt_code[:min(len(prompt_code), 30)]
        with open('output/code/' + prompt_code_short.replace(" ", "_") + current_time +'.json' , 'wb') as f:
                f.write(json.dumps(completion).encode())
        return code

    except Exception as e:
        logger.debug(f'An error occurred while generating code: {str(e)}')