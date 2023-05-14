#Mengimport modul socket dari library python
import socket
#Mendefinisikan variabel ServerName yang menyimpan alamat IP dari server yang digunakan untuk mengakses permintaan HTTP dari client
ServerName = '127.0.0.1'
#Mendefinisikan variabel ServerPort yang menyimpan alamat port yang digunakan web server untuk melayani permintaan HTTP dari client
ServerPort = 1234

#Membuat socket baru
#socket.AF_INET menunjukkan bahwa socket akan menggunakan alamat IPv4
#socket.SOCK_STREAM menunjukkan bahwa socket akan menggunakan protokol TCP
ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Melakukan set option pada socket
#SOL_SOCKET merupakan konstanta yang menandakan bahwa opsi yang diatur berada pada level socket layer
#SO_REUSEADDR memungkinkan socket untuk menggunakan kembali alamat yang sama yang telah digunakan pada koneksi sebelumnya
#Nilai 1 menandakan bahwa opsi tersebut diaktifkan (enable)
ServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#Mengaitkan socket dengan alamat (host dan nomor port) pada jaringan yang akan digunakan untuk menerima permintaan koneksi dari client
ServerSocket.bind((ServerName, ServerPort))

#Mengaktifkan socket server untuk mendengarkan koneksi masuk dari klien
#Nilai 1 menunjukkan jumlah permintaan koneksi yang dapat diterima secara simultan
ServerSocket.listen(1)

#Mencetak nilai variabel ServerPort
print('Listening on port %s ...' % ServerPort)

#Membuat program terus berjalan selama program dijalankan
while True:    
    #Menerima permintaan koneksi dari klien melalui objek ServerSocket dan mengembalikan objek koneksi baru KoneksiKlien dan alamat klien AlamatKlien
    KoneksiKlien, AlamatKlien = ServerSocket.accept()

    #Menerima data dari klien melalui objek KoneksiKlien dan menyimpannya ke variabel req dengan maksimum ukuran data 1024 byte
    req = KoneksiKlien.recv(1024).decode()
    #Mencetak data permintaan dari klien ke konsol
    print(req)
    
    #Membagi data permintaan yang diterima menjadi baris-baris dan menyimpannya ke dalam variabel header
    header = req.split('\n')
    #Mengambil rute dari permintaan yang diterima dengan membagi baris pertama header[0] menjadi beberapa kata dan menyimpan kata kedua ke dalam variabel rute
    rute = header[0].split()[1]
    #Inisialisasi variabel file dengan nilai string kosong
    file = ""
   
    #Memeriksa apakah rute yang diminta adalah "/" (root), jika iya maka file yang akan dikirimkan adalah "fileisi.html"
    if rute == '/':
        file = 'fileisi.html'
    #Jika tidak, maka kode tersebut memeriksa apakah rute adalah "/dian", jika iya maka file yang akan dikirimkan adalah "dian.html"
    elif rute == "/dian" :
        file = "dian.html"
    #Selanjutnya, jika rute adalah "/shasa", maka file yang akan dikirimkan adalah "shasa.html"
    elif rute == "/shasa" :
        file = "shasa.html"
 
    try:
        #Membuka file yang telah ditentukan berdasarkan rute atau path yang diminta oleh klien pada permintaan HTTP
        BukaFile = open(file)
        content = BukaFile.read()
        #Menutup file dengan memanggil fungsi close()
        BukaFile.close()

        #Mengisi variabel respon dengan header HTTP "HTTP/1.0 200 OK\n\n" dan isi file yang telah dibaca sebelumnya
        respon = 'HTTP/1.0 200 OK\n\n' + content
        
    except FileNotFoundError:
        #Membuat error message apabila file tidak ditemukan
        respon = 'HTTP/1.0 404 NOT FOUND\n\n404 NOT FOUND'
    
    #Mengirimkan respon HTTP yang telah dibuat ke klien melalui koneksi yang terbentuk dengan klien saat fungsi accept() dipanggil
    KoneksiKlien.sendall(respon.encode())
    #Menutup socket dan menyelesaikan koneksi antara server dan klien
    KoneksiKlien.close()
