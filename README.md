# chatgpt_api

This is a small Python CLI tool that uses OpenAI API to generate responses and output in various formats

## Help:
### usage:
```bash
config.py [-h] [-v] [--output OUTPUT] {image,conv,code,text,img_var} ...
```

### positional arguments: 

```bash
  {image,conv,code,text,img_var}
    image               generate image(s) based on provided prompt
    conv                start a conversation providing initial prompt
    code                generate code based on the prompt provided
    text                generate text based on provided prompt
    img_var             generate image variation based on provided image png file
```
### optional arguments:
```bash
  -h, --help            show this help message and exit
  -v, --verbose         enable verbose output
  --output OUTPUT       output file path
```

## Usage Example:


```bash
  ./config image "two people having coffee" --download false --number 4
  ./config conv "hello"
```
  
  