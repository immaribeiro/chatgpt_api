import argparse

from utils.logger import get_logger

def add_shared_args(subparser):
    logger = get_logger(__name__, 'utils/add_shared_args.log')        
    logger.info('subparser: ' + str(subparser))
    try:
        subparser.add_argument('prompt', type=str, nargs='?', help='Prompt for ChatGPT generation')
        subparser.add_argument('--number', dest='number', type=int, help='define the number image(s) to generate')
        subparser.add_argument('--engine', dest='engine', type=str, help='define the engine to use')
        subparser.add_argument('--temperature', dest='temperature', type=float, help='the sampling temperature to use')
        subparser.add_argument('--max-tokens', dest='max_tokens', type=int, help='the maximum number of tokens to generate')
        subparser.add_argument('--stop-sequences', dest='stop_sequences', nargs='+', type=str, help='a list of stop sequences to use')
        subparser.add_argument('--presence-penalty', dest='presence_penalty', type=float, help='the presence penalty to use for text generation')
        subparser.add_argument('--frequency-penalty', dest='frequency_penalty', type=float, help='the frequency penalty to use for text generation')
        subparser.add_argument('--best-of', dest='best_of', type=int, help='the number of best outputs to return')
        subparser.add_argument('--prompt', dest='prompt', type=str, help='the prompt to use for text generation')
        subparser.add_argument('--stream', dest='stream', action='store_true', help='stream the output instead of returning it all at once')
        subparser.add_argument('--log-probabilities', dest='log_probabilities', action='store_true', help='log the probabilities of generated tokens')
        subparser.add_argument('--expand', dest='expand', nargs='+', type=str, help='the IDs of the documents to expand with the Davinci-Codex model')
        subparser.add_argument('--model', dest='model', type=str, help='the ID of the Davinci-Codex model to use')
        subparser.add_argument('--timeout', dest='timeout', type=int, help='the number of seconds to wait for a response from the API')

        #Image
        subparser.add_argument('--response-format', dest='response_format', type=str, help='The format in which the generated images are returned. Must be one of url or b64_json')
        subparser.add_argument('--size', dest='size', type=str, help='The size of the generated images. Must be one of 256x256, 512x512, or 1024x1024')
        subparser.add_argument('--download', dest='download', type=bool, help='download or not the images generated')
        subparser.add_argument('--image', dest='image', type=str, help='The image to edit. Must be a valid PNG file, less than 4MB, and square. If mask is not provided, image must have transparency, which will be used as the mask.')
        subparser.add_argument('--mask', dest='mask', type=str, help='An additional image whose fully transparent areas (e.g. where alpha is zero) indicate where image should be edited. Must be a valid PNG file, less than 4MB, and have the same dimensions as image.')

        #Code
        subparser.add_argument('--top_p', dest='top_p', type=int, help='An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.')
        subparser.add_argument('--stop', dest='stop', type=str, help='Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence.')

        return subparser
    except Exception as e:
        logger.error(f'Error occurred while creating parser: {e}')

def create_parser():
    logger = get_logger(__name__, 'utils/create_parser.log')
    try:
        parser = argparse.ArgumentParser(description='ChatGPT API CLI tool')
        subparsers = parser.add_subparsers(dest='subcommand')

        # define image argument and subarguments
        image_parser = subparsers.add_parser('image', help='generate image(s) based on provided prompt')
        add_shared_args(image_parser)

        # define conversation argument and subarguments
        conv_parser = subparsers.add_parser('conv', help='start a conversation providing initial prompt')
        add_shared_args(conv_parser)


        # define code argument and subarguments
        code_parser = subparsers.add_parser('code', help='generate code based on the prompt provided')
        add_shared_args(code_parser)

        # define text argument and subarguments
        text_parser = subparsers.add_parser('text', help='generate text based on provided prompt')
        add_shared_args(text_parser)

        # define text argument and subarguments
        img_var_parser = subparsers.add_parser('img_var', help='generate image variation based on provided image png file')
        add_shared_args(img_var_parser)

        parser.add_argument('-v', '--verbose', action='store_true', help='enable verbose output')
        parser.add_argument('--output', type=str, help='output file path')

        return parser

    except Exception as e:
        logger.error(f'Error occurred while creating parser: {e}')

create_parser()