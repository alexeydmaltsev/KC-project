# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    import subprocess


    def compress_image(input_file, output_file):
        """
        Compress an image using libjpeg-turbo.
        Args:
        input_file (str): Path to the input image file.
        output_file (str): Path to the output compressed image file.
        """


        # Define the libjpeg-turbo executable command
        cmd = ["jpegtran", "-copy", "none", "-optimize", "-outfile", output_file, input_file]
        # Run the command using subprocess
        try:
            subprocess.run(cmd, check=True)
            print(f"Image compressed successfully: {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error compressing image: {e}")

        # Example usage
    input_file = "Daniel.jpg"
    output_file = "test.jpg"
    compress_image(input_file, output_file)