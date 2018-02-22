# Projeto-AD

# Projeto realizado por Miguel Almeida 48314, Tiago Gon�alves 48299 e Henrique Peralta 48292

Comando necessario para a execu��o do servidor (permanece ligado):
	
	> python lock_server <PORTO_ID> <N�Recursos> <N� Maximo de Utilizadores no mesmo recurso> <Tempo Limite>

Comando Necessario para a execu��o de um pedido do cliente (Desliga-se ap�s envio do pedido e recep��o da resposta):
	
	> python lock_client <IP> <PORTO_ID> <ID_Client

Todos os comandos funcionam:
	Lock <Resource_ID>
	Release <Resource_ID>
	Stats <Resource_ID>
	Test <Resource_ID>
	Stats_Y
	Stats_N

Cada vez que � enviado um pedido ao servidor, o servidor imprime o estado dos recursos.