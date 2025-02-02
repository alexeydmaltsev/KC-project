import SSIM_evaluation_1

if __name__ == '__main__':
    from PIL import Image
    import time
    import os


    def evaluate(compression_func, quality):
        start_time = time.time()
        total_size = 0
        number_of_images = 0
        total_reduction = 0
        total_encode = 0
        total_decode = 0
        total_SSIM = 0
        total_MSE = 0

        for image in os.listdir("image library"):
            number_of_images += 1
            with Image.open("image library/" + image) as img:
                # print(f'{image}:')

                decode_timer = time.perf_counter()  # decoding timer
                img = img.convert("RGB")
                img.save(f'bitmap {image}', "BMP")  # saves image as a bitmap
                total_decode += (time.perf_counter() - decode_timer)  # time to convert it to a bitmap
                bmp_size = os.path.getsize(f"bitmap {image}")

                # optional information about individual images
                # print(f'size of bitmap image: {round((bmp_size) / 1024, 1)} KB')
                # print(f'time to decode image: {round(time.perf_counter() - decode_timer, 5)}s')

                encode_timer = time.perf_counter()  # encoding timer
                compression_func(f'bitmap {image}', f'compressed {image}', quality) # quality used here - can be varied
                total_encode += (time.perf_counter() - encode_timer)
                total_size += os.path.getsize(f"compressed {image}") / 1024
                total_reduction += (bmp_size - os.path.getsize(f"compressed {image}"))/bmp_size

                MSE, SSIM = SSIM_evaluation_1.main(f"bitmap {image}", f"compressed {image}")
                total_MSE += MSE
                total_SSIM += SSIM

                # optional information about individual images
                # print(f'time to encode image: {round(time.perf_counter() - encode_timer, 5)}s')
                # print(f'size of final compressed image, reduced quality: {round(os.path.getsize(f"compressed {image}") / 1024, 1)} KB')
                # print("\n")

                os.remove(f'compressed {image}')
                os.remove(f'bitmap {image}')

        print(f"done, total time was: {round(time.time() - start_time, 3)}s")
        print(f'{number_of_images} images were compressed')
        print(f'average decode time was {round(total_decode / number_of_images * 1000, 3)}ms')
        print(f"average encode time was {round(total_encode / number_of_images * 1000, 3)}ms")
        print("\n")
        print(f'average file size was {round(total_size/number_of_images, 4)} KB')
        print(f'average file size reduction was {round(total_reduction * 100/number_of_images, 3)}%')
        print("\n")
        print(f'average MSE was {round(total_MSE/number_of_images, 4)}')
        print(f"average SSIM was {round(total_SSIM/number_of_images, 4)}")


    def compress_image(input_file, output_file, quality=85):
        with Image.open(input_file) as img:
            img.save(output_file, "JPEG", quality=quality)


    evaluate(compress_image, 30)
