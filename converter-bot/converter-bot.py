from gtts import gTTS
import os
import re

DIR_PROJECT = os.path.abspath("..")
FOLDER_PATH_SCRIPTS = f"{DIR_PROJECT}/common/scripts-txt"
FOLDER_PATH_AUDIOS = f"{DIR_PROJECT}/common/files-audio"
LANG = "pt"
    
def converter_files():
    list_scripts_txt = get_files(FOLDER_PATH_SCRIPTS)

    if(len(list_scripts_txt) >= 1):
    
        for script_name in list_scripts_txt:
            file = open(os.path.join(FOLDER_PATH_SCRIPTS, script_name), "r")
            text = file.read()

            output = gTTS(text=text, lang=LANG, slow=False)
            
            file_name = clear_file_name(script_name)

            output.save(f"{FOLDER_PATH_AUDIOS}/{file_name}.mp3")

            file.close()

    else:
        print("Error: Not exists scripts.")

def get_files(folder_path):
    try:
        files_name = os.listdir(folder_path)
        files_name.remove(".gitKeep")
        return files_name
    except:
        print(f"Error: get files in {folder_path}")

def clear_file_name(file_name):
    try:
        return re.sub(r".txt", "", file_name)
    except:
        print("Error: clear file name")

if __name__ == "__main__":
    print("="*20, "converter-bot", "="*20)
    converter_files()
