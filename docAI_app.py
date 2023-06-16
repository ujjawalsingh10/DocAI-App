# import streamlit as st

# header = st.container()

# with header:
#     st.title("Title not decided yet")
#     st.text('Read pdf and perform ocr')

from PIL import Image
import easyocr
import cv2 as cv

img = cv.imread('invoice.png')

##OCR reader
read = easyocr.Reader(['en'])

## Performing OCR on image
ocr_image = read.readtext(img)

## Bounding boxes
for detection in ocr_image:
    box, text, score = detection
    x_min, y_min = map(int, box[0])
    x_max, y_max = map(int, box[2])

    ## Creating Red colored Bounding box
    cv.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)

print('done')
cv.imwrite('Invoice_OCRd.png', img)
        