import file_handler
import evaluations

if __name__ == '__main__':
    encoder = file_handler.Encoder()
    decoder = file_handler.Decoder()

    evaluator = evaluations.Evaluator()
    evaluate = evaluator.evaluate

    evaluate(encoder.pillowAVIF, 30, ".avif")

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










