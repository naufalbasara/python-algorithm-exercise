n = list(map(int,input().split()))
def main(n):
	if len(n) > 2 or len(n) == 0:
		return
	else:
		print(sum(n))
		print(n[0] - n[1])
		print(n[0] * n[1])
		print(n[0]//n[1])
		print(n[0] % n[1])
		return
main(n)