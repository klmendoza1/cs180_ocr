from PIL import Image
#from scipy import ndimage
from numpy import asarray
from itertools import chain

def regression(x,d,alpha=0.01):
	m = len(x) 			# size
	n = len(x[0]) 		# features
	weights = tuple(random() for i in range(n+1))
	_x=[[1]+each for each in x]

	s = lambda z: 1 if 1/(1+ exp(z))>=0.5 else 0 #sigmoid fcn
	y = lambda u: s(sum(map(mul,u,weights)))

	for index in range(m):
		if not y(_x[index])==d[index]:
			weights=tuple(weights[j]+(alpha*(d[index]-y(_x[index]))*((_x[index])[j])) for j in range(n+1))

	return weights,y

def main():
	chars = ['a','i','u','e','o']
	x_train_all = []
	for each1 in chars:
		x_train = []
		for each2 in range(100):
			xid = str(each2)
			if each2<10:
				xid = '0'+xid
			im = asarray(Image.open('train_'+each1+'/'+xid+'.jpg').convert('L'))
			img = list(chain(*im))
			x_train.append(img)
		x_train_all.append(x_test)
	#print x_train_all
	ones=[1 for each in range(100)]
	weights_a,fcn = regression(x_train_all[0], 1)
	weights_i,_ = regression(x_train_all[1], 1)
	weights_u,_ = regression(x_train_all[2], 1)
	weights_e,_ = regression(x_train_all[3], 1)
	weights_o,_ = regression(x_train_all[4], 1)

	#test here


if __name__ == '__main__':
  main()