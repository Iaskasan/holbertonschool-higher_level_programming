from PIL import Image

# ASCII characters used to build the output text
ASCII_CHARS = "@%#*+=-:. "

# Resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 32]
    return ascii_str

# Convert image to ASCII art
def image_to_ascii(image, new_width=100):
    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)
    
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ""
    
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + "\n"
    
    return ascii_img

# Main function
def main(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file: {e}")
        return
    
    ascii_art = image_to_ascii(image, new_width)
    print(ascii_art)

    # Save the ASCII art to a text file
    output_file = "ascii_image.txt"
    try:
        with open(output_file, "w") as f:
            f.write(ascii_art)
        print(f"ASCII art written to {output_file}")
    except Exception as e:
        print(f"Unable to save ASCII art to file: {e}")

# Run the main function
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python png_to_ascii.py <image_path>")
    else:
        image_path = sys.argv[1]
        main(image_path)
