from utils.logger import get_logger
from utils.args_parser import create_parser

#from tools.ascii import ascii

def start():
    parser = create_parser()
    args = parser.parse_args()

    logger = get_logger(__name__, 'start.log')
    logger.info('ARGUMENTS: ' + str(args))

    # ASCII :)
    # print('\n')
    # ascii('ChatGPT API', 'xtimes', 'white', 100)
    # ascii('CLI Tool', '6x10', 'grey', 100)

    if args.subcommand == 'image':
        prompt = args.prompt
        number = args.number
        size = args.size
        response_format = args.response_format
        download = args.download
        logger.info('IMAGE: ' + str(prompt) + '\nnumber: ' + str(number) + '\nsize: ' + str(size))
        from utils.get_images import get_images
        image = get_images(prompt, number, size, response_format, download)
        if image is not None:
            print('\n Image(s) generated successfully!\n')
        else:
            print('Error: Could not generate image.')
            with open('logs/utils/get_images.log', 'r') as f:
                print('\nfrom get_images log:\n' + f.readlines()[-1])


    if args.subcommand == 'img_var':
        image = args.image
        number = args.number
        size = args.size
        response_format = args.response_format
        download = args.download
        logger.info('VAR IMG: ' + str(image) + '\nnumber: ' + str(number) + '\nsize: ' + str(size))
        from utils.get_images import get_image_variations
        image = get_image_variations(image, number, size, response_format, download)
        if image is not None:
            print('\n Variation image(s) generated successfully!\n')
        else:
            print('Error: Could not generate variation image.')
            with open('logs/utils/get_image_variations.log', 'r') as f:
                print('\nfrom get_image_variations log:\n' + f.readlines()[-1])

    if args.subcommand == 'conv':
        prompt = args.prompt
        max_tokens = args.max_tokens
        temperature = args.temperature
        logger.info('CONV: ' + str(prompt) + '\nmax-tokens: ' + str(max_tokens) + '\ntemperature: ' + str(temperature))
        from utils.get_conversation import get_conversation
        conv = get_conversation(prompt, max_tokens)
        if conv != None:
            print('\nConversation started. Wait for reply.\nReply "done" to end conversation.\n')
        elif image is None:
            print('\nConversation closed.\n')

        else:
            print('Error: Could not start conversation.')
            with open('logs/utils/get_conversation.log', 'r') as f:
                print('\nfrom get_conversation log:\n' + f.readlines()[-1])

    if args.subcommand == 'code':
        prompt = args.prompt
        model = args.model
        engine = args.engine
        max_tokens = args.max_tokens
        temperature = args.temperature
        number = args.number
        top_p = args.top_p
        frequency_penalty = args.frequency_penalty
        presence_penalty = args.presence_penalty
        stop = args.stop
        logger.info('CODE: ' + str(prompt))
        from utils.get_code import get_code
        code = get_code(prompt, number, model, engine, max_tokens, temperature, top_p, frequency_penalty, presence_penalty, stop)
        if code is not None:
            print('\n---- GENERATED CODE ----\n\n' + str(code) + '\n\n- END -\n')
        else:
            print('Error: Could not generate code.')
            with open('logs/utils/get_code.log', 'r') as f:
                print('\nfrom get_code log:\n' + f.readlines()[-1])

    if args.subcommand == 'text':
        prompt = args.prompt
        logger.info('TEXT: ' + str(prompt))
        from utils.get_text import get_text
        text = get_text(args.text_data)
        if text is not None:
            print('\n---- GENERATED TEXT ----\n\n' + str(text) + '\n\n- END -\n')
        else:
            print('Error: Could not generate text.')
            with open('logs/utils/get_text.log', 'r') as f:
                print('\nfrom get_text log:\n' + f.readlines()[-1])

    else:
        print('\n * Please provide an argument and a  prompt *\nRunning -h for help\n')
       # parser.print_help()  
         
start()