import socket
import time
import select

def run_client(server_address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2)

    message = "Ping"
    print(f"Sende: {message} an {server_address}")

    sock.sendto(message.encode('utf-8'), server_address)
    return sock

server_address = ('127.0.0.1', 4712)

sockets = []
responses = {}


for i in range(5):
    sock = run_client(server_address)
    sockets.append(sock)
    responses[sock] = {'start': time.time()}

print("Warte auf Antworten von Servern...")


while sockets:

    readable, _, _ = select.select(sockets, [], [], 2)

    for sock in readable:
        try:
            data, server = sock.recvfrom(4096)
            end = time.time()
            elapsed = end - responses[sock]['start']
            print(f"Antwort vom Server: {data.decode('utf-8')}\nAntwort nach {elapsed:.4f} Sekunden erhalten")
            sockets.remove(sock)
            sock.close()
        except socket.timeout:
            print(f"REQUEST TIMED OUT für {sock.getpeername()}")
            sockets.remove(sock)
            sock.close()

print("Alle Clients haben ihre Anfragen abgeschlossen.")
