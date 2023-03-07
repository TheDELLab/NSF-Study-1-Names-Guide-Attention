from psychopy import visual, sound

# Create a window to display the stimuli
win = visual.Window(fullscr=True, color=(1, 1, 1))

# Load the audio file
my_sound = sound.Sound('my_audio_file.mp3')

# Set the volume of the audio stimulus
my_sound.setVolume(0.5)

# Play the audio stimulus
my_sound.play()

# Wait for the audio to finish playing
my_sound.wait()

# Stop the audio stimulus
my_sound.stop()

# Close the window
win.close()
