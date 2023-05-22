# Import necessary libraries
from psychopy import visual, event
import pylink

# Set up EyeLink connection
eyelink = pylink.EyeLink()
eyelink.send_command("screen_pixel_coords = 0 0 1919 1079")
eyelink.send_command("screen_phys_coords = -29.7 -16.7 29.7 16.7")
eyelink.send_command("link_sample_data = LEFT,RIGHT,GAZE,AREA,STATUS")
eyelink.send_command("button_function 5 'accept_target_fixation'")

# Set up Psychopy window and stimuli
win = visual.Window(size=(1920, 1080), fullscr=True, units='deg', monitor='testMonitor')
image = visual.ImageStim(win, image='example.png', pos=[0,5])
ready = visual.TextStim(win, text='READY', pos=[0,0], color='white')

# Start EyeLink recording and calibration
eyelink.open_data_file("example.edf")
pylink.flush_getkey_queue()
eyelink.do_tracker_setup()

# Display image and wait for fixation to be on image for 2 seconds
eyelink.start_recording()
while True:
    image.draw()
    win.flip()
    if eyelink.get_input_key() == pylink.ESCKEY:
        break
    if eyelink.eye_available():
        if eyelink.is_new_data_available():
            left_eye = eyelink.get_float_data("LEFT_GAZE_X,LEFT_GAZE_Y")
            right_eye = eyelink.get_float_data("RIGHT_GAZE_X,RIGHT_GAZE_Y")
            if left_eye != pylink.MISSING_DATA and right_eye != pylink.MISSING_DATA:
                x, y = (left_eye[0] + right_eye[0]) / 2, (left_eye[1] + right_eye[1]) / 2
                if abs(x) < 3 and abs(y - 5) < 3:
                    eyelink.send_command("record_status_message 'on_image'")
                    fixation_start_time = win.getFutureFlipTime(clock='ptb') + 2.0  # Wait for 2 seconds of stable fixation
                    while win.getFutureFlipTime(clock='ptb') < fixation_start_time:
                        if eyelink.get_input_key() == pylink.ESCKEY:
                            break
                        if eyelink.eye_available():
                            if eyelink.is_new_data_available():
                                left_eye = eyelink.get_float_data("LEFT_GAZE_X,LEFT_GAZE_Y")
                                right_eye = eyelink.get_float_data("RIGHT_GAZE_X,RIGHT_GAZE_Y")
                                if left_eye != pylink.MISSING_DATA and right_eye != pylink.MISSING_DATA:
                                    x, y = (left_eye[0] + right_eye[0]) / 2, (left_eye[1] + right_eye[1]) / 2
                                    if abs(x) < 3 and abs(y - 5) < 3:
                                        ready.draw()
                                        win.flip()
                                        event.waitKeys(keyList=['5'])
                                        break
                    break

# End EyeLink recording and close connection
eyelink.set_offline_mode()
pylink.close_graphics()
eyelink.close_data_file()
