from PIL import Image

def bin_to_text(binary_data):
    binary_data = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return ''.join(chr(int(byte, 2)) for byte in binary_data)

def extract_message(image_path):
    img = Image.open(image_path)
    data = img.getdata()
    binary_data = ''

    for pixel in data:
        for i in range(3):  # Vérifier les 3 canaux des pixels
            binary_data += str(pixel[i] & 1)

    return bin_to_text(binary_data.split('1111111111111110')[0])  # Utilisation du délimiteur

print(extract_message('output_image.png'))
