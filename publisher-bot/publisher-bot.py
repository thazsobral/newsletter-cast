from dotenv import load_dotenv
import requests
import os
import re
from time import sleep

load_dotenv()

# bot credentials
TOKEN_BOT = str(os.environ["TOKEN_BOT"])
CHAT_ID = str(os.environ["CHAT_ID"])
BASE_URL = f"https://api.telegram.org/bot{TOKEN_BOT}/sendAudio"
DIR_PROJECT = os.path.abspath("..")
FOLDER_PATH_AUDIOS = f"{DIR_PROJECT}/common/files-audio/"

def upload_files():
    list_audio = get_files(FOLDER_PATH_AUDIOS)
    print(list_audio)
    if(len(list_audio) >= 1):
        for audio_name in list_audio:
            file = open(os.path.join(FOLDER_PATH_AUDIOS, audio_name), "rb")
            
            episode_name = clear_file_name(audio_name)

            parameters = {
                "chat_id" : CHAT_ID,
                "caption" : f"Novo episódio de Filipe Deschamps Newsletter: {episode_name} !!\nAssine também para receber a Newsletter em seu e-mail: https://filipedeschamps.com.br/newsletter"
            }
            
            files = {
                "audio": file,
            }

            response = requests.post(BASE_URL, data=parameters, files=files)

            print(response.text)
            file.close()
            sleep(10)
    else:
        print("Error: Not exists files")

def get_files(folder_path):
    try:
        files_name = os.listdir(folder_path)
        files_name.remove(".gitKeep")
        return files_name
    except:
        print(f"Error: get files in {folder_path}")

def clear_file_name(file_name):
    try:
        file_name = re.sub(r".mp3", "", file_name)
        # file_name = re.sub(r"\d*-", "", file_name)
        return file_name
    except:
        print("Error: clear file name")

if __name__ == "__main__":
    print("="*20, "publisher-bot", "="*20)
    upload_files()
