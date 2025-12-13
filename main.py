import os
from groq import Groq
from rgbprint import gradient_print, Color, rgbprint
import textwrap

api = "token"
model = "openai/gpt-oss-120b" # or others

def wrap_text(text, width=80, indent=3):
    wrapped = textwrap.fill(text, width=width-indent)
    lines = wrapped.split('\n')
    if len(lines) > 0:
        indented_lines = [lines[0]] + [' ' * indent + line for line in lines[1:]]
    else:
        indented_lines = []
    return '\n'.join(indented_lines)

def main():
    client = Groq(api_key=api)
    os.system('cls' if os.name == 'nt' else 'clear')
    gradient_print("""
 __       ______                
 \ \     / ____/________  ____ _
  \ \   / / __/ ___/ __ \/ __ `/
  / /  / /_/ / /  / /_/ / /_/ / 
 /_/   \____/_/   \____/\__, /  
                          /_/   
    """, start_color=Color.orange, end_color=Color.orange_red)

    while True:
        inp = input(f"{Color.white_smoke} > ")
        
        if inp.lower() in ['exit']: break
        
        if not inp.strip():
            print("")
            continue

        try:
            chat = client.chat.completions.create(messages=[{"role": "user","content": inp,}],model=model)
            text = wrap_text(chat.choices[0].message.content)
            rgbprint(f"{Color.beige}\n [ " + text + " ]\n")
            usage = chat.usage

        except Exception as e:
            print(f"\n\n{Color.red} [ Error: {e} ]\n")

if __name__ == "__main__":
    main()
