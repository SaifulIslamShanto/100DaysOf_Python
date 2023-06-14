import os

# os.mkdir("DATA")

if (not os.path.exists("data")):
    os.mkdir("data")

for i in range(0, 10):
    os.rename(f"data/Tutorial{i+1}", f"data/Tutorial {i+1}")
    # os.mkdir()
