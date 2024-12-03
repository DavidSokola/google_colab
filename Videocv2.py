import cv2
import sys
import logging
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG)

video_path = '/home/david/CODE/Video/test.mov'
logging.debug(f"Checking if video file exists at: {video_path}")

# Check if the video file exists
if not os.path.exists(video_path):
    logging.error(f"Video file does not exist at: {video_path}")
    sys.exit(-1)

# Attempt to open the video file
videoCapture = cv2.VideoCapture(video_path)

if not videoCapture.isOpened():
    logging.error("Cannot open video file")
    sys.exit(-1)

logging.debug("Video file opened successfully")

i = 0
j = 0
while True:
    success, frame = videoCapture.read()
    if success:
        logging.debug(f"Read frame {i}")
        cv2.imshow('Display', frame)
        i += 1
        if i % 10 == 0:
            j += 1
            img_path = f'/home/david/CODE/IMG/img_{j:04d}.jpg'
            cv2.imwrite(img_path, frame)
            logging.debug(f"Saved frame {i} as {img_path}")

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            logging.debug("Exit key pressed")
            cv2.destroyAllWindows()
            break
    else:
        logging.debug("No more frames to read or error reading frame")
        break