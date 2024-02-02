import pylink
from psychopy import visual, core, event, monitors
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy from math import hypot
# Connect to the tracker
tk = pylink.EyeLink('100.1.1.1')
# Open an EDF data file on the Host PC
tk.openDataFile('psychopy.edf')
# Put the tracker in offline mode before we change tracking parameters
tk.setOfflineMode()
# Make all types of eye events available over the link, especially the
# FIXUPDATE event, which reports the current status of a fixation at
# predefined intervals (default = 50 ms)
event_flags = 'LEFT,RIGHT,FIXATION,FIXUPDATE,SACCADE,BLINK,BUTTON,INPUT'
tk.sendCommand(f'link_event_filter = {event_flags}')
# Screen resolution
SCN_W, SCN_H = (1280, 800)
# Open a PsyhocPy window
win = visual.Window((SCN_W, SCN_H), fullscr=False, units='pix')

# Pass the display pixel coordinates (left, top, right, bottom) to the tracker
coords = f"screen_pixel_coords = 0 0 {SCN_W - 1} {SCN_H - 1}"
tk.sendCommand(coords)
# Request Pylink to use the custom EyeLinkCoreGraphicsPsychoPy library
# to draw calibration graphics (target, camera image, etc.)
genv = EyeLinkCoreGraphicsPsychoPy(tk, win)
pylink.openGraphicsEx(genv)

# Calibrate the tracker
calib_msg = visual.TextStim(win, text='Press ENTER twice to calibrate') calib_msg.draw()
win.flip()
tk.doTrackerSetup()


# Run 3 trials in a for-loop
# in each trial, first show a fixation dot, wait for the participant # to gaze at the fixation dot, then present an image for 2 secs
for i in range(3):
    # Prepare the fixation dot in memory
    fix = visual.GratingStim(win, tex='None', mask='circle', size=30.0)
    # Load the image
    img = visual.ImageStim(win, image='woods.jpg', size=(SCN_W, SCN_H))
    # Put tracker in Offline mode before we start recording
    tk.setOfflineMode()
    # Start recording
    tk.startRecording(1, 1, 1, 1)
    # Wait for the block start event to arrive, give a warning # if no event or sample is available
    block_start = tk.waitForBlockStart(100, 1, 1)
    if block_start == 0:
            print("ERROR: No link data received!")
    # Check eye availability; 0-left, 1-right, 2-binocular
    # read data from the right eye if tracking in binocular mode eye_to_read = tk.eyeAvailable()
    if eye_to_read == 2:
            eye_to_read = 1
    
    # Show the fixation dot
    fix.draw()
    win.flip()
    
    # Gaze trigger
    # wait for gaze on the fixation dot (for a minimum of 300 ms) 
    fix_dot_x, fix_dot_y = (SCN_W/2.0, SCN_H/2.0)
    triggered = False
    fixation_start_time = -32768
    
    while not triggered:
        # Check if any new events are available 
        dt = tk.getNextData()
        if dt == pylink.FIXUPDATE:
            ev = tk.getFloatData()
            if ev.getEye() == eye_to_read:
                # 1 deg = ? pixels in the current fixation
                ppd_x, ppd_y = ev.getEndPPD()
        
                # Get the gaze error
                gaze_x, gaze_y = ev.getAverageGaze() 
                gaze_error = hypot((gaze_x - fix_dot_x)/ppd_x,
                                                   (gaze_y - fix_dot_y)/ppd_y)
                if gaze_error < 1.5:
                    # Update fixation_start_time, following the first 
                    # FIXUPDATE event
                    if fixation_start_time < 0:
                        fixation_start_time = ev.getStartTime()
                    else:
                    # Break if the gaze is on the fixation dot
                    # for > 300 ms
                        if (ev.getEndTime() - fixation_start_time) >= 300:
                            triggered = True 
                else:
                    fixation_start_time = -32768
    # Show the image for 2 secs 
    img.draw()
    win.flip()
    core.wait(2.0)
    
    # Clear the screen
    win.color = (0, 0, 0)
    win.flip()
    core.wait(0.5)
    
    # Stop recording
    tk.stopRecording()
    # Close the EDF data file on the Host
    tk.closeDataFile()
    
# Close the EDF data file on the Host
tk.closeDataFile()

# Download the EDF data file from Host
tk.receiveDataFile('psychopy.edf', 'psychopy.edf')
# Close the link to the tracker
tk.close()
# Close the graphics
win.close()
core.quit()

            
        
