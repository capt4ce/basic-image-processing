import cv2

# reading image
img = cv2.imread('./img/Q450-quadcopter-kopen.jpg')

cv2.imshow('basic' ,img)
cv2.waitKey(0)
cv2.destroyAllWindows()