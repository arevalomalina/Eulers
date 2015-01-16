import utils

counter = 0
i = 1
while counter < 10001:
	i += 1
	print counter
	if utils.is_prime(i):
		counter += 1

print i 