import time
from datetime import datetime
# from pathlib import Path
# import os

log_file_path = r"C:\Users\user\AppData\LocalLow\Northwood\SCPSL\Player.log"
session_path = r"C:\Users\user\AppData\LocalLow\Northwood\SCPSL\session.log"
def follow_log_file():
    with open(log_file_path, 'r', encoding='utf-8') as log_file, \
        open(session_path, 'a', encoding='utf-8') as session_log:

        for line in log_file:
            print(line.strip())
            session_log.write(line.strip())
        log_file.seek(0, 2)

        print("[INFO] START RECORDING")
        session_log.write("[INFO] START RECORDING\n")
        while True:
            line = log_file.readline()

            if not line:
                time.sleep(0.1)
                continue

            line = line.strip()
            current_time = datetime.now()

            print(f"[{current_time}] {line}")
            session_log.write(f"[{current_time}] {line}\n")

            # stop_recording = False
            # if not line and stop_recording:
            #     print("FINISHED RECORDING")
            #     session_log.write("FINISHED RECORDING\n")
            #     session_log.close()
            #     os.rename(session_path, f"session{current_time.strftime('%Y%m%d%H')}")
            #     break
            #
            # if line == "--End of Log--":
            #     print("[INFO] STOPPING")
            #     session_log.write("[INFO] STOPPING\n")
            #     stop_recording = True
            #     time.sleep(5)

if __name__ == "__main__":
    try:
        follow_log_file()
    except KeyboardInterrupt:
        pass