import openai

prompt_code = input('\nWhat code you want to generate?  \n')
#prompt_code = 'How do I read a CSV file in Python?'

def get_code(prompt_code):
    completion = openai.Completion.create(
            engine='davinci-codex',
            prompt=prompt_code,
            max_tokens=200,
            n=5,
            stop=None,
            temperature=0.1,
            frequency_penalty=0.9,
            presence_penalty=0.6,
            #model="text-davinci-002"
        )

    print(completion.choices[0].text)
   # return completion
get_code(prompt_code)