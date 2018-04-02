# Projeto-AD

# Projeto realizado por Miguel Almeida 48314, Tiago Gonçalves 48299 e Henrique Peralta 48292
# Grupo ad001

Comando necessario para a execução do servidor (permanece ligado):

	> python lock_server.py <PORTO_ID> <NºRecursos> <Nº máximo de bloqueios permitidos para cada recurso> <Nº máximo permitido de recursos bloqueados num dado> <Tempo Limite>

Comando Necessario para a execução de um pedido do cliente (Envia o pedido, recebe a resposta e depois desliga-se):

	> python lock_client.py <IP> <PORTO_ID> <ID_Client>

Todos os comandos funcionam:
	LOCK <Resource_ID>
	RELEASE <Resource_ID>
	TEST <Resource_ID>
	STATS <Resource_ID>
	STATS-N
	STATS-Y

NOTAS:

- Cada cliente só pode dar lock a um recurso de cada vez e dar release só ao recurso que deu lock.

- O Cliente só se liga ao servidor quando envia o comando, depois desliga-se.

- Aguenta varios clientes

- O Y já é respeitado e não deixa recursos serem Locked se o Y já estiver no limite

- O servidor verifica o K em cada recurso cada vez que surge um pedido, por isso se o recurso já chegou ao K
só irá desactivar quando for feito outro pedido, o pedido não necessita de ser com esse recurso.

- Recursos desactivados não conseguem ser usados, e se enviar um TEST irá dizer que está desactivado, mas tambem
é possivel ver isso pela a terminal do lock_server.py.

- Os pedidos são enviados e recebidos em codigos(10,20,...) mas imprimidos numa versão simples para o cliente,
deixei na mesma o print do objecto para mostrar que são enviados como pedido no enunciado.

- Se um cliente tentar-se ligar a um servidor que não existe, irá esperar até esse estar disponivel.

- Se o utilizador tentar iniciar um servidor com um PORT_ID já em uso, o servidor irá enviar uma mensagem para tentar
com outro PORT_ID.

- Quando testado usei os seguintes valores N = 4, K = 4, Y = 2, T = 100 e 3 Clientes com ID's = 1 , 2 e 3

