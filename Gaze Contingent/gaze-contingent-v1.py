import pylink
import time

# Connect to the EyeLink eyetracker
eyelink = pylink.EyeLink()
eyelink.openDataFile("image_gaze_contingent.edf")
eyelink.sendCommand("screen_pixel_coords = 0 0 %d %d" % (800, 600))
eyelink.sendMessage("DISPLAY_COORDS  0 0 %d %d" % (800, 600))
eyelink.setOfflineMode()

# Create a window to display the stimuli
win = visual.Window(size=(800, 600), units='pix', color=(1, 1, 1))

# Create an image stimulus
image = visual.ImageStim(win, image='image.jpg')

# Start recording eye position
eyelink.startRecording(1, 1, 1, 1)

# Draw the image on the screen
image.draw()
win.flip()

# Get the current time
start_time = time.time()

# Check if the gaze is on the image
while time.time() - start_time < 10:
    gaze_x, gaze_y = eyelink.getLastSample().getLeftEye().getGaze()
    if gaze_x is not None and gaze_y is not None:
        if image.contains(gaze_x, gaze_y):
            if time.time() - start_time > 2:
                # If gaze is on the image for more than 2 seconds, stop recording
                eyelink.stopRecording()
                break
    time.sleep(0.01)

# Close the EyeLink connection
eyelink.close()

# Close the window
win.close()
