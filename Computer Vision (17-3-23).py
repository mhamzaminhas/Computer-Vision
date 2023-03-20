#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2


# In[8]:


# input image in grayscale
img = cv2.imread(r"C:\Users\Minhas\Downloads\hamza.jpg", 0)


# Apply thresholding to segment foreground text from background
threshold_value = 150
max_value = 255
ret, thresh = cv2.threshold(img, threshold_value, max_value, cv2.THRESH_BINARY)

# Preprocess the image using morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Apply a filter to smooth the image
filtered = cv2.medianBlur(morph, 3)

# Add text to the image
font = cv2.FONT_HERSHEY_SIMPLEX
text = "python developer"
color = (250, 250, 250)
thickness = 2
size = cv2.getTextSize(text, font, 1, thickness)[0]
x = int((img.shape[1] - size[0]) / 2)
y = int((img.shape[0] + size[1]) / 2)
cv2.putText(filtered, text, (x, y), font, 1, color, thickness, cv2.LINE_AA)

# Save the output image
cv2.imwrite("output_image.png", filtered)
cv2.namedWindow('hamza',cv2.WINDOW_NORMAL)
cv2.imshow('hamza',filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




