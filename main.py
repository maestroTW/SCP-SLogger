import time
from datetime import datetime
from pathlib import Path

log_file_path = r"C:\Users\user\AppData\LocalLow\Northwood\SCPSL\Player.log"

def follow_log_file():
    with open(log_file_path, 'r', encoding='utf-8') as log_file:

        for line in log_file:
            print(line.strip())


        log_file.seek(0, 2)


        print("[INFO] START RECORDING")

        while True:
            line = log_file.readline()

            if not line:
                time.sleep(0.1)
                continue

            # delet spaces
            line = line.strip()

            current_time = datetime.now()


            print(f"[{current_time}] {line}")

            #if line == "--End of Log--":



if __name__ == "__main__":
    try:
        follow_log_file()
    except KeyboardInterrupt:
        pass