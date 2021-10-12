import socket

import argparse

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

#Função que checa se os dois ports foram passados corretamentes para a função de verificar um range de ports
def required_length():
    class RequiredLength(argparse.Action):
        def __call__(self, parser, args, values, option_string=None):
            if len(values) != 2:
                msg = 'argumento "{f}" requer exatamente dois argumentos'.format(f=self.dest)
                raise argparse.ArgumentTypeError(msg)
            if values[0] > values[1]:
                msg = 'o primeiro argumento de "{f}" deve ser menor que o segundo'.format(f=self.dest)
                raise argparse.ArgumentTypeError(msg)
            setattr(args, self.dest, values)
    return RequiredLength

#Roda se o módulo for rodado direto, e não importado
import read_services
if __name__ == "__main__":
    services = read_services.read_services()

    parser = argparse.ArgumentParser()
    parser.add_argument('-ip', default='127.0.0.1',
    help='ip que terá suas portas escaneadas (DEFAULT="127.0.0.1")')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-l', '--list', type=int, nargs='+',
    help="escaneia todos os ports em uma dada lista. Informe cada elemento da lista separados por espaço após a flag")
    group.add_argument('-r', '--range', type=int, nargs='+', action=required_length(),
    help="escaneia todos os ports entre dois valores dados. Informe os dois valores separados por espaço após a flag")
   
    try:
        args = parser.parse_args()
    except argparse.ArgumentTypeError as err:
        print(err)


    open_ports = []

    if args.list:
        open_ports = check_port_list(args.list, args.ip)
    if args.range:
        open_ports = check_port_range(args.range[0], args.range[1])
    else:
        print('use "-h" para informações de como rodar o script')

    if args.list or args.range:
        if (not open_ports):
            print("Nenhuma porta está aberta!")
        else:
            for open_port in open_ports:
                print(services.get(open_port,
                "{port} - Serviço não encontrado para esse port em /etc/services".format(port=open_port)))
