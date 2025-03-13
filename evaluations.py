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

    def evaluate(self, compression_func, quality, extension, decoding_func=None, numpy_needed=False):
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
                image = image[:-4]
                img = img.convert("RGB")
                img.save(f'bitmap {image}.bmp', "BMP")  # saves image as a bitmap
                bmp_size = os.path.getsize(f"bitmap {image}.bmp")

                if numpy_needed:  # some compression methods require an input of a numpy array and do not take bitmaps
                    in_file = open(f"image library/{image}.jpg", 'rb')
                    np_arr = self.jpeg.decode(in_file.read())
                    in_file.close()

                encode_timer = time.perf_counter()  # encoding timer
                if not numpy_needed:
                    compression_func(f'bitmap {image}.bmp', f'compressed {image}', quality) # quality used here - can be varied
                else:
                    compression_func(np_arr, f'compressed {image}', quality)

                total_encode += (time.perf_counter() - encode_timer)
                total_size += os.path.getsize(f"compressed {image}{extension}") / 1024
                total_reduction += (bmp_size - os.path.getsize(f"compressed {image}{extension}"))/bmp_size

                if extension == ".avif":
                    with Image.open(f"compressed {image}{extension}") as img:
                        img.save("temp.png", format="PNG")
                    MSE, SSIM = SSIM_evaluation_1.main(f"bitmap {image}.bmp", "temp.png")
                    os.remove("temp.png")
                else:
                    MSE, SSIM = SSIM_evaluation_1.main(f"bitmap {image}.bmp", f"compressed {image}{extension}")
                total_MSE += MSE
                total_SSIM += SSIM

                decode_timer = time.perf_counter()  # decoding timer
                if decoding_func is None:
                    decoder.default_decode(f'compressed {image}{extension}')
                else:
                    decoding_func(f'compressed {image}')
                total_decode += (time.perf_counter() - decode_timer)  # time to convert it to a bitmap

                os.remove(f'compressed {image}{extension}')
                os.remove(f'bitmap {image}.bmp')
                os.remove(f'bitmap compressed {image}{extension}')

        printer = printing_helper.Printer()
        printer.print_normal_stats(number_of_images, total_decode, total_encode, total_size, total_reduction, total_MSE, total_SSIM, compression_func.__name__)

    def evaluate_decode(self, decoding_func, is_numpy = False):
        number_of_images = 0
        total_MSE = 0
        total_SSIM = 0
        total_time = 0
        for image in os.listdir("image library"):
            number_of_images += 1

            if not is_numpy:
                decode_timer = time.perf_counter()
                decoding_func(f"image library/{image}")
                total_time += time.perf_counter() - decode_timer

                MSE, SSIM = SSIM_evaluation_1.main(f"bitmap {image}", f"image library/{image}")
                total_MSE += MSE
                total_SSIM += SSIM

                os.remove(f"bitmap {image}")


            if is_numpy:
                decode_timer = time.perf_counter()
                np_arr = decoding_func(f"image library/{image}")
                total_time += time.perf_counter() - decode_timer

                np_arr = np_arr[..., ::-1]
                data = Image.fromarray(np_arr, "RGB")
                data.save(f"bitmap {image[:-3] + 'png'}", "PNG", quality = 100)
                print(image)

                MSE, SSIM = SSIM_evaluation_1.main(f"bitmap {image[:-3] + 'png'}", f"image library/{image}")
                total_MSE += MSE
                total_SSIM += SSIM

                os.remove(f"bitmap {image[:-3] + 'png'}")



        printer = printing_helper.Printer()
        printer.print_decode_stats(number_of_images=number_of_images, total_time=total_time, total_MSE=total_MSE, total_SSIM=total_SSIM, name=decoding_func.__name__)
