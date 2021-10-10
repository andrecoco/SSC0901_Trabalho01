import read_services
import check_ports

def check_ip_address(ip):
	services = read_services.read_services()
	if (valid_ip_address(ip)):
		# print("ip ta top")
		# check_address(ip)
		open_ports = check_ports.check_port_range(1, 1000, ip) # testa as 50 primeiras portas do localhost

		if (not open_ports):
		    print("Nenhuma porta está aberta!")
		else:
		    for open_port in open_ports:
		        print(services[open_port])
	else:
		print("IP inválido!")

def valid_ip_address(ip):
	'''
	Testa se o ip alvo passado pelo usuário é um endereço IPv4 válido.

	Retorna um booleano que indica se o ip é válido ou não.
	'''
	tmp = ip.split('.')
	if len(tmp) != 4:
		return False
	for x in tmp:
		if not x.isdigit():
			return False
		i = int(x)
		if i < 0 or i > 255:
			return False
	return True