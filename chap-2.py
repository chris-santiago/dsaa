import time
import random

MAX = 1e7
MIN = 0
N = int(1e6)
X = random.randint(MIN, MAX)

arr = [random.randint(MIN, MAX) for _ in range(N)]
arr_sort = sorted(arr)


def linear_search(array, value):
	steps = 0
	for i,x in enumerate(array):
		steps += 1
		if x == value:
			return i, steps
		if x > value:
			return None, steps
	return None, steps


def binary_search(array, value):
	steps = 0
	lower = 0
	upper = len(array) - 1

	while lower <= upper:
		steps += 1
		midpoint = (upper + lower) // 2
		value_at_midpoint = array[midpoint]

		if value_at_midpoint == value:
			return midpoint, steps
		elif value_at_midpoint > value:
			upper = midpoint - 1
		elif value_at_midpoint < value:
			lower = midpoint + 1
	return None, steps


start = time.perf_counter()
res = linear_search(arr_sort, X)

end = time.perf_counter()
print(f'Linear search took {end-start} seconds for {res[1]} steps.')

start = time.perf_counter()
res = binary_search(arr_sort, X)
end = time.perf_counter()
print(f'Binary search took {end-start} seconds for {res[1]} steps.')

