import time
import subprocess

while True:
    print("Startar finn_discord_bot.py ...")
    p = subprocess.Popen(["python", "finn_discord_bot.py"])
    p.wait()
    print("finn_discord_bot.py avslutades, startar om om 60 sekunder...")
    time.sleep(60)

