
import random
import math

class Perceptron(object):
  
  def __init__(self, width, a="step", t=1, l=0.1):
    self.threshold  = t
    self.inputs     = [0] * width
    self.weights    = [1] * width
    self.l_rate     = l
    self.a_func     = a
  
  def append(self, i, w):
    self.inputs.append(i)
    self.weights.append(w)
    if len(inputs) != len(weights):
      print "Invalid test data! Exiting..."
      exit(1)
  
  def set_input(self, i): self.inputs = i
  
  def activate(self):
    i_sum = 0.0
    # perform summation operation of i_n * w_n
    for x in range(len(self.inputs)):
      i_sum += self.inputs[x] * self.weights[x]
    
    diff = i_sum - self.threshold
    
    # using difference, determine output
    if diff > 0:
      self.output = 1.0
    else:
      self.output = 0.0
    
  def get_output(self): return self.output

  def train_step(self, exp_out):
    
    # perform activation
    self.activate()
    det_out = self.output # determined output
    
    # if output is not correct, calculate error
    error = 0
    error_rate = 0
    if det_out != exp_out:
      error = exp_out - det_out
      # adjust weights
      for x in range(len(self.inputs)):
        
        self.weights[x] += self.l_rate * error * self.inputs[x]
      
      self.threshold -= self.l_rate * error
      return 1 # return 1 for error
    else:
      return 0 # return 0 for no errors
