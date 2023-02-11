import openai
import os
import json

#prompt_code = input('\nWhat code you want to generate?  \n')

def get_code(prompt_code):
    os.makedirs('code_output/', exist_ok=True)
    completion = openai.Completion.create(
            engine='davinci-codex',
            prompt=prompt_code,
            max_tokens=200,
            n=1,
            stop=None,
            temperature=0.1,
            frequency_penalty=0.9,
            presence_penalty=0.6,
            #model="text-davinci-002"
        )
    
    #selecting only the first result to print
    code = completion.choices[0].text
    #writing to file all the results
    with open('code_output/' + prompt_code + '.json' , 'wb') as f:
            f.write(json.dumps(completion).encode())

    return code
