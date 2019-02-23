# platform: python3 macOS
import random
import numpy as np
import matplotlib.pyplot as plt

# initialize the constants for calculating the average
avg_in = 0
avg_out = 0
E_in = []
E_out = []
minus = []

for N in range(1000):

	# load the data
	datasetx = []
	datasety = []
	for i in range(20):
		datasetx.append(random.uniform(-1, 1))
		if (datasetx[i] >= 0): datasety.append(1)
		if (datasetx[i] < 0):  datasety.append(-1)
	datasetx.sort()
	datasety.sort()

	for i in range(20):
		flp = random.uniform(0, 1)
		if flp <= 0.2:
			datasety[i] = -1 * datasety[i]

	# initialize the constants for calculate E_in and E_out
	s = 0
	theta = 0.0
	number = 0
	minerr = 2147483647.0
	hypths = np.ones(len(datasetx))


	# start the main process
	for i in range(40):
		if i - 20 < 0:  hypths[i % 20] = -1
		if i - 20 >= 0: hypths[i % 20] = 1

		err = 0.0
		tmps = []
		tmpt = []
		for k in range(20):
			if (datasety[k] != hypths[k]): err += 1

		if (err <= minerr) and (i % 20 != 19):
			minerr = err
			tmps.append(hypths[i % 20] * -1)
			tmpt.append((datasetx[i % 20] + datasetx[i % 20 + 1]) / 2)
			
			number = len(tmpt)
			index = random.randint(0, number - 1)
			s = tmps[index]
			theta = tmpt[index]

	avg_in = avg_in + minerr / 20
	avg_out = avg_out + 0.5 + 0.3 * s * (abs(theta) - 1)
	E_in.append(minerr / 20)
	E_out.append(0.5 + 0.3 * s * (abs(theta) - 1))
	minus.append((minerr / 20) - (0.5 + 0.3 * s * (abs(theta) - 1)))
	print ("Round", N, "with  E_in = %.2f " % E_in[N], "E_out =", E_out[N])


# print the result
print ("The average of E_in is", avg_in / 1000)
print ("The average of E_out is", avg_out / 1000)
plt.title("E_in V.S. E_out")
plt.xlim((0, 1))
plt.ylim((0, 1))
plt.scatter(E_in, E_out, alpha = 0.1)
plt.show()

plt.title("E_in - E_out")
plt.hist(minus, bins=40)
plt.show()
