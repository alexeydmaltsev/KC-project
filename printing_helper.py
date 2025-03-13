class Printer:
    def __init__(self):
        pass
    def print_normal_stats(self, number_of_images, total_decode, total_encode, total_size, total_reduction, total_MSE, total_SSIM, name):
        # print(f"done encoding using {name}")
        # print(f'{number_of_images} images were compressed')
        # print(f'average decode time was {round(total_decode / number_of_images * 1000, 3)}ms')
        # print(f"average encode time was {round(total_encode / number_of_images * 1000, 3)}ms")
        # print("\n")
        # print(f'average file size was {round(total_size / number_of_images, 4)} KB')
        # print(f'average file size reduction was {round(total_reduction * 100 / number_of_images, 3)}%')
        # print("\n")
        # print(f'average MSE was {round(total_MSE / number_of_images, 4)}')
        # print(f"average SSIM was {round(total_SSIM / number_of_images, 4)}")

        print(round(total_decode / number_of_images * 1000, 3))
        print(round(total_encode / number_of_images * 1000, 3))
        print(round(total_reduction * 100 / number_of_images, 3))
        print(round(total_MSE / number_of_images, 4))
        print(round(total_SSIM / number_of_images, 4))

    def print_decode_stats(self, number_of_images, total_time, total_MSE, total_SSIM, name):
        print(f"Done decoding using {name}")
        print(f"{number_of_images} were decoded")
        print(f"average decode time was {round((total_time/number_of_images) * 1000, 3)}ms")
        print(f'average MSE was {round(total_MSE / number_of_images, 4)}')
        print(f"average SSIM was {round(total_SSIM / number_of_images, 4)}")