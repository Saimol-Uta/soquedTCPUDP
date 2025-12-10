from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("El servidor está listo para recibir")

# Recibe mensaje del cliente
message, clientAddress = serverSocket.recvfrom(2048)
print(f"Mensaje recibido de {clientAddress}: {message.decode()}")

# Pregunta al servidor cómo responder
choice = input("¿Responder automático (A) o manual (M)? ").strip().upper()

if choice == 'A':
    # Convierte la frase a mayúsculas y la envía de vuelta con un mensaje
    modifiedMessage = message.decode().upper()
    response = f"Servidor responde: {modifiedMessage}"
else:
    # El servidor ingresa manualmente la respuesta
    manualResponse = input("Ingresa tu respuesta al cliente: ")
    response = f"Servidor responde: {manualResponse}"

serverSocket.sendto(response.encode(), clientAddress)
print("Respuesta enviada al cliente:", response)

# Espera confirmación del cliente
confirmation, clientAddress = serverSocket.recvfrom(2048)
print("Confirmación recibida del cliente:", confirmation.decode())

# Responde a la confirmación
finalResponse = "Servidor: Confirmación recibida. Comunicación finalizada."
serverSocket.sendto(finalResponse.encode(), clientAddress)
print(finalResponse)

serverSocket.close()