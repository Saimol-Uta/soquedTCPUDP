from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('El servidor está listo para recibir')

while True:
    connectionSocket, addr = serverSocket.accept()
    try:
        # Recibe la frase del cliente
        sentence = connectionSocket.recv(1024).decode()
        print("Mensaje recibido del cliente:", sentence)

        # Convierte la frase a mayúsculas y la envía de vuelta con un mensaje
        capitalizedSentence = sentence.upper()
        autoResponse = f"Servidor responde (automático): {capitalizedSentence}"
        connectionSocket.send(autoResponse.encode())
        print("Respuesta automática enviada:", autoResponse)
        
        # Espera confirmación del cliente sobre la respuesta automática
        confirmation1 = connectionSocket.recv(1024).decode()
        print("Confirmación 1 del cliente:", confirmation1)
        
        # El servidor ingresa manualmente una segunda respuesta
        manualResponse = input("Ingresa tu respuesta manual al cliente: ")
        response = f"Servidor responde (manual): {manualResponse}"
        connectionSocket.send(response.encode())
        print("Respuesta manual enviada:", response)

        # Espera confirmación del cliente
        confirmation = connectionSocket.recv(1024).decode()
        print("Confirmación del cliente:", confirmation)
        
        # Responde a la confirmación
        finalResponse = "Servidor: Confirmación recibida. Cerrando conexión."
        connectionSocket.send(finalResponse.encode())
        print(finalResponse)
    finally:
        connectionSocket.close()
