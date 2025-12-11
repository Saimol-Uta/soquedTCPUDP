# Análisis Práctico: TCP vs UDP

Este documento explica las diferencias fundamentales entre los protocolos TCP y UDP basándose en el comportamiento del código implementado en este proyecto.

## 🧐 ¿Representa este código la realidad?

**Sí.** El código captura la esencia de ambos protocolos:

*   **TCP** se muestra como una **conversación telefónica**: Hay que marcar (`connect`), alguien tiene que descolgar (`accept`), y la línea se mantiene abierta hasta que uno cuelga.
*   **UDP** se muestra como enviar **cartas por correo**: Simplemente envías el mensaje a una dirección (`sendto`). No sabes si llegaron a menos que te respondan.

## ⚡ La Diferencia Más Significativa (En este código)

Como notaste al ejecutar los programas, el comportamiento del servidor es radicalmente distinto:

### 1. El Servidor TCP (Persistente)
> *"Sigue buscando cliente"*

En `tcp_server.py`, verás un bucle `while True`. Esto es posible y necesario porque TCP distingue entre:
1.  **El socket de bienvenida (`serverSocket`):** Siempre está escuchando (`listen`).
2.  **El socket de conexión (`connectionSocket`):** Se crea uno nuevo y exclusivo para cada cliente.

Cuando un cliente termina, el servidor cierra ese socket específico, pero **el servidor principal sigue vivo** esperando al siguiente.

### 2. El Servidor UDP (Transaccional)
> *"Cierra la comunicación por completo"*

En `udp_server.py`, el código se ejecuta linealmente y termina.
*   **No hay `listen()` ni `accept()`**: El servidor no "acepta" una conexión, simplemente espera recibir datos.
*   **No hay socket dedicado**: Usa el mismo socket para todo.
*   **Cierre inmediato**: Al no haber un estado de "conexión establecida", en este código el servidor procesa el flujo y se apaga (`serverSocket.close()`). Para que fuera eterno, tendríamos que forzar un bucle manualmente, ya que el protocolo no gestiona "sesiones".

## 💻 Diferencias en el Código (Sintaxis)

### TCP (Orientado a Conexión)
Requiere 3 pasos obligatorios antes de enviar datos (Handshake):

```python
# SERVIDOR
serverSocket = socket(AF_INET, SOCK_STREAM) # STREAM = Flujo continuo
serverSocket.listen(1)                      # Escuchar
connectionSocket, addr = serverSocket.accept() # Aceptar conexión

# CLIENTE
clientSocket.connect((serverName, serverPort)) # Conectar explícitamente