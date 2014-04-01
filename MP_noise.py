from PIL import Image
import math
import random
import os

consonants_spc=['s','t','h','y','w']
consonants = ['','k','n','m','r']
vowels = ['a','i','u','e','o']

def add_noise(original, num, amt=0.3):
  img    = Image.open(original)
  width  = img.size[0]
  height = img.size[1]
  pixels = img.load()

  for i in range(width):      # for each column
    for j in range(height):   # for each row
      x = random.random()
      if x < amt:             # probability is amt
        y = random.randint(1,255)
        pixels[i,j] = (y, y, y, 255)
  out_filename = os.path.splitext(original)[0] + "_%i.png" %num
  img.save(out_filename, "png")
  
if __name__ == "__main__":
  
  for bawat in consonants:
    for each in vowels:
      for y in range(1, 31):
        add_noise("train/train_%s/%s.png"%(bawat+each,bawat+each), y)
