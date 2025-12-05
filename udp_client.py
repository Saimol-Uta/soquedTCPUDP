from socket import *

serverName = 'localhost'  # o la IP del servidor
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Enviar mensaje al servidor
message = input('Ingresa una oración en minúsculas: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Esperar respuesta del servidor
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print("Respuesta del servidor:", modifiedMessage.decode())

# Enviar confirmación al servidor
confirmation = "Mensaje recibido correctamente"
clientSocket.sendto(confirmation.encode(), (serverName, serverPort))

# Recibir respuesta final del servidor
finalMessage, serverAddress = clientSocket.recvfrom(2048)
print("Respuesta final del servidor:", finalMessage.decode())

clientSocket.close()
