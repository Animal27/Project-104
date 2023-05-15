import cv2

# Read the image
img = cv2.imread("planets.jpg")

text = "Sun"
# Add text to the image using putText()
cv2.putText(img, "Sun", (75, 300), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img, "Mercury", (210, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img, "Venus", (120, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img, "Earth", (300, 410), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img, "Mars", (480, 330), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img, "Jupiter", (700, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img, "Saturn", (830, 330), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img, "Uranus", (920, 430), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img, "Neptune", (1020, 500), cv2.FONT_HERSHEY_CO, 1, (0, 0, 255), 2)

# Display the image
cv2.imshow("output", img)
cv2.waitKey(0)
