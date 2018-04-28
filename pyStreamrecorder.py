# This script just needs Opencv to run
# Install opencv using pip: python -m pip install opencv-python
# See this link for more information: https://www.scivision.co/install-opencv-python-windows/
import cv2


# The Program can be stopped anytime by pressing q on the keyboard!

#=======Set parameters===========
IP = 'rtmp://127.0.0.1:1935/source' # Source IP adress (works also with rtsp and can even be a filepath to a mp4 file, but then you have to disable the line "source.open(IP)". Also it can be used to record from the local computers webcam, just set the IP to 0 and delete the line "source.open(IP)")
FILENAME = 'out.avi' # Name of the output file
OUTPUT_RESOLUTION = (1920,1080) # Resolution of the resulting output video
LIVE_VIEW_RESOLUTION = (800,600) # Resolution of the live view while recording
OUTPUT_FPS = 30 # Frames per second of the output file. Set preferably to the same as the input
VERBOSE = True # Print out message for each processed frame
#================================

# Open stream source
source = cv2.VideoCapture(IP)
source.open(IP)
source.set(cv2.cv2.CAP_PROP_FPS, OUTPUT_FPS)
# Start recorder
recorder = cv2.VideoWriter(FILENAME, cv2.VideoWriter_fourcc('M','J','P','G'),10, OUTPUT_RESOLUTION)

# If the stream couldnt be opened output error
if (source.isOpened() == False):
    print('Error opening video stream')
else:
    while(source.isOpened()): # Go as long as the input source is sending
        # Read th.e current frame
        ret, frame = source.read()
        # If a frame was found process it otherwise the stream has ended/the file is over
        if ret == True:
            # Write the frame to file
            recorder.write(cv2.resize(frame, OUTPUT_RESOLUTION))
            if VERBOSE == True:
                print("processed frame")
            cv2.imshow('Live view', cv2.resize(frame,LIVE_VIEW_RESOLUTION))
            if (cv2.waitKey(25) & 0xFF == ord('q')):
                cv2.destroyAllWindows()
                break
        else:
            print("File ended/Stream stopped")
            cv2.destroyAllWindows()
            break;
# Close all file operations
source.release()
recorder.release()

