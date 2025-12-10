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

        # Pregunta al servidor cómo responder
        choice = input("¿Responder automático (A) o manual (M)? ").strip().upper()
        
        if choice == 'A':
            # Convierte la frase a mayúsculas y la envía de vuelta con un mensaje
            capitalizedSentence = sentence.upper()
            response = f"Servidor responde: {capitalizedSentence}"
        else:
            # El servidor ingresa manualmente la respuesta
            manualResponse = input("Ingresa tu respuesta al cliente: ")
            response = f"Servidor responde: {manualResponse}"
        
        connectionSocket.send(response.encode())
        print("Respuesta enviada al cliente:", response)

        # Espera confirmación del cliente
        confirmation = connectionSocket.recv(1024).decode()
        print("Confirmación del cliente:", confirmation)
        
        # Responde a la confirmación
        finalResponse = "Servidor: Confirmación recibida. Cerrando conexión."
        connectionSocket.send(finalResponse.encode())
        print(finalResponse)
    finally:
        connectionSocket.close()
