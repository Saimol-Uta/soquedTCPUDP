from socket import *

serverName = 'localhost'  
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Enviar frase al servidor
sentence = input('Ingresa una oración en minúsculas: ')
clientSocket.send(sentence.encode())

# Recibir frase modificada del servidor
modifiedSentence = clientSocket.recv(1024)
print('Desde el servidor:', modifiedSentence.decode())

# Enviar confirmación al servidor
confirmation = "Mensaje recibido correctamente"
clientSocket.send(confirmation.encode())

# Recibir respuesta final del servidor
finalMessage = clientSocket.recv(1024)
print('Respuesta final del servidor:', finalMessage.decode())

clientSocket.close()
