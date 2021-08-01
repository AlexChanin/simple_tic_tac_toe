n = int(input())
score_li = [input().split() for i in range(n)]
print([name[0] for name in score_li if name[1] == 'win'])
print(sum([1 for res in score_li if res[1] == 'win']))
