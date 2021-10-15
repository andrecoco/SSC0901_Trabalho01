# Classe do serviço.
# Guarda a porta e os protocolos nas camadas de aplicação e de serviço.
class Service:
    def __init__(self, port, transport_protocol, application_protocol):
        self.port = port
        self.transport_protocol = transport_protocol
        self.application_protocol = application_protocol

    def __str__(self) -> str:
        return self.application_protocol + (21 - len(self.application_protocol))*" " + self.transport_protocol + "/" + self.port

def read_services():
    '''
    Lê o arquivo /etc/services para identificar serviços abertos nas camadas de aplicação 
    e de transporte e suas respectivas portas.

    Retorno: retorna um dicionário de elementos da classe Service cujas chaves são as portas
    em que os serviços estão abertos.
    '''

    # Lê o arquivo, separando por linha e filtrando linhas vazias ou de comentários
    f = open("/etc/services", "r")
    lines = [x for x in f.read().split("\n") if x and x[0] != '\n' and x[0] != '#']
    f.close()

    # Separa as colunas por tabs e limpa 
    service_strings = []
    for line in lines:
        service_string = [x for x in line.split("\t") if x]
        service_strings.append(service_string)

    # Algumas linhas têm suas colunas separadas por espaços, não tab
    for index, service_string in enumerate(service_strings):
        if len(service_string[0].split()) > 1:
            service_strings[index] = service_string[0].split()

    # Transforma as strings divididas em objetos da classe Service
    services = {}
    for service_string in service_strings:
        if('udp' in service_string[1]):
            continue
        application_protocol = service_string[0]
        port, transport_protocol = service_string[1].split('/')
        
        service = Service(port, transport_protocol, application_protocol)
        services[int(port)] = service

    return services


# Roda se o módulo for rodado diretamente, não importado
if __name__ == "__main__":
    services = read_services()
    for key, value in services.items():
        print(value)
