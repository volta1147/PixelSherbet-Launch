import os
import sys
import subprocess

resp = ""
repo = "https://github.com/volta1147/MetroVoltBot.git"

def settings_dir(dirs : str):
    return os.path.relpath(os.path.abspath(dirs))

def channel(username="volta1147"):
    channel_file = open("Settings\\Channel.txt")
    channel_name = channel_file.read()
    channel_file.close()
    return f"https://github.com/{username}/{channel_name}Bot.git"

def settings():
    set_dir   = "Settings"
    set_level = 0
    while True:
        set_resp = input()

        if set_level < 0:
            set_dir   = "Settings"
            set_level = 0
        if set_resp == "S!dir":
            print(settings_dir(set_dir))
        if set_level == 0 and set_resp == "Security":
            if input("Are you sure? \"Y\" for edit security settings. : ") != "Y":
                continue
        pass

def cmd():
    global resp
    global repo

    repo = channel()

    while True:
        resp = input("SR >>> ")
        if resp == "install":
            botname = input("Bot Name : ")
            os.system(f"git clone {repo} bot\\{botname}")
            SecList = os.listdir("Settings\\Security")
            for i in SecList:
                if i != "SecurityFiles.txt":
                    os.system(f"copy Settings\\Security\\{i} Bot\\{botname}\\res\\security\\{i}")
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
        if resp == "settings":
            settings()
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
