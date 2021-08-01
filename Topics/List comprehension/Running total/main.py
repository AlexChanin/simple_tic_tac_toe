s_input = [int(x) for x in input()]
cumulative_sum = [sum(s_input[0: i + 1]) for i in range(len(s_input))]
print(cumulative_sum)
