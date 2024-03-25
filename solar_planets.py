import cv2

img = cv2.imread("solar-system.jpg")



cv2.putText(img, 'Sun', (30, 200), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))

cv2.putText(img, 'Mercury', (120, 240), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255))

cv2.putText(img, 'Venus', (200, 260), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255))

cv2.putText(img, 'Earth', (290, 260), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255))

cv2.putText(img, 'Mars', (380, 260), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255))

cv2.putText(img, 'Jupiter', (580, 380), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255))

cv2.putText(img, 'Saturn', (760, 300), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255))

cv2.putText(img, 'Uranus', (970, 290), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255))

cv2.putText(img, 'Neptune', (1120, 290), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255))



cv2.waitKey(0)

cv2.imshow("solar-system.jpg", img)

cv2.waitKey(0)