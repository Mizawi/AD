# Projeto-AD

# Projeto realizado por Miguel Almeida 48314, Tiago Gonçalves 48299 e Henrique Peralta 48292

Comando necessario para a execução do servidor (permanece ligado):

	> python lock_server <PORTO_ID> <NºRecursos> <Nº máximo de bloqueios permitidos para cada recurso> <Nº máximo permitido de recursos bloqueados num dado> <Tempo Limite>

Comando Necessario para a execução de um pedido do cliente (Desliga-se após envio do pedido e recepção da resposta):

	> python lock_client <IP> <PORTO_ID> <ID_Client>

Todos os comandos funcionam:
	LOCK <Resource_ID>
	RELEASE <Resource_ID>
	TEST <Resource_ID>
	STATS <Resource_ID>
	STATS-N
	STATS-Y

NOTAS:

O servidor verifica o K em cada recurso cada vez que surge um pedido, por isso se o recurso já chegou ao K
só irá desactivar quando for feito outro pedido, o pedido não necessita de ser com esse recurso.

Recursos desactivados não conseguem ser usados, e se enviar um TEST irá dizer que está desactivado, mas tambem é possivel
ver isso pela a terminal do lock_server.py.

Os pedidos são enviados e recebidos em codigos(10,20,...) mas imprimidos numa versão simples para o cliente.
Deixei na mesma o print do objecto para mostrar que são enviados como pedido no enunciado.

Se um cliente tentar-se ligar a um servidor que não existe, irá esperar até esse estar disponivel.
Se um client enviar um Quit para o servidor, o servidor irá avisar o utilizador, e vai esperar por uma nova ligação.
Se o utilizador tentar iniciar um servidor com um PORT_ID já em uso, o servidor irá enviar uma mensagem para tentar
com outro PORT_ID.