from datetime import datetime
import os
def markAttendence(name):
    today = datetime.today()
    dtString = today.strftime("%d-%m-%Y")
    file_name = f"{dtString}.csv"

    if not os.path.isfile(file_name):
        with open(file_name, "w") as f:
            f.write("Name,Time")

    with open(f"{dtString}.csv", "r+") as f:
        attendance = f.readlines()
        names = set()
        for line in attendance:
            entry = line.split(",")
            names.add(entry[0])

        if name not in names:
            now = datetime.now()
            dtString = now.strftime("%H:%M:%S")
            f.writelines(f"\n{name},{dtString}")