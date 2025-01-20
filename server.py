import socket
import select

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 4712))

print("UDP Server läuft auf Port 4712")

socket_list = [sock]

while True:
    try:
        read_sockets,_,_ = select.select(socket_list,[],[])

        for socket in read_sockets:
            if socket == sock:
                data, addr = sock.recvfrom(4096)
                decoded_data = data.decode('utf-8')
                print(f"Empfangen von {addr}: {decoded_data}")


                response_message = "Pong"
                response = response_message.encode('utf-8')
                sock.sendto(response, addr)

    except KeyboardInterrupt:
        print("\nServer wird geschlossen.")
        break
    except Exception as e:
        print(f"Fehler: {e}")

sock.close()
