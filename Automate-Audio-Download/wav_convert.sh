#!/bin/bash

input_folder="$1"
output_folder="${input_folder}_wavs"

# Create the output folder if it doesn't exist
mkdir -p "$output_folder"

# Loop through each MP3 file in the input folder
for file in "$input_folder"/*.mp3; do
    # Extract the filename without extension
    filename=$(basename "$file" .mp3)
    # Set the output path for the WAV file
    output_file="$output_folder/$filename.wav"
    
    # Convert MP3 to WAV using FFmpeg
    ffmpeg -i "$file" "$output_file"
done
