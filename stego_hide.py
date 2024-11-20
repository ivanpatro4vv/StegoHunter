from PIL import Image
import binascii

def text_to_bin(message):
    return ''.join(format(ord(i), '08b') for i in message)

def hide_message(image_path, message, output_image_path):
    img = Image.open(image_path)
    binary_message = text_to_bin(message) + '1111111111111110'  # ajout d'un delimiter
    data = img.getdata()

    new_data = []
    message_index = 0
    for pixel in data:
        if message_index < len(binary_message):
            pixel = list(pixel)
            for i in range(3):  # Modifier les 3 premiers canaux de chaque pixel
                if message_index < len(binary_message):
                    pixel[i] = pixel[i] & ~1 | int(binary_message[message_index])
                    message_index += 1
            new_data.append(tuple(pixel))
        else:
            new_data.append(pixel)
    
    img.putdata(new_data)
    img.save(output_image_path)

message = "This is a secret message!"
hide_message('input_image.png', message, 'output_image.png')
