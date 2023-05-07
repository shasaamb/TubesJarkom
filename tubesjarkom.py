import socket
ServerName = '127.0.0.1'
ServerPort = 1234


ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ServerSocket.bind((ServerName, ServerPort))
ServerSocket.listen(1)
print('Listening on port %s ...' % ServerPort)

while True:    
 
    KoneksiKlien, AlamatKlien = ServerSocket.accept()

    req = KoneksiKlien.recv(1024).decode()
    print(req)
    
    header = req.split('\n')
    rute = header[0].split()[1]
    file = ""
   
    if rute == '/':
        file = 'fileisi1.html'
    elif rute == "/dian" :
        file = "fileisi2.html"
    elif rute == "/shasa" :
        file = "fileisi3.html"
    try:
        BukaFile = open(file)
        content = BukaFile.read()
        BukaFile.close()

        respon = 'HTTP/1.0 200 OK\n\n' + content
    except FileNotFoundError:

        respon = 'HTTP/1.0 404 NOT FOUND\n\n404 NOT FOUND'
    KoneksiKlien.sendall(respon.encode())
    KoneksiKlien.close()
