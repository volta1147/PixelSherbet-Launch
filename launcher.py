import os
import sys
import subprocess

resp = ""
repo = "https://github.com/volta1147/ProxieLBot-SE.git"

def cmd():
    global resp
    while True:
        resp = input("SR >>> ")
        if resp == "install":
            botname = input("Bot Name : ")
            os.system(f"git clone {repo} bot\\{botname}")
            SecList = os.listdir("Security")
            for i in SecList:
                if i != "SecurityFiles.txt":
                    os.system(f"copy Security\\{i} Bot\\{botname}\\res\\security\\{i}")
        if resp == "print":
            BotList = os.listdir("Bot")
            BotList.remove(".git")
            print(f"\n".join(BotList))
        if resp == "run":
            botname = input("Bot Name : ")
            try:
                subprocess.run(["python", f"Bot\\{botname}\\main.py"])
            except KeyboardInterrupt:
                print("="*30+" 종료됨 "+"="*30)
        if resp == "quit":
            break

def main():
    try:
        cmd()
    except Exception as err:
        print(err)
    finally:
        if not resp == "quit":
            print("")
            main()

main()