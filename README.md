# SSC0901 - Trabalho 01 - Script de Mapeamento 
Alunos:
- André Bermudes Viana – 10684580
- Antônio Sebastian Fernandes Rabelo - 10797781
- Thiago Daniel Cagnoni de Pauli - 10716629
- Vitor Oliveira Caires - 10748027
- Luíza Pereira Pinto Machado - 7564426

## Requisitos
Para executar o script é necessário ter o python3 instalado, testamos nas versões 3.6.9 e 3.4.3, ambas rodaram sem problemas.
Não existe a necessidade de instalação de bibliotecas adicionais.

## Guia de Utilização
O script possui dois modos de utilização, o modo range e o modo list.

### Modo Range
No modo range o script verifica todas as portas dentro de um range.

Utilização:
```
python3 scan_ports.py -r inicio fim
```
Onde inicio e fim são dois números inteiros, e inicio é menor do que fim.

### Modo List
No modo range o script verifica somente uma lista de portas fornecidas pelo usuário.

Utilização:
```
python3 scan_ports.py -l porta1 porta2 porta3...
```
As portas da lista devem ser passadas separadas por um espaço único.

## Especificando IP
Por padrão o script analisa o localhost, porém é possível escolher o IP para análise através da flag '-ip'.

Utilização:
```
python3 scan_ports.py -ip IP_ALVO -r inicio fim
python3 scan_ports.py -ip IP_ALVO -l porta1 porta2 porta3...
```
Como mostrado acima, essa flag vale tanto para o modo List quanto o modo Range.

## Exemplos
### Exemplo na VM do metasploitable
Comando:
```python3 scan_ports.py -r 10 50```

Saída:
```  
SERVIÇO       PROTOCOLO/PORTA
ftp               tcp/21
ssh               tcp/22
telnet            tcp/23
smtp              tcp/25
```

### Exemplo no Ubuntu 18.04 rodando no WLS2
Comando:
```python3 scan_ports.py -l 22 80 433```

Saída:
```  
Nenhuma porta está aberta!
```

Após a execução do comando iniciei o serviço de ssh.
```sudo service start ssh```

Rodando novamente:
```python3 scan_ports.py -l 22 80 433```

Saída:
```  
SERVIÇO       PROTOCOLO/PORTA
ssh               tcp/22
```
