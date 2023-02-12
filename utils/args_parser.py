import argparse

from utils.logger import get_logger

def create_parser():
    logger = get_logger(__name__, 'utils/create_parser.log')
    try:
        parser = argparse.ArgumentParser(description='ChatGPT API CLI tool')

        subparsers = parser.add_subparsers(dest='subcommand')

        # define image arguments
        image_parser = subparsers.add_parser('image', help='generate image(s) based on the prompt provided')
        image_parser.add_argument('prompt', type=str, help='Prompt for image generation')   
        image_parser.add_argument('--size', dest='size', type=str, help='define the size the generated image(s) to a specific width', default="256x256")
        image_parser.add_argument('--number', dest='number', type=int, help='define the number image(s) to generate', default=1)

        # define conversation arguments
        conv_parser = subparsers.add_parser('conv', help='start a conversation providing initial prompt')
        conv_parser.add_argument('prompt', type=str, help='Prompt for conversation start')   

        # code_parser = subparsers.add_parser('code', dest='code_data', help='generate code based on the prompt provided')
        # code_parser.add_argument('prompt', type=str, help='Prompt for image generation')   
        # code_parser.add_argument('--size', dest='size', type=str, help='define the size the generated image(s) to a specific width', default="256x256")
        # code_parser.add_argument('--temperature', dest='temperature', default=0.5, type=float, help='the sampling temperature to use')

        # text_parser = subparsers.add_parser('text', dest='text_data', help='generate text based on the prompt provided')
        # text_parser.add_argument('prompt', type=str, help='Prompt for image generation')   
        # text_parser.add_argument('--size', dest='size', type=str, help='define the size the generated image(s) to a specific width', default="256x256")

        #parser.add_argument('-v', '--verbose', action='store_true', help='enable verbose output')
        parser.add_argument('--output', type=str, help='output file path')

        return parser

    except Exception as e:
        logger.debug(f'An error occurred while parsing the arguments: {str(e)}')

create_parser()

# engine_parser = subparsers.add_parser('engine')


# code_parser = subparsers.add_parser('code', help='generate code based on the prompt provided')
# code_parser.add_argument('-c', '--code', dest='code_data', help='generate code based on the prompt provided')
# engine_parser.add_argument('--engine', dest='engine', default='davinci-codex', type=str, help='define the engine to use')


# text_parser = subparsers.add_parser('text', help='generate text based on the prompt provided')
# text_parser.add_argument('-t', '--text', dest='code_data', help='generate text based on the prompt provided')

# engine_parser.add_argument('--engine', dest='engine', default='davinci-codex', type=str, help='define the engine to use')
# engine_parser.add_argument('--temperature', dest='temperature', default=0.5, type=float, help='the sampling temperature to use')
# engine_parser.add_argument('--max-tokens', dest='max_tokens', default=2048, type=int, help='the maximum number of tokens to generate')
# engine_parser.add_argument('--stop-sequences', dest='stop_sequences', default=[], nargs='+', type=str, help='a list of stop sequences to use')
# engine_parser.add_argument('--presence-penalty', dest='presence_penalty', default=0.0, type=float, help='the presence penalty to use for text generation')
# engine_parser.add_argument('--frequency-penalty', dest='frequency_penalty', default=0.0, type=float, help='the frequency penalty to use for text generation')
# engine_parser.add_argument('--best-of', dest='best_of', default=1, type=int, help='the number of best outputs to return')
# engine_parser.add_argument('--prompt', dest='prompt', default='', type=str, help='the prompt to use for text generation')
# engine_parser.add_argument('--stream', dest='stream', action='store_true', help='stream the output instead of returning it all at once')
# engine_parser.add_argument('--log-probabilities', dest='log_probabilities', action='store_true', help='log the probabilities of generated tokens')
# engine_parser.add_argument('--expand', dest='expand', default=[], nargs='+', type=str, help='the IDs of the documents to expand with the Davinci-Codex model')
# engine_parser.add_argument('--model', dest='model', default=None, type=str, help='the ID of the Davinci-Codex model to use')
# engine_parser.add_argument('--timeout', dest='timeout', default=60, type=int, help='the number of seconds to wait for a response from the API')

# define additional arguments for the Davinci-Codex engine

