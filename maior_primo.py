def maior_primo(n): 

	def ePrimo(k):	
			x = 2
			if k == 2:
					return True
			while k % x != 0 and x <= k/2:
					x = x + 1
			if k % x == 0:
					return False
			else:
					return True


	numero = n
	while numero > 0:
		if ePrimo(numero):
			return numero       	
		else:
			numero = numero - 1
