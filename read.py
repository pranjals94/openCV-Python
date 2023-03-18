import cv2 as cv
import os

# os.system('start') # run commands in command prompt
img = cv.imread('Images/cat.jpg')
img2 = cv.imread('Images/dog.jpg')
cv.imshow('cat', img)
cv.waitKey(1000)  # delay certain amount of time
cv.imshow('cat', img2)
cv.waitKey(1000)  # delay certain amount of time

# capture = cv.VideoCapture(0)  # 0 means first camera that is attached to computer
# while True:
#     isTrue, frame = capture.read()
#     cv.rectangle(frame, (200, 10), (frame.shape[1] // 2, frame.shape[0] // 2), (0, 225, 0), thickness=5)
#     cv.circle(frame, (100, 100), 40, (0, 225, 0), thickness=2)
#
#     cv.imshow('video', frame)
#     if cv.waitKey(1) & 0xFF == ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

# ---------------------------------------------------------------------------------------------
# # importing the subprocess module
# import subprocess
#
# # using the check_output() for having the network term retrieval
# devices = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'])
#
# # decode it to strings
# # print(devices)
# devices = devices.decode('ascii')
# devices = devices.replace("\r", "")
#
# # displaying the information
# print(devices)
# -------------------------------------------------------------------------------------------------


# # import module
# import os
#
# # scan available Wifi networks
# os.system('cmd /c "netsh wlan show networks"')
#
# # input Wifi name
# name_of_router = input('Enter Name/SSID of the Wifi Network you wish to connect to: ')
#
# # connect to the given wifi network
# os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')
#
# print("If you're not yet connected, try connecting to a previously connected SSID again!")
#---------------------------------------------------------------------------------------------------

