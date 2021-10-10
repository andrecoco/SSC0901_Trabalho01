# import check_ip
# import re
import sys
import check_ip

# Comando para pedir ajuda
if (sys.argv[1] == '--help'):
	print('* Default - por padrão, são escaneadas as 1000 primeiras portas do ip_alvo')
	print('> python3 main.py <ip_alvo>')
	print('\nOutros modos:')
	print('\n* Porta específica - escaneia apenas uma determinada porta em um determinado endereço IPv4')
	print('> python3 main.py <ip_alvo> <porta_alvo>')
	print('\n* Range - escaneia um determinado intervalo de endereços IPv4')
	print('> python3 main.py <ip_inicio>-<ip_final>')
else:
	# print(sys.argv[1][0])
	# if (sys.argv[1][0] == '-')
	ip = sys.argv[1]
	print(ip)
	check_ip.check_ip_address(ip)
