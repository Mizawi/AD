# Projeto-AD

# Projeto realizado por Miguel Almeida 48314, Tiago Goncalves 48299 e Henrique Peralta 48292

Comando necessario para a execucao do servidor (permanece ligado):
	
	> python lock_server.py <PORTO_ID> <N Recursos> <N  Maximo de Utilizadores no mesmo recurso> <Tempo Limite>

Comando Necessario para a execucao de um pedido do cliente (Desliga-se apos envio do pedido e recepcao da resposta):
	
	> python lock_client.py <IP> <PORTO_ID> <ID_Client>

Todos os comandos funcionam:
	Lock <Resource_ID>
	Release <Resource_ID>
	Stats <Resource_ID>
	Test <Resource_ID>
	Stats_Y
	Stats_N

Cada vez que e enviado um pedido ao servidor, o servidor imprime o estado dos recursos.