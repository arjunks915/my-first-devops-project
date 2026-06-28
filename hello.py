print("Hello, arjun! Your DevOps journey has officially started.")
import os

# Create a new folder automatically
os.makedirs("devops_folder", exist_ok=True)

# Create a text file inside that folder and write into it
with open("devops_folder/status.txt", "w") as file:
    file.write("Automation works! This file was created by Python.")

print("Folder and file created successfully via code!")