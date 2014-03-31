from PIL import Image
import math
import random
import os

vowels = ['a','i','u','e','o']
BLACK = (0,0,0)

noise_amt = 0.3

def add_noise(original, amt, num):
  
  img    = Image.open(original)
  width  = img.size[0]
  height = img.size[1]
  pixels = img.load()
  # must use digits to iterate through pixels
  for i in range(width):
    for j in range(height):
      x = random.random()
      if x < amt:
        y = random.randint(1,255)
        pixels[i,j] = (y, y, y, 255)
  out_filename = os.path.splitext(original)[0] + "_%i.png" %num
  img.save(out_filename, "PNG")
  
if __name__ == "__main__":
  
  for each in vowels:
    for y in range(1, 31):
      add_noise("train/train_%s/%s.png"%(each,each),noise_amt, y)
