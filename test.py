from PIL import Image
import time
import os
import cv2
from turbojpeg import TurboJPEG, TJPF_GRAY, TJSAMP_GRAY, TJFLAG_PROGRESSIVE, TJFLAG_FASTUPSAMPLE, TJFLAG_FASTDCT



if __name__ == "__main__":
    image_path = "boat jpeg quality 1.jpg.jpg"
    img = cv2.imread(image_path)
    if img is None:
        print("OH NO")

