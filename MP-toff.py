from PIL import Image
#from scipy import ndimage
from math import exp
from numpy import asarray
from operator import mul, add, sub
from itertools import chain
from random import random

def regression(x,d,alpha=0.01):
	m = len(x) 			# size
	n = len(x[0]) 		# features
	weights = tuple(random()-0.5 for i in range(n+1))
	_x=[[1]+each for each in x]

	ss = lambda zz: 1/(1+exp(-zz))
	s = lambda z: 1 if ss(z)>=0.5 else 0 #sigmoid fcn
	y = lambda u: sum(map(mul,u,weights))
	sy = lambda zu: s(y(zu))

	for index in range(m):
		#if index==0:
		#	print y(_x[index])
		#	print d[index]
		print str(y(_x[index]))+", "+str(ss(y(_x[index])))+", "+str(sy(_x[index]))
		if not sy(_x[index])==d[index]:
			print "whoa"
			weights=tuple(int(weights[j]+(alpha*(d[index]-sy(_x[index]))*((_x[index])[j]))) for j in range(n+1))

	return weights,y

def main():
	#chars = ['a','i','u','e','o']
	chars = ['a']
	x_train_all = []
	for each1 in chars:
		x_train = []
		for each2 in range(30):
			xid = str(each2)
			if each2<10:
				xid = '0'+xid
			im = asarray(Image.open('train_'+each1+'/'+xid+'.jpg').convert('L'))
			img = list(chain(*im))
			huehue = lambda qwerty: float(255-qwerty)/float(255)
			img = [huehue(huahua) for huahua in img]
			x_train.append(img)
			if each2==1:
				print img
			print "image"+xid+" translation success"
		x_train_all.append(x_train)
	#print x_train_all
	ones=[1 for each in range(30)]
	weights_a,fcn = regression(x_train_all[0], ones)
	#weights_i,_ = regression(x_train_all[1], 1)
	#weights_u,_ = regression(x_train_all[2], 1)
	#weights_e,_ = regression(x_train_all[3], 1)
	#weights_o,_ = regression(x_train_all[4], 1)

	#test here
	print "weights: "
	print weights_a

	tim = asarray(Image.open('train_a/31.jpg').convert('L'))
	timg = [1]+list(chain(*tim))

	print "timg: "
	#print timg

	print "result: "
	print sum([a*b for a,b in zip(timg,weights_a)])

if __name__ == '__main__':
  main()