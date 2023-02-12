import openai
import os
import json
import time

from utils.logger import get_logger

def get_text(prompt_text):
    logger = get_logger(__name__, 'utils/get_text.log')
    try:
        os.makedirs('output/text/', exist_ok=True)
        model_engine = "davinci"
        max_tokens = 128
        temperature = 0.7
        top_p = 0.9
        frequency_penalty = 0.0
        presence_penalty = 0.0

        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt_text,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )

        #selecting only the first result to print
        text = response.choices[0].text
        #writing to file all the results
        current_time = str(int(time.time()))
        prompt_text_short = prompt_text[:min(len(prompt_text), 30)]
        with open('output/text/' + prompt_text_short.replace(" ", "_") + current_time + '.json' , 'wb') as f:
                f.write(json.dumps(response).encode())
        return text

    except Exception as e:
        logger.debug(f'An error occurred while generating text: {str(e)}')

