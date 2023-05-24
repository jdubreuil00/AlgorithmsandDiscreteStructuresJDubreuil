from PIL import Image
import zlib
import numpy as np

def compress_image(image_path):
    # Open the image using PIL and convert to grayscale
    image = Image.open(image_path).convert('L')

    # Convert the grayscale image to a NumPy array
    image_array = np.array(image)

    # Compress the image array using zlib
    compressed_data = zlib.compress(image_array.tobytes())

    # Return the compressed data
    return compressed_data

def decompress_image(compressed_data, output_path, image_size):
    # Decompress the data using zlib
    decompressed_data = zlib.decompress(compressed_data)

    # Convert the decompressed data back to a NumPy array
    image_array = np.frombuffer(decompressed_data, dtype=np.uint8)

    # Reshape the array to the original image size
    image_array = image_array.reshape(image_size)

    # Create a PIL image from the array
    image = Image.fromarray(image_array)

    # Save the decompressed image
    image.save(output_path)

# Path to the original image
original_image_path = 'JaysJPEGTest/pic.jpeg'

# Compress the image and retrieve the compressed data
compressed_data = compress_image(original_image_path)

# Path to save the decompressed image
output_image_path = 'JaysJPEGTest/newpic.jpeg'

# Get the size of the original image
with Image.open(original_image_path) as image:
    image_size = image.size

# Decompress the data and save the image
decompress_image(compressed_data, output_image_path, image_size)
