#!/usr/bin/env python

from multiprocessing import cpu_count
from multiprocessing import Pool

def func(temp):
	while True:
		temp = (temp ** temp )
		if(temp > 5000):
			temp = 2


def main():
	number_of_cores = cpu_count()
	print("Number of cores availabe is {}".format(number_of_cores))
	use_cpu = 2
	pool = Pool(use_cpu)
	pool.map(func, range(use_cpu))

if __name__ == '__main__':
    main()
