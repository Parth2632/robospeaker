import os

def text_to_speech(text):
    command=f'powershell -Command "(New-Object -ComObject SAPI.SpVoice).Speak(\'{text}\')"'
    os.system(command)

if __name__ == "__main__":
    while True:
        text_to_speech("type:")
        x = input("text:")
        if x.lower()=="exit":
            break
        text_to_speech(x)
