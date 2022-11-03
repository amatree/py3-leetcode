import os, os.path

easy = os.listdir("Easy\\")
medium = os.listdir("Medium\\")
hard = os.listdir("Hard\\")

print(f"Total Easy: {len(easy)}")
print(f"Total Medium: {len(medium)}")
print(f"Total Hard: {len(hard)}")