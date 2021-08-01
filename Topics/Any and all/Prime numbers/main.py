prime_numbers = [number for number in range(2, 1001) if all([number % divider for divider in range(2, number)])]
