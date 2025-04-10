import time
from datetime import datetime
import os

log_file_path = r"C:\Users\user\AppData\LocalLow\Northwood\SCPSL\Player.log"
session_path = r"C:\Users\user\AppData\LocalLow\Northwood\SCPSL"


def follow_log_file():
    with open(log_file_path, 'r', encoding='utf-8') as log_file, \
            open(fr"{session_path}\session.log", 'a', encoding='utf-8') as session_log:

        # write old logs
        for line in log_file:
            print(line.strip())
            session_log.write(line.strip() + "\n")
        log_file.seek(0, 2)

        # recording new logs
        print(f"[{datetime.now()}] [INFO] START RECORDING")
        session_log.write(f"[{datetime.now()}] [INFO] START RECORDING\n")
        while True:
            line = log_file.readline()

            if not line:
                time.sleep(0.1)
                continue

            line = line.strip()

            current_time = datetime.now()

            print(f"[{current_time}] {line}")
            session_log.write(f"[{current_time}] {line}\n")

            if line == "--End of Log--":
                print("[INFO] GAME CLOSED")
                session_log.write("[INFO] GAME CLOSED\n")


if __name__ == "__main__":
    try:
        follow_log_file()
    except KeyboardInterrupt:
        current_time = datetime.now()
        print(f"[{current_time}] [INFO] RECORDING FINISHED")
        with open(f"{session_path}\session.log", 'a', encoding='utf-8') as session_log:
            session_log.write(f"[{current_time}] [INFO] RECORDING FINISHED")
            session_log.close()
            os.rename(fr"{session_path}\session.log",
                      fr"{session_path}\{current_time.strftime("%Y-%m-%d=%H-%M-%S")}.log")
        pass
