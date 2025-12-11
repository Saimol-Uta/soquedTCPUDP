from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('--- SERVIDOR UDP INICIADO ---')
print("El servidor está listo para recibir datagramas (Sin conexión previa)...")

# Recibe mensaje del cliente
message, clientAddress = serverSocket.recvfrom(2048)
print(f"📦 Datagrama UDP recibido de {clientAddress}: {message.decode()}")

# Convierte la frase a mayúsculas y la envía de vuelta con un mensaje
modifiedMessage = message.decode().upper()
autoResponse = f"Servidor responde (automático): {modifiedMessage}"
serverSocket.sendto(autoResponse.encode(), clientAddress)
print("Respuesta automática enviada:", autoResponse)

# Espera confirmación del cliente
confirmation, clientAddress = serverSocket.recvfrom(2048)
print("Confirmación recibida del cliente:", confirmation.decode())

# El servidor ingresa manualmente una segunda respuesta
manualResponse = input("Ingresa tu respuesta manual al cliente: ")
response = f"Servidor responde (manual): {manualResponse}"
serverSocket.sendto(response.encode(), clientAddress)
print("Respuesta manual enviada:", response)

# Espera confirmación final del cliente
finalConfirmation, clientAddress = serverSocket.recvfrom(2048)
print("Confirmación final del cliente:", finalConfirmation.decode())

# Responde con confirmación final
finalResponse = "Servidor: Confirmación recibida. Comunicación finalizada."
serverSocket.sendto(finalResponse.encode(), clientAddress)
print(finalResponse)

print("🛑 Terminando ejecución del servidor UDP.")
print("(Nota: UDP no mantiene estado de conexión, por lo que este script termina aquí para demostrar el cierre total).")
serverSocket.close()