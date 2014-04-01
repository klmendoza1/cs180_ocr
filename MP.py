from os import listdir
import sys
from glob import glob
from pickle import dump
from PIL import Image
from numpy import asarray
from itertools import chain
from perceptron import Perceptron

consonants_spc=['s','t','h','y','w']
consonants = ['','k','n','m','r']
vowels = ['a','i','u','e','o']

def main():
  print "START: Training"
  perceptrons = list()
  # make perceptron for each character to be recognized
  for x in range(len(vowels)*len(consonants)):
    perceptrons.append(Perceptron(1024))
  train(perceptrons)
  print "END: Training"

  out_name = raw_input("Save perceptron data file as: ")
  out_file = open(out_name, "w")
  dump(perceptrons, out_file)

  print "START: Testing"
  # list compatible images
  compat = glob("*.png")
  if len(compat) > 0:
    print "Test images found:"
    for png in compat:
      print png
  else:
    print "n/a"
  
  # prompt to input image name
  while True:
    try:
      img_name = raw_input("Type filename with extension (Ctrl+C to exit): ")
    except KeyboardInterrupt:
      print
      print "Exiting."
      exit(0)
    # process image
    img = Image.open(img_name)
    
    counter = 0
    ans = None
    for x in range(len(perceptrons)):
      n = perceptrons[x]
      feed(img, n)
      n.activate()
      if n.get_output() == 1.0:
        ans = vowels[x]
        counter += 1
    
    if counter == 1: # if one neuron responded
      print img_name + " has been recognized as a katakana " + ans + "."
    else: # if multiple or no perceptrons responded
      print img_name + " was unrecognizable."

def train(perceptrons):
  for each_con in range(len(consonants)):   # for each consonant (and initial blank)
    for each_vow in range(len(vowels)):     # for each vowel
      print "Training: katakana '%s'" %(consonants[each_con]+vowels[each_vow])
      n = perceptrons[each_con*len(consonants)+each_vow]
      # perceptrons are arranged in a list in an order:
      # 'a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', ..., consonants[-1]+vowels[-1]
      ls1 = listdir("train/")
      ls1 = sorted(ls1)
      #ls1 = list of folders in folder 'train'

      errors  = 1      # initialize as 1 to enter loop
      
      while errors > 0:
        errors = 0     # change value to 0, counts instances of
                       # inconsistencies with solved and desired output
        for i in ls1: # for every folder in 'train'
          exp_out = 0   # must return negative match
          if str(i) == "train_"+consonants[each_con]+vowels[each_vow]:
            exp_out = 1 # training set is to the corresponding
                        # perceptron; must return positive match
          dir1 = "train/%s/" %i
          ls2 = listdir(dir1)
          ls2 = sorted(ls2)
          # list of files in folder 'train/train_xy' for x in consonants and y in vowels
          for j in ls2: # for every file in 'train/train_xy' for x in consonants and y in vowels
            img = Image.open(dir1 + j)
            feed(img, n)  # convert images to list of key value
            errors += n.train_step(exp_out) # add 1 if error is detected

def feed(pimg, n):
  im = asarray(pimg.convert('L'))
  img = list(chain(*im))
  n.set_input(img)

if __name__ == "__main__":
  
  
  main()
