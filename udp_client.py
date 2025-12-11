from socket import *

# Permite introducir la IP del servidor; por defecto usa localhost
serverName = input('IP del servidor (Enter para localhost): ').strip() or 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Enviar mensaje al servidor
message = input('Ingresa una oración en minúsculas: ')
print(f"📤 Enviando datagrama UDP a {serverName}:{serverPort} (Sin handshake)...")
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Esperar respuesta del servidor (automática)
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print("Respuesta del servidor:", modifiedMessage.decode())

# Enviar confirmación al servidor
confirmation = "Mensaje recibido correctamente"
clientSocket.sendto(confirmation.encode(), (serverName, serverPort))

# Recibir respuesta manual del servidor
manualMessage, serverAddress = clientSocket.recvfrom(2048)
print("Respuesta manual del servidor:", manualMessage.decode())

# Enviar confirmación final al servidor
finalConfirmation = "Confirmación final recibida"
clientSocket.sendto(finalConfirmation.encode(), (serverName, serverPort))

# Espera confirmación final del servidor
finalMessage, serverAddress = clientSocket.recvfrom(2048)
print("Respuesta final del servidor:", finalMessage.decode())

clientSocket.close()
