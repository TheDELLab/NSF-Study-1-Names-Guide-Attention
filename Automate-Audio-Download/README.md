# Automate-Audio-Download
Selenium Automation to Download Audio Files from Natural Reader

# Install check
- Make sure you have installed webdriver-manager and pandas // 'pip install webdriver-manager' , 'pip install pandas'

### Instructions

- First execute `python selenium-automate-v2.py` // if first time, accept chrome permission request then run again.
- Copy the audio files into folders named condition_1 and condition_2 within the same directory as wav_convert.sh
- Now, `bash wav_convert.sh ./condition_1` and `bash wav_convert.sh ./condition_2`

---
- Note this works only on MacOS, and requires `ffmpeg`, install ffmpeg with `brew install ffmpeg` 
