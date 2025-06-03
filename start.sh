#!/bin/bash

# Prompt for topic
read -p "Enter your topic to explain like you're 5: " topic

# Prompt for output format
read -p "CLI or .md File? " output_format

# Convert to uppercase for comparison
output_format=$(echo "$output_format" | tr '[:lower:]' '[:upper:]')

# Prompt for explanation style
read -p "Concise or Comprehensive? " explanation_style

# Convert to uppercase for comparison
explanation_style=$(echo "$explanation_style" | tr '[:lower:]' '[:upper:]')

# Run the ELI5 assistant
python eli5_assistant.py "$topic" "$output_format" "$explanation_style"
