import socket,time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 4712)
start = time.time()
sock.settimeout(2)
try:
    message = "Ping"
    print(f"Sende: {message}")

    sock.sendto(message.encode('utf-8'), server_address)

    data, server = sock.recvfrom(4096)
    end = time.time()
    elapsed = end - start
    print(f"Antwort vom Server: {data.decode('utf-8')}\nAntwort nach {elapsed} Sekunden erhalten")

except socket.timeout:
    print('REQUEST TIMED OUT')

finally:
    print("Client closing")
    sock.close()
