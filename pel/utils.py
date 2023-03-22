import cv2
import numpy as np
import os
from . import huffman

def messageToBinary(message):
    if type(message) == str:
        return ''.join([format(ord(i), "08b") for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format(i, "08b") for i in message]
    elif type(message) == int or type(message) == np.unit8:
        return format(message, "08b")
    else:
         raise TypeError("Format Not Supported")
    
def hideData(image, secret_message):
    # n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    # if len(secret_message) > n_bytes:
    #     raise ValueError(
    #         "Error encountered insufficient bytes, need bigger image or less data !!")

    secret_message += "#####"  # you can use any string as the delimeter

    data_index = 0
    # convert input data to binary format using messageToBinary() fucntion
    binary_secret_msg = messageToBinary(secret_message)

    # Find the length of data that needs to be hidden
    data_len = len(binary_secret_msg)
    for values in image:
        for pixel in values:
            # convert RGB values to binary format
            r, g, b = messageToBinary(pixel)
            # modify the least significant bit only if there is still data to store
            if data_index < data_len:
                # hide the data into least significant bit of red pixel
                pixel[0] = int(r[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # hide the data into least significant bit of green pixel
                pixel[1] = int(g[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            if data_index < data_len:
                # hide the data into least significant bit of  blue pixel
                pixel[2] = int(b[:-1] + binary_secret_msg[data_index], 2)
                data_index += 1
            # if data is encoded, just break out of the loop
            if data_index >= data_len:
                break

    return image

def showData(image):

    binary_data = ""
    for values in image:
        for pixel in values:
            # convert the red,green and blue values into binary format
            r, g, b = messageToBinary(pixel)
            # extracting data from the least significant bit of red pixel
            binary_data += r[-1]
            # extracting data from the least significant bit of red pixel
            binary_data += g[-1]
            # extracting data from the least significant bit of red pixel
            binary_data += b[-1]
    # split by 8-bits
    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
    # convert from bits to characters
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        # check if we have reached the delimeter which is "#####"
        if decoded_data[-5:] == "#####":
            break
    # print(decoded_data)
    # remove the delimeter to show the original hidden message
    return decoded_data[:-5]

def decode_text(image):
    # read the image that contains the hidden image
    #image = cv2.imread(image_name)  # read the image using cv2.imread()
    # cv2.imshow('image',resized_image)  # display the Steganographed image

    text = showData(image)
    return text
