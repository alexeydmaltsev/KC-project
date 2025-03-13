from PIL import Image
from turbojpeg import TurboJPEG, TJFLAG_FASTUPSAMPLE, TJFLAG_FASTDCT
import pillow_avif
class Decoder:
    def __init__(self):
        self.jpeg = TurboJPEG("C:\libjpeg-turbo-gcc64\\bin\libturbojpeg.dll")
    def default_decode(self, image):
        with Image.open(image) as img_compressed:
            img_compressed = img_compressed.convert("RGB")
            img_compressed.save(f'bitmap {image}', "BMP")  # saves image as a bitmap
    def turbo_jpeg_decode(self, image):
        in_file = open(image, 'rb')
        np_arr = self.jpeg.decode(in_file.read())
        in_file.close()
        return np_arr
    def turbo_jpeg_decode_fast(self, image):
        in_file = open(image, 'rb')
        np_arr = self.jpeg.decode(in_file.read(), flags=TJFLAG_FASTUPSAMPLE|TJFLAG_FASTDCT)
        in_file.close()
        return np_arr
class Encoder:
    def __init__(self):
        self.jpeg = TurboJPEG("C:\libjpeg-turbo-gcc64\\bin\libturbojpeg.dll")
    def turbo_jpeg(self, input_file, output_file, quality=85):
        out_file = open(output_file + ".jpg", 'wb')
        out_file.write(self.jpeg.encode(input_file, quality=quality))
        out_file.close()
    def pillowJPEG(self, input_file, output_file, quality=85):
        with Image.open(input_file) as img:
            img.save(output_file + ".jpg", "JPEG", quality=quality, optimise=True)
    def pillowWEBP(self, input_file, output_file, quality=85):
        with Image.open(input_file) as img:
            img.save(output_file + ".webp", "WEBP", quality=quality, optimise=True)

    def pillowPNG(self, input_file, output_file, quality=85):
        with Image.open(input_file) as img:
            img.save(output_file + ".png", "PNG", quality=quality, optimise=True)

    def pillowAVIF(self, input_file, output_file, quality = 85):
        with Image.open(input_file) as img:
            img.save(output_file + ".avif", quality=quality)