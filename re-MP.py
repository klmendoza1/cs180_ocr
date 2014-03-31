from os import listdir
import sys
from glob import glob
from pickle import dump
from PIL import Image
from numpy import asarray
from itertools import chain
from perceptron import Perceptron

vowels = ['a','i','u','e','o']

def main():
  print "START: Training"
  perceptrons = list()
  for x in vowels:
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
    print "Compatible images found:"
    for png in compat:
      print png
  else:
    print "No compatible images found in current directory."
  
  # prompt to input image name
  while True:
    try:
      img_name = raw_input("Input image filename (Ctrl+C to exit): ")
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
        print "Neuron %i is responding." %x
        ans = str(x)
        counter += 1
    
    if counter == 1: # if one neuron responded
      print img_name + " has been recognized as a " + ans + "."
    else: # if multiple or no perceptrons responded
      print img_name + " was unrecognizable."

def train(perceptrons):
  """
    Use data from training-sets directory to train.
  """
  for digit in range(len(perceptrons)):
    
    print "TRAINING FOR %s" %vowels[digit]
    
    n = perceptrons[digit]
    
    ls1 = listdir("train/")
    ls1 = sorted(ls1)
    
    
    errors  = 1
    counter = 0
    
    while errors > 0:
      errors = 0
      for i in ls1: # for every directory in training sets
        
        ### SET EXPECTED OUTPUT FOR CURRENT DIRECTORY
        try:
          exp_out = 0   # for other digits, training as not recognized (0)
          if str(i) == "train_"+vowels[digit]:
            exp_out = 1 # corresponding digit,  training as recognized (1)
        except ValueError:
          break # ignore directories that are not named as an integer
        
        ### FOR EACH IMAGE, FEED PIXEL SET AS INPUT AND USE exp_out TO CHECK
        dir1 = "train/%s/" %i
        ls2 = listdir(dir1)
        ls2 = sorted(ls2)
        for j in ls2: # for every image
          
          img = Image.open(dir1 + j)
          feed(img, n)
          counter += 1
          errors += n.train_step(exp_out) # train with inputs
        # end of j-loop
      # end of i-loop
      print "Errors: %i" %errors
    # end of while loop
    
    
    
    print "Images processed: %i" %counter
    
  # end of for loop
  
# end of def train
  

def feed(pimg, n):
  im = asarray(pimg.convert('L'))
  img = list(chain(*im))
  n.set_input(img)

if __name__ == "__main__":
  
  
  main()
