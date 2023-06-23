from psychopy import visual, core, sound, event

# create a window
win = visual.Window([800,600], color="white", units='pix')

# create some stimuli
number1 = visual.TextStim(win, text="1", pos=(-200,0), color="black")
number2 = visual.TextStim(win, text="2", pos=(200,0), color="black")

# create an audio stimulus
audio = sound.Sound('my_sound.wav')  # replace 'my_sound.wav' with your actual sound file

# draw the stimuli and flip the window
number1.draw()  # this will draw number 1
number2.draw()  # this will draw number 2
win.flip()  # this will update the window

# play the audio
audio.play()

# wait for a key press
keys = event.waitKeys(keyList=['left', 'right'])

# close the window
win.close()

# quit the experiment
core.quit()
