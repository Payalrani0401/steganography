#encoding phase(hiding of data/ hide text in image)
from PIL import Image




img = Image.new('RGB', (300, 300), color='white')  # 300x300 white image
img.save("original.png")


def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    binary_message = ''.join(format(ord(c), '08b') for c in message + '#####')  # '#####' as a delimiter
    pixels = list(img.getdata())
    
    new_pixels = []
    msg_index = 0

    for pixel in pixels:
        new_pixel = []
        for channel in pixel[:3]:  # R, G, B
            if msg_index < len(binary_message):
                new_channel = (channel & ~1) | int(binary_message[msg_index])
                msg_index += 1
            else:
                new_channel = channel
            new_pixel.append(new_channel)
        if len(pixel) == 4:  # preserve alpha
            new_pixel.append(pixel[3])
        new_pixels.append(tuple(new_pixel))

    img.putdata(new_pixels)
    img.save(output_path)
    print("Data hidden successfully!")

encode_image("original.png", "Secret Message", "stego_image.png")

