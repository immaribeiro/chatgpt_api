# chatgpt_api

This is just a test on python using openai sdk

## Help:
### usage: config [-h] [-i IMAGE_DATA] [-c CODE_DATA] [-t TEXT_DATA]

### optional arguments: 

```bash
  -h,            --help                show this help message and exit
  
  -i IMAGE_DATA (String), --image IMAGE_DATA    Give the prompt to generate an image
  
  -c CODE_DATA (String),  --code  CODE_DATA     Give the prompt to generate code
  
  -t TEXT_DATA (String),  --text  TEXT_DATA     Give the prompt to generate text
```
  
  
  
## Usage Example:

```bash
  ./config -i "two people having coffee" -c "generate a simple python script" -t "what is the capital of Portugal?"
```

Can be used with multiple types of requestes or only one:
```bash
  ./config -i "two dogs having coffee"
```
  
  