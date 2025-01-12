if __name__ == '__main__':
    from PIL import Image
    import time
    import os

    def compress_image(input_file, output_file, quality=85):
        with Image.open(input_file) as img:
            img.save(output_file, "JPEG", quality=quality)

    x1 = time.time()
    for image in os.listdir("image library"):
        with Image.open("image library/" + image) as img:
            print(f"size of image as jpeg: {round(os.path.getsize('image library/' + image)/1024, 1)} KB")

            t1 = time.perf_counter()
            img = img.convert("RGB")
            img.save(f'bitmap {image}', "BMP")
            print(f'time to decode image: {round(time.perf_counter() - t1, 5)}s')
            print(f'size of bitmap image: {round(os.path.getsize(f"bitmap {image}")/1024, 1)} KB')

            t2 = time.perf_counter()
            compress_image(f'bitmap {image}', f'jpeg {image}', quality=30)
            print(f'time to encode image: {round(time.perf_counter() - t2, 5)}s')
            print(f'size of final jpeg image, reduced quality: {round(os.path.getsize(f"jpeg {image}")/1024, 1)} KB')
            print("\n")

    print("done, total time was: ", end="")
    print(time.time()-x1)
