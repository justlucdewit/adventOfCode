def part2():
	inp = [int(x) for x in  open('input.txt').read().split(',')]

	for x1 in range(100):
		for x2 in range(100):
			P = [x for x in inp]
			P[1] = x1
			inp[2] = x2
			i = 0
			while True:
				opp= P[i]
				i1 = P[i+1]
				i2 = P[i+2]
				i3 = P[i+3]
				if opp== 1:
					P[i3] = P[i1]+P[i2]
				elif opp== 2:
					P[i3] = P[i1]*P[i2]
				else:
					assert opp== 99
					break
				i += 4
			if P[0] == 19690720:
				print(100*x1+x2)

def part1():
	inp = [int(x) for x in  open('input.txt').read().split(',')]
	inp[1] = 12
	inp[2] = 2
	i = 0
	while True:
		opp= inp[i]
		i1 = inp[i+1]
		i2 = inp[i+2]
		i3 = inp[i+3]
		if opp== 1:
			inp[i3] = inp[i1]+inp[i2]
		elif opp== 2:
			inp[i3] = inp[i1]*inp[i2]
		else:
			assert opp== 99
			break
		i += 4
	print(inp[0])
	
part1()