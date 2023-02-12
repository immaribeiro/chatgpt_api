# chatgpt_api

This is a small Python CLI tool that uses OpenAI API to generate responses and output in various formats

## Help:
### usage:
```bash
config [-h] [-i IMAGE_DATA] [-c CODE_DATA] [-t TEXT_DATA]
```

### optional arguments: 

```bash
  -h,                     --help                show this help message and exit
  
  -i IMAGE_DATA (String), --image IMAGE_DATA    generate image(s) based on the prompt provided
  
  -c CODE_DATA (String),  --code  CODE_DATA     generate code based on the prompt provided
  
  -t TEXT_DATA (String),  --text  TEXT_DATA     generate text based on the prompt provided
```


## Usage Example:

```bash
  ./config -i "two people having coffee" -c "generate a simple python script" -t "what is the capital of Portugal?"
```

Can be used with multiple types of requestes or only one:
```bash
  ./config -i "two dogs having coffee"
```
  
  