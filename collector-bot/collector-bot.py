from dotenv import load_dotenv
import imaplib
import email
import re
import os

load_dotenv()

# account credentials
SERVER = "imap.gmail.com"
EMAIL = str(os.environ['EMAIL_USER'])
PASSWORD = str(os.environ['EMAIL_PASSWORD'])
DIR_PROJECT = os.path.abspath("..")

def decode_email_string(string):
    try:
        byte = string.get_payload(decode=True)
        charset = string.get_content_charset("iso-8859-1")
        chars = byte.decode(charset, "replace")
        return chars
    except:
        print("Error: decode string")

def clear_content(string):
    try:
        URLless_string = string
        URLless_string = re.sub(r"http\S+", "", str(URLless_string)) # clear link
        URLless_string = re.sub(r"Link\s(\w+\s|)\(..\)", "", str(URLless_string)) # clear patrocined link
        URLless_string = re.sub(r"\((..\)|.\))", "", str(URLless_string)) # clear blank parentheses
        URLless_string = re.sub(r"Cancelar inscrição[\s\S]*", "", str(URLless_string)) # clear rest text
        URLless_string = re.sub(r"Rua Antônio da Veiga, 495, Blumenau, SC, 89012-500", "", str(URLless_string)); # clear address 
        URLless_string = re.sub(r".\n", " ", str(URLless_string)) # replace new line to white space
        return URLless_string
    except:
        print("Error: clear_content")

def write_file(string, name):
    try:
        file = open(f"{DIR_PROJECT}/common/scripts-txt/{str(name)}.txt", "w+")
        file.write(string)
        file.close()
    except:
        print("Error: write file")

def read_mail():
    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select("NEWSLETTER")

    status, data = mail.search(None, "UNSEEN")

    mail_ids = []

    for block in data:
        mail_ids += block.split()
        
    for indice,id in enumerate(mail_ids):
        status, data = mail.fetch(id, "(RFC822)")

        for response_part in data:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])
                date = str(message["date"])
                date = re.sub(r"\s\d{2}:\d{2}:\d{2} \+\d{4}.\(\w{3}\)", "", date)
                name_file = f"{date}"

                if message.is_multipart():
                    mail_content = ""

                    for part in message.get_payload():

                        if part.get_content_type() == "text/plain":
                            mail_content += decode_email_string(part)
                
                else:
                    mail_content = decode_email_string(message)
            mail_content = clear_content(mail_content)
            write_file(mail_content, name_file)


if __name__ == "__main__":
    print("="*20, "collector-bot", "="*20)
    read_mail()
