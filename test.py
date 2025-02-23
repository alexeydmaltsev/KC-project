from PIL import Image
import time
import os
import cv2
from turbojpeg import TurboJPEG, TJPF_GRAY, TJSAMP_GRAY, TJFLAG_PROGRESSIVE, TJFLAG_FASTUPSAMPLE, TJFLAG_FASTDCT



if __name__ == "__main__":
    jpeg = TurboJPEG("C:\libjpeg-turbo-gcc64\\bin\libturbojpeg.dll")
    imgs = []
    t1 = time.perf_counter()
    for image in os.listdir("image library"):
        in_file = open(f"image library/{image}", 'rb')
        bgr_array = jpeg.decode(in_file.read())
        imgs.append(bgr_array)
        in_file.close()
    print(time.perf_counter() - t1)
    t2 = time.perf_counter()
    for img in imgs:
        cv2.imshow('bgr_array', img)

    print(time.perf_counter() - t2)

