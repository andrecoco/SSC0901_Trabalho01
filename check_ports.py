import socket

def _check_port(port, IP):
    '''
    Testa se a porta passada por argumento está aberta no IP alvo.

    Retorna um booleano que indica se a porta está aberta ou não.
    '''
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.settimeout(0.1)
    code = soc.connect_ex((IP, port))
    soc.close()
    if (code == 0):
        return True
    else:
        return False
    

def check_port_range(begin, end, IP = "0.0.0.0"):
    '''
    Testa se as portas entre begin e end (inclusas) estão abertas no IP alvo.

    Retorna uma lista de todas as portas abertas.
    '''
    result = []
    for port in range(begin, end + 1):
        if(_check_port(port,IP)):
            result.append(port)
    
    return result

def check_port_list(ports, IP = "0.0.0.0"):
    '''
    Testa se as portas na lista passada por argumento estão abertas no IP alvo.

    Retorna uma lista de todas as portas abertas.
    '''
    result = []
    for port in ports:
        if(_check_port(port,IP)):
            result.append(port)
    
    return result

#Roda se o módulo for rodado direto, e não importado
import read_services
if __name__ == "__main__":
    services = read_services.read_services()
    open_ports = check_port_range(1, 50) #testa as 50 primeiras portas do localhost
    if (not open_ports):
        print("Nenhuma porta está aberta!")
    else:
        for open_port in open_ports:
            print(services[open_port])
