# Expr = polynomial in the form
# [(a,b)(c,d),etc] such that
# f(x) = a x ** b + c x ** d etc..
# Example: f(x) = x**3 -4x**2 + x + 6
# [(1,3),(-4,2),(1,1),(6,0)]
def polynomial(expr, x):
	return sum([ e[0] * x**e[1] for e in expr])
	

def divisors(n):
	n = abs(n)
	pos = [ e for e in range(1, n/2 + 1) if n % e == 0] + [ n ]
	return sorted(map(lambda x : -1 * x, pos) + pos)


def gcd(a,b):
	d = 1
	for da in divisors(a):
		for db in divisors(b):
			d = da if da == db and da > d else d
			
	return d


def subtractpoly(expr1, expr2):
	result = []
	for i in range(len(expr2)):
		r = (expr1[i][0] - expr2[i][0], expr1[i][1])
		if not r[0] == 0: result.append(r)
	return result + expr1[len(expr2):]


def longdivision(divider, dividend, result = []):
	if dividend == []: return result
	
	c1 = divider[0][0]; e1 = divider[0][1]; c2 = dividend[0][0]; e2 = dividend[0][1]
	c = c2 / c1; e = e2 - e1
	result.append((c, e))
	dividend = subtractpoly(dividend, [ (d[0] * c, d[1] + e) for d in divider ])
	return longdivision(divider, dividend, result)

	
def factorsOfPoly(expr):
	precision = 10
	
	const = [e[0] for e in expr if e[1] == 0]
	lead  = [e[0] for e in expr if e[1] == max([n[1] for n in expr])]

	if len(const) == 1 and len(lead) == 1:
		factors = []
		for c in divisors(const[0]):
			for m in divisors(lead[0]):
				x = float(c)/m
				print (c, m), polynomial(expr, x)
				if round(polynomial(expr, x), precision) == 0: 
					if not x in [ float(e[0]) / e[1] for e in factors]:
						if c < 0 and m < 0: c = -1 * c; m = -1 * m
						d = gcd(c,m)
						factors.append((c / d,m / d))
		
		return factors
	
	else: return None


poly1 = [(4,2),(20,1),(24,0)]
poly2 = [(2,1),(6,0)]
print longdivision(poly2,poly1)
