from PIL import Image
import numpy as np

stickers = [
    "naga_coffee.png", "naga_sip.png", "naga_sleep.png",
    "naga_fine.png", "naga_peek.png", "naga_cozy.png"
]

# Load and resize all to same dimensions
images = [np.array(Image.open(f).convert("RGB").resize((256, 256))) for f in stickers]
avg = np.mean(images, axis=0).astype(np.uint8)
Image.fromarray(avg).save("blend.png")
