from PIL import Image

def encrypt_image(input_path, output_path, key=None):
    """
    Encrypt the image by swapping the red and blue channels.
    The 'key' determines whether to swap channels (just for consistency).
    """
    # Open the input image
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Swap the red and blue channels
            encrypted_pixel = (b, g, r)  # Swap red and blue channels
            pixels[i, j] = encrypted_pixel

    # Save the encrypted image
    img.save(output_path)
    print("Image encrypted successfully!")


def decrypt_image(input_path, output_path, key=None):
    """
    Decrypt the image by swapping the red and blue channels back.
    The 'key' determines whether to swap channels (just for consistency).
    """
    # Open the encrypted image
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Swap the red and blue channels back
            decrypted_pixel = (b, g, r)  # Swap red and blue channels back
            pixels[i, j] = decrypted_pixel

    # Save the decrypted image
    img.save(output_path)
    print("Image decrypted successfully!")


# Image paths
input_image = r"/home/rohith/Downloads/image.jpeg"
encrypted_image = r"encrypted_image.jpg"
decrypted_image = r"decrypted_image.jpg"

# Encrypt and decrypt the image
encrypt_image(input_image, encrypted_image)
decrypt_image(encrypted_image, decrypted_image)

