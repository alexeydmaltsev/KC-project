import file_handler
import time
import os
from PIL import Image
from turbojpeg import TurboJPEG
import SSIM_evaluation_1
import printing_helper

class Evaluator:
    def __init__(self):
        self.jpeg = TurboJPEG("C:\libjpeg-turbo-gcc64\\bin\libturbojpeg.dll")

    def evaluate(self, compression_func, quality, decoding_func=None, numpy_needed=False):
        decoder = file_handler.Decoder()
        total_size = 0
        number_of_images = 0
        total_reduction = 0
        total_encode = 0
        total_decode = 0
        total_SSIM = 0
        total_MSE = 0

        for image in os.listdir("image library"):
            number_of_images += 1

            with Image.open(f"image library/{image}") as img:
                img = img.convert("RGB")
                img.save(f'bitmap {image}', "BMP")  # saves image as a bitmap
                bmp_size = os.path.getsize(f"bitmap {image}")

                if numpy_needed:  # some compression methods require an input of a numpy array and do not take bitmaps
                    in_file = open(f"image library/{image}", 'rb')
                    np_arr = self.jpeg.decode(in_file.read())
                    in_file.close()

                encode_timer = time.perf_counter()  # encoding timer
                if not numpy_needed:
                    compression_func(f'bitmap {image}', f'compressed {image}', quality) # quality used here - can be varied
                else:
                    compression_func(np_arr, f'compressed {image}', quality)
                total_encode += (time.perf_counter() - encode_timer)
                total_size += os.path.getsize(f"compressed {image}") / 1024
                total_reduction += (bmp_size - os.path.getsize(f"compressed {image}"))/bmp_size

                MSE, SSIM = SSIM_evaluation_1.main(f"bitmap {image}", f"compressed {image}")
                total_MSE += MSE
                total_SSIM += SSIM

                decode_timer = time.perf_counter()  # decoding timer
                if decoding_func is None:
                    decoder.default_decode(f'compressed {image}')
                else:
                    decoding_func(f'compressed {image}')
                total_decode += (time.perf_counter() - decode_timer)  # time to convert it to a bitmap

                os.remove(f'compressed {image}')
                os.remove(f'bitmap {image}')

        printer = printing_helper.Printer()
        printer.print_normal_stats(number_of_images, total_decode, total_encode, total_size, total_reduction, total_MSE, total_SSIM)

    def evaluate_decode(self, decoding_func):
        number_of_images = 0
        for image in os.listdir("image library"):
            number_of_images += 1
            decoding_func(f"image library/{image}")
