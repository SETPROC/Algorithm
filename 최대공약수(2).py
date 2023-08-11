#유클리드 알고리즘
#a와 b의 최대공약수는 'b'와 'a를 b로 나눈 나머지'의 최대공약수와 같다.
#즉, gcd(a,b) = gcd(b,a%b)이다.
#어떤 수와 0의 최대공약수는 자기 자신이다.
#즉, gcd(n,0)=n

def gcd(a,b):
	if b==0:
		return a
	return gcd(b,a%b)

print(gcd(1,5))
print(gcd(3,6))
print(gcd(60,24))
print(gcd(81,27))
