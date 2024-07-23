import cv2
import time
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from the .env file

stream_url = os.getenv('STREAM_URL')
snapshot_interval = 15 * 60  # 15 minutes

while True:
    cap = cv2.VideoCapture(stream_url)
    if cap.isOpened():
        ret, frame = cap.read()
        timestamp = int(time.time())
        output_filename = f"snapshots/snapshot_{timestamp}.jpg"
        cv2.imwrite(output_filename, frame)
        print(f"Snapshot saved as {output_filename}")
    else:
        print("Failed to open stream")

    cap.release()
    time.sleep(snapshot_interval)

