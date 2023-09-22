from psychopy import visual, monitors

# Create a window to access display properties
win = visual.Window()

# Get the primary monitor (usually the main screen)
primary_monitor = monitors.Monitor('testMonitor')

# Manually set the physical size of the monitor in millimeters
primary_monitor.setSizePix((1920, 1080))  # Set the screen size in pixels
primary_monitor.setWidth(518.4)  # Set the screen width in millimeters

# Calculate screen height based on aspect ratio
aspect_ratio = primary_monitor.getSizePix()[0] / primary_monitor.getSizePix()[1]
screen_height_mm = primary_monitor.getWidth() / aspect_ratio

print(f"Screen Size (pixels): {primary_monitor.getSizePix()}")
print(f"Screen Resolution (mm): Width {primary_monitor.getWidth()}, Height {screen_height_mm}")

# Close the PsychoPy window
win.close()
