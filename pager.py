import sys
import telnetlib
import time
import os

tn_ip = "10.2.0.187"  # IP do Transmissor
tn_port = "3700"     # Porta comunicação telnet
# Script pradão para login
login = "<Login user='geoffrey' passwd='mypassword' services='NetPage'/>"

# Define a mensagem que será apresentada no display do pager, de acordo com o 2º parâmetro passado
def mens():
    if len(sys.argv) < 2:  
        # não havendo parâmetros passados
        sys.exit()
    elif sys.argv[2] == '1' or sys.argv[2] == 1:
        return 'PLATAFORMA E EXPEDICAO COM VEICULO'
    elif sys.argv[2] == '2' or sys.argv[2] == 2:
        return 'EXPEDICAO COM VEICULO'
    elif sys.argv[2] == '3' or sys.argv[2] == 3:
        return 'DOCUMENTO LIBERADO PORTARIA'
    elif sys.argv[2] == '4' or sys.argv[2] == 4:
        return 'PORTARIA SEM VEICULO'
    elif sys.argv[2] == '5' or sys.argv[2] == 5:
        return 'PLATAFORMA E PRACA DE MINERIO'
    elif sys.argv[2] == '6' or sys.argv[2] == 6:
        return 'EXPEDICAO SEM VEICULO'
    elif sys.argv[2] == '7' or sys.argv[2] == 7:
        return 'ENTRADA LIBERADA DESCARREGAR'
    elif sys.argv[2] == '8' or sys.argv[2] == 8:
        return 'PESAGEM LIBERADA'
    elif sys.argv[2] == '9' or sys.argv[2] == 9:
        return 'ENTRADA LIBERADA CARREGAR'

def telnet():
    tn = telnetlib.Telnet(tn_ip, tn_port, 15)
    tn.set_debuglevel(100)
    tn.read_until(b'>', 10)
    tn.write(login.encode('utf-8'))
    tn.write(b'\n')
    tn.read_until(b'>', 10)
    tn.write(chamada.encode('utf-8'))
    tn.write(b'\n')
    tn.read_until(b'>', 10)
    time.sleep(2)
    retorno = tn.read_until(b'>', 10)
    tn.close()

    file = open(sys.argv[1] + ".txt", "w")
    file.write(retorno.decode('utf-8'))
    file.close()


mensagem = mens()

# Script para chamada do pager
chamada = "<PageRequest id='1'> <Pager Type='AlphaCoaster' ID='" + \
    sys.argv[1] + "' power='5' /> <Message> " + \
    mensagem + " </Message> </PageRequest>"

# função para escrita e leitura telnet
telnet()

# para criar executável use o com comando no terminal -> cxfreeze -c pager.py
# o executável estará na pasta 'dist'
