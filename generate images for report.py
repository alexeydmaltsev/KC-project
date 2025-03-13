import SSIM_evaluation_1

if __name__ == '__main__':
    from PIL import Image
    import os
    from turbojpeg import TurboJPEG
    import SSIM_evaluation_1
    import file_handler


    def compress_image(input_file, output_file, quality=85):
        with Image.open(input_file) as img:
            img.save(output_file, "JPEG", quality=quality)


    # evaluate(compress_image, 30)


    images = ["boat", "mountain", "snowy path", "desert tree", "black and white cathedral"]
    encoder = file_handler.Encoder()
    jpeg = TurboJPEG("C:\libjpeg-turbo-gcc64\\bin\libturbojpeg.dll")
    for image in images:
        with Image.open("image library/" + image + ".jpg") as img:
            print("\n")
            print(image + ":")
            img = img.convert("RGB")
            img.save(f'{image} bitmap.bmp', "BMP")
            print(f'{round(os.path.getsize(f"{image} bitmap.bmp") / 1024, 1)}')
            in_file = open(f"image library/{image}.jpg", 'rb')
            np_arr = jpeg.decode(in_file.read())
            in_file.close()

            for i in range(1, 6):


                encoder.turbo_jpeg(np_arr, f'{image} turbo jpeg quality {i}', 20*i)


                MSE, SSIM = SSIM_evaluation_1.main(f'{image} bitmap.bmp', f'{image} turbo jpeg quality {i}.jpg')
                print(round(MSE, 5))
                print(round(SSIM,5))
                print(f'size for quality {i}: {round(os.path.getsize(f"{image} turbo jpeg quality {i}.jpg") / 1024, 2)}')
                print("\n")
            os.remove(f'{image} bitmap.bmp')

