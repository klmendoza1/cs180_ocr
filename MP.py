from PIL import Image
#from scipy import ndimage
from math import exp
from numpy import asarray
from operator import mul, add, sub
from itertools import chain
from random import uniform

def regression(x,d,alpha=0.01):
	m = len(x) 			# size
	n = len(x[0]) 		# features
	weights = tuple(uniform(-0.5, 0.5) for i in range(n+1)) #(random() for i in range(n+1))
	_x=[[1]+each for each in x]

	s = lambda z: 1 if 1/(1+exp(-z))>=0.5 else 0 #sigmoid fcn
	y = lambda u: sum(map(mul,u,weights))/(n+1)
	sy = lambda zu: s(y(zu))
	for index in range(m):
		print y(_x[index])
		print "desired: "+str(d[index])
		if not sy(_x[index])==d[index]:
			print "whoa"
			weights=tuple(weights[j]+(alpha*(d[index]-sy(_x[index]))*((_x[index])[j])) for j in range(n+1))

	return weights,sy

def main():
	#chars = ['a','i','u','e','o']
	huehue =  lambda qwerty: float(qwerty)/float(255) #lambda qwerty: 1 if qwerty<=150 else 0 
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
			
			img = [huehue(huahua) for huahua in img] #[huehue(huahua) for huahua in img]
			x_train.append(img)
			print "image"+xid+" translation success"
		x_train_all.append(x_train)
	#print x_train_all
	ones=[1 for each in range(30)]
	weights_a,fcn = regression(x_train_all[0], ones)
	#weights_i,_ = regression(x_train_all[1], 1)
	#weights_u,_ = regression(x_train_all[2], 1)
	#weights_e,_ = regression(x_train_all[3], 1)
	#weights_o,_ = regression(x_train_all[4], 1)

	print x_train_all[0][0]

	#test here
	print "weights: "
	print weights_a

	tim = asarray(Image.open('train_a/31.jpg').convert('L'))
	timg = [1]+list(chain(*tim))
	timg = [huehue(huahua) for huahua in timg]

	print "timg: "
	print timg

	print "result: "

	print sum(map(mul,timg,weights_a))

if __name__ == '__main__':
  main()