# -*- coding: utf-8 -*-
"""
Created on Sun May  2 00:47:23 2021

@author: chari
"""
from PIL import Image
import pytesseract
import cv2
import re

#declare the tesseract exe path
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#load the image
image_to_ocr = cv2.imread('Images/test/sample1.png')

#preprocessing the image

#preprocess step1:convert it into gray
preprocessed_img = cv2.cvtColor(image_to_ocr, cv2.COLOR_BGR2GRAY)

#preprocess step2:do binary and otsu threshold
preprocessed_img = cv2.threshold(preprocessed_img,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#preprocess step3:smooth the image using medianblur
preprocessed_img = cv2.medianBlur(preprocessed_img, 3)

#save the processed image temporarily into the disk
cv2.imwrite('temp_img.jpg',preprocessed_img)

#load the image as a PIL/Pillow image
preprocessed_pil_img = Image.open('temp_img.jpg')

#pass the PIL image to tesseract to do OCR
text_extracted = pytesseract.image_to_string(preprocessed_pil_img)

#print extracted text
text_extracted = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\xff]', '', text_extracted)
print(text_extracted)

#display the original image
cv2.imshow("actualimage",image_to_ocr)


