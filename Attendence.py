from datetime import datetime
def markAttendence(name):
    with open("Attendence.csv", "r+") as f:
        attendence = f.readlines()
        names = set()
        for line in attendence:
            entry = line.split(",")
            names.add(entry[0])

        if name not in names:
            now = datetime.now()
            dtString = now.strftime("%H:%M:%S")
            f.writelines(f"\n{name},{dtString}")