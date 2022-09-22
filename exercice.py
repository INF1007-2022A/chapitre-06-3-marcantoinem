#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools as i


def get_maximums(numbers):
	new_list = []
	for old_list in numbers:
		new_list.append(max(old_list))
	return new_list

def join_integers(numbers):
	return "".join(str(number) for number in numbers)

def generate_prime_numbers(limit):
	primes = []
	is_prime = [True for _ in range(limit+1)]
	for i in range(2, math.isqrt(limit)+1):
		if is_prime[i]:
			primes.append(i)
			for j in range(2,limit//i+1):
				is_prime[i*j] = False
	for i in range(math.isqrt(limit)+1, limit+1):
		if is_prime[i]:
			primes.append(i)
	return primes

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	if excluded_multiples == None:
		numbers = [x for x in range(1, num_combinations+1)]
	else:
		numbers = [x for x in range(1, num_combinations+1) if x % excluded_multiples != 0]

	return [letter + str(number) for number in numbers for letter in strings]

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
