from socket import *

# Permite introducir la IP del servidor; por defecto usa localhost
serverName = input('IP del servidor (Enter para localhost): ').strip() or 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

print(f"⏳ Intentando establecer conexión TCP (Handshake) con {serverName}:{serverPort}...")
clientSocket.connect((serverName, serverPort))
print("✅ Conexión establecida exitosamente.")

# Enviar frase al servidor
sentence = input('Ingresa una oración en minúsculas: ')
clientSocket.send(sentence.encode())

# Recibir frase modificada del servidor (respuesta automática)
modifiedSentence = clientSocket.recv(1024)
print('Desde el servidor:', modifiedSentence.decode())

# Enviar confirmación al servidor
confirmation = "Mensaje recibido correctamente"
clientSocket.send(confirmation.encode())

# Recibir respuesta manual del servidor
manualMessage = clientSocket.recv(1024)
print('Respuesta manual del servidor:', manualMessage.decode())

# Enviar confirmación final al servidor
finalConfirmation = "Confirmación final recibida"
clientSocket.send(finalConfirmation.encode())

# Recibir respuesta final del servidor
finalMessage = clientSocket.recv(1024)
print('Respuesta final del servidor:', finalMessage.decode())

clientSocket.close()
