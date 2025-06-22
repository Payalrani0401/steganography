#decode (extract hidden data)

from PIL import Image

def decode_image(stego_path):
   img = Image.open(stego_path)
   pixels = list(img.getdata())
   binary_data = ''

   for pixel in pixels:
        for channel in pixel[:3]:
            binary_data += str(channel & 1)

   chars = [chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)]
   message = ''.join(chars)
   return message.split("#####")[0]

print("Hidden Message:", decode_image("stego_image.png"))
