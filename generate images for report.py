import SSIM_evaluation_1

if __name__ == '__main__':
    from PIL import Image
    import os


    def compress_image(input_file, output_file, quality=85):
        with Image.open(input_file) as img:
            img.save(output_file, "JPEG", quality=quality)


    # evaluate(compress_image, 30)


    images = ["boat", "mountain", "snowy path", "desert tree", "black and white cathedral"]
    for image in images:
        with Image.open("image library/" + image + ".jpg") as img:
            print("\n")
            print(image + ":")
            img = img.convert("RGB")
            img.save(f'{image} bitmap.bmp', "BMP")
            print(f'bitmap file size: {round(os.path.getsize(f"{image} bitmap.bmp") / 1024, 1)}')
            for i in range(1, 6):
                compress_image(f'{image} bitmap.bmp', f'{image} jpeg quality {i}.jpg', 15*i)
                SSIM_evaluation_1.main(f'{image} bitmap.bmp', f'{image} jpeg quality {i}.jpg')
                print(f'size for quality {i}: {round(os.path.getsize(f"{image} jpeg quality {i}.jpg") / 1024, 1)}')
                print("\n")


