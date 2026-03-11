from withoutbg import *

# Initialize model once
model = WithoutBG.opensource()

img = "Screenshot_1.png" #instead of Screenshot_1.png type in your picture name and file type

# Process image
result = model.remove_background(img)
result.save('Output.png')

# Process with progress callback
def progress(value):
    print(f"Progress: {value * 100:.1f}%")

result = model.remove_background(img, progress_callback=progress)