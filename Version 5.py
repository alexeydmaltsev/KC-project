import file_handler
import evaluations

if __name__ == '__main__':
    encoder = file_handler.Encoder()
    decoder = file_handler.Decoder()

    evaluator = evaluations.Evaluator()
    evaluate = evaluator.evaluate

    print("the information comes in this format: ")
    print("compression algorithm")
    print("quality")
    print("average decode latency")
    print("average compression latency")
    print("average percentage reduction")
    print("average MSE")
    print("average SSIM")

    evaluate(encoder.pillowPNG, 10, ".png")

    # for i in range(20, 120, 20):
    #     print("\n")
    #     print("pillow png")
    #     print(i)
    #     evaluate(encoder.pillowPNG(), i, ".png")

    # evaluator.evaluate_decode(decoder.turbo_jpeg_decode, True)
    # evaluate(encoder.turbo_jpeg, quality=50, decoding_func=decoder.turbo_jpeg_decode, numpy_needed=True)
    # print("\n")
    # print("\n")
    # evaluate(encoder.pillowJPEG, 100)
    # print("\n")
    # print("\n")
    # evaluate(encoder.pillowWEBP, 50)
    # print("\n")
    # print("\n")
    # evaluate(encoder.pillowPNG, 50)










