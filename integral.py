def simp(f,a,b,n=8000):
	pas= (b-a)/n
	spair=0
	simpair=0
	if (n == 2):
		integ= (pas/3)*(f(a)+f(b)+4*f(a+pas))
		print("l'approximation de l'intégral est: ",integ)
	else:
		d= n//2
		for loop in range(d):
			simpair += f(a+(2*loop+1)*pas)
			spair += f(a+2*loop*pas)
		integ = (pas/3)*(f(a)+f(b)+4*simpair+2*spair)
		print("Integral aproximation: ",integ)
