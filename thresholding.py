import cv2

# reading image
img = cv2.imread('./img/bookpage.jpg')

# img = cv2.medianBlur(img,5)
# th = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2,threshold_binary = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
threshold_gaussian = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow('basic' ,img)
cv2.imshow('greyscale' ,grayscaled)
cv2.imshow('threshold binary' ,threshold_binary)
cv2.imshow('threshold gaussian' ,threshold_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()