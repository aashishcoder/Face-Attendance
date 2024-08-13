import datetime

def mark_attendance(name):
    with open("attendance.csv", "a") as f:
        now = datetime.datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{name},{dt_string}\n")

# Call mark_attendance(name) inside the recognize_faces function whenever a match is found.