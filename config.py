from utils.logger import get_logger
from utils.args_parser import create_parser

def start():
    parser = create_parser()
    args = parser.parse_args()

    logger = get_logger(__name__, 'start.log')
    logger.info('ARGUMENTS: ' + str(args))

    if args.subcommand == 'image':
        prompt = args.prompt
        number = args.number
        size = args.size
        logger.info('IMAGE: ' + str(prompt) + str(number) + str(size))
        from utils.get_images import get_images
        image = get_images(prompt, number, size)
        if image is not None:
            print('\n Image(s) generated successfully!\n')
        else:
            print('Error: Could not generate image.')
            with open('logs/utils/get_images.log', 'r') as f:
                print('\nfrom get_images log\n' + f.readlines()[-1])

    # if args.image_data and args.code_data and args.code_data:
    #     logger.info('IMAGE: ' + str(args.image_data))
    #     from utils.get_images import get_images
    #     image = get_images(args.image_data)
    #     if image is not None:
    #         print('\n Image(s) generated successfully!\n')
    #     else:
    #         print('Error: Could not generate image.')
    #         with open('logs/utils/get_images.log', 'r') as f:
    #             print('\nfrom get_images log\n' + f.readlines()[-1])

    #     logger.info('CODE: ' + str(args.code_data))
    #     from utils.get_code import get_code
    #     code = get_code(args.code_data)    
    #     if code is not None:
    #         print('\n---- GENERATED CODE ----\n\n' + str(code) + '\n\n- END -\n')
    #     else:
    #         print('Error: Could not generate code.')
    #         with open('logs/utils/get_code.log', 'r') as f:
    #             print('\nfrom get_code log\n' + f.readlines()[-1])

    #     logger.info('TEXT: ' + str(args.text_data))
    #     from utils.get_text import get_text
    #     text = get_text(args.text_data)
    #     if text is not None:
    #         print('\n---- GENERATED TEXT ----\n\n' + str(text) + '\n\n- END -\n')
    #     else:
    #         print('Error: Could not generate text.')
    #         with open('logs/utils/get_text.log', 'r') as f:
    #             print('\nfrom get_text log\n' + f.readlines()[-1])


    # elif args.image_data:
    #     logger.info('IMAGE: ' + str(args.image_data))
    #     from utils.get_images import get_images
    #     image = get_images(args.image_data)
    #     if image is not None:
    #         print('\n Image(s) generated successfully!\n')
    #     else:
    #         print('Error: Could not generate image.')
    #         with open('logs/utils/get_images.log', 'r') as f:
    #             print('\nfrom get_images log\n' + f.readlines()[-1])

    # elif args.code_data:
    #     logger.info('CODE: ' + str(args.code_data))
    #     from utils.get_code import get_code
    #     code = get_code(args.code_data)    
    #     if code is not None:
    #         print('\n---- GENERATED CODE ----\n\n' + str(code) + '\n\n- END -\n')
    #     else:
    #         print('Error: Could not generate code.')
    #         with open('logs/utils/get_code.log', 'r') as f:
    #             print('\nfrom get_code log\n' + f.readlines()[-1])


    # elif args.text_data:
    #     logger.info('TEXT: ' + str(args.text_data))
    #     from utils.get_text import get_text
    #     text = get_text(args.text_data)
    #     if text is not None:
    #         print('\n---- GENERATED TEXT ----\n\n' + str(text) + '\n\n- END -\n')
    #     else:
    #         print('Error: Could not generate text.')
    #         with open('logs/utils/get_text.log', 'r') as f:
    #             print('\nfrom get_text log\n' + f.readlines()[-1])

    else:
        print('Please provide either an image prompt or a code prompt \nRun with -h for help')
    
start()