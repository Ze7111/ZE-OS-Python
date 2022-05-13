import os
import json
def apptxtwrite():
    filename = 'apps\\apps.json'
    path = "none"
    entry = ""
    start_path = 'apps'
    curly1 = "{"
    curly2 = "}"
    with open("apps\\apps.txt", "w") as file:
        file.write("Manifest Of Installed Programs\n")
        for path,dirs,files in os.walk(start_path):
            for filename in files:
                filewall = os.path.join("apps\\",filename)
                apps = os.path.join("apps\\",filename)
                file.write(apps)
                file.write("\n")