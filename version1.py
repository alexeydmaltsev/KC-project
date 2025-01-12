
if __name__ == '__main__':
    from PIL import Image
    import time
    import os

    def compress_image(input_file, output_file, quality=85):
        with Image.open(input_file) as img:
            img.save(output_file, "JPEG", quality=quality)


    input_file = "Daniel.jpg"
    c=1
    for i in range(1, 101, 11):
        t1 = time.time()
        file_name = f'test{c}.jpg'
        compress_image(input_file, file_name, quality=i)
        c += 1
        t2 = time.time()
        print(f' {c}: time taken was {t2-t1}, size is {round(os.path.getsize(file_name)/1024, 1)} KB')