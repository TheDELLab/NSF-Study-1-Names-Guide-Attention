# Load necessary libraries
library(dplyr)
library(readr)

# Read the datasets
cleaned_file_005 <- read_csv("path/to/cleaned_file_005.csv")
audacity_file <- read_csv("path/to/005_audacity.csv")

# Combine words in the audacity_file dataset
audacity_grouped <- audacity_file %>%
  group_by(number) %>%
  summarise(
    combinedWordOnset = min(wordOnset),
    combinedWordOffset = max(wordOffset),
    combinedWord = paste(word, collapse = " ")
  )

# Add 1200 milliseconds to the trial onset time in cleaned_file_005 for mapping
cleaned_file_005 <- cleaned_file_005 %>%
  mutate(spokenWordStartTime = trialOnset + 1300)

# Merge the original audacity_file with cleaned_file_005
detailed_merged_data <- merge(cleaned_file_005, audacity_file, by.x = "targetNumber", by.y = "number", all.x = TRUE)

# Merge the detailed merged data with the grouped audacity data
final_detailed_dataset <- merge(detailed_merged_data, audacity_grouped, by = "number", all.x = TRUE)

# Write the final detailed dataset to a CSV file
write_csv(final_detailed_dataset, "path/to/final_detailed_gaze_spoken_word_dataset.csv")
