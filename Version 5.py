import file_handler
import evaluations

if __name__ == '__main__':
    encoder = file_handler.Encoder()
    decoder = file_handler.Decoder()

    evaluator = evaluations.Evaluator()
    evaluate = evaluator.evaluate

    print("JPG turbo: ")
    evaluate(encoder.turbo_jpeg, quality=50, decoding_func=decoder.turbo_jpeg_decode, numpy_needed=True)
    print("\n")
    print("\n")
    print("JPG:")
    evaluate(encoder.pillowJPEG, 50)
    print("\n")
    print("\n")
    print("WEBP:")
    evaluate(encoder.pillowWEBP, 50)
    print("\n")
    print("\n")
    print("PNG:")
    evaluate(encoder.pillowPNG, 50)










