# platform: python3 macOS
from numpy import loadtxt
import numpy as np
import matplotlib.pyplot as plt

def check(wei, data):
	tmp = 0.0
	for k in range(5):
		tmp += wei[k] * data[k]

	if tmp > 0.0: return 1
	if tmp <= 0.0: return -1


# load the data
dataset = loadtxt("Problem7.dat")
initial = np.ones(len(dataset))
dataset = np.insert(dataset, 0, values=initial, axis=1)

# initialize the constants for recording the index
k = 0
tot = len(dataset)

# initialize the constants for calculating the average
upd = []
avg = 0


# start the main process
for N in range(1126):
	num = 0
	chg = 0
	wei = [0, 0, 0, 0, 0]

	while True:
		if num >= tot: break

		test = check(wei, dataset[k])

		if test != dataset[k][5]:
			wei += dataset[k][5] * dataset[k][:5]
			num = 0
			chg = chg + 1

		if test == dataset[k][5]:
			num = num + 1

		k = (k + 1) % tot

	np.random.seed(N)
	np.random.shuffle(dataset)

	avg = avg + chg
	upd.append(chg)


# print the result
print ("The average numbers of updates before the algorithm halts:", avg / 1126)
print ("The histogram of the number of updates versus the frequency of the number: ")
plt.title("The Number Of Updates V.S. The Frequency Of The Number")
plt.hist(upd, bins=40)
plt.show()