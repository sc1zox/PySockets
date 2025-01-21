import concurrent.futures
import socket

def handle_client(sock, addr):
    try:
        data, _ = sock.recvfrom(4096)
        decoded_data = data.decode('utf-8')
        print(f"Empfangen von {addr}: {decoded_data}")

        response_message = "Pong"
        response = response_message.encode('utf-8')
        sock.sendto(response, addr)
    except Exception as e:
        print(f"Fehler bei der Verarbeitung der Anfrage von {addr}: {e}")

def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 4712))
    print("UDP Server läuft auf Port 4712")

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        while True:
            try:
                data, addr = sock.recvfrom(4096)
                executor.submit(handle_client, sock, addr)
            except KeyboardInterrupt:
                print("\nServer wird geschlossen.")
                break
            except Exception as e:
                print(f"Fehler: {e}")

    sock.close()

if __name__ == "__main__":
    start_server()
