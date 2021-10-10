import socket

def _check_port(port, ip):
	'''
	Testa se a porta passada por argumento está aberta no ip alvo.

	Retorna um booleano que indica se a porta está aberta ou não.
	'''
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	soc.settimeout(0.1)
	code = soc.connect_ex((ip, port))
	soc.close()
	if (code == 0): 
		return True
	else: 
		return False
	

def check_port_range(begin, end, ip):
	'''
	Testa se as portas entre begin e end (inclusas) estão abertas no ip alvo.

	Retorna uma lista de todas as portas abertas.
	'''
	result = []
	for port in range(begin, end + 1):
		if(_check_port(port,ip)):
			result.append(port)
	
	return result

def check_port_list(ports, ip):
	'''
	Testa se as portas na lista passada por argumento estão abertas no ip alvo.

	Retorna uma lista de todas as portas abertas.
	'''
	result = []
	for port in ports:
		if(_check_port(port,ip)):
			result.append(port)
	
	return result

# Roda se o módulo for rodado diretamente, não importado
if __name__ == "__main__":
	services = read_services.read_services()
	if (valid_ip_address(ip)):
		print("ip ta top")
		# check_address(ip)
		open_ports = check_port_range(1, 1000) # testa as 50 primeiras portas do localhost

		if (not open_ports):
		    print("\nNenhuma porta está aberta!")
		else:
		    for open_port in open_ports:
		        print(services[open_port])
	else:
		print("\nIP inválido!")