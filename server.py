from socket import *

# 서버의 호스트명과 포트 번호 설정
serverName = 'localhost'
serverPort = 8080

def handle_request(request):
    # 요청 메시지를 공백을 기준으로 나누어 메서드, 경로, 버전으로 분리
    method, path, version, _ = request.split(' ', 3)
    
    # 메서드에 따라 적절한 응답 생성
    if method == 'GET':
        if path == '/':
            # GET 메서드와 경로가 '/'인 경우, 정상적이라고 응답
            response = 'HTTP/2.0 200 OK\r\nContent-Type: text/html\r\n\r\nHello, World!'
        else:
            # GET 메서드와 경로가 '/'가 아닌 경우, 클라이언트가 잘못된 경로나 존재하지 않는 파일을 요청했다고 응답
            response = 'HTTP/2.0 404 Not Found\r\nContent-Type: text/html\r\n\r\n404 Page Not Found'
    elif method == 'POST':
        if path == '/login':
            # POST 메서드와 경로가 '/login'인 경우, 정상적이라고 응답
            response = 'HTTP/2.0 200 OK\r\nContent-Type: text/html\r\n\r\nLogin Successful'
        else:
            # POST 메서드와 경로가 '/login'이 아닌 경우, 클라이언트가 잘못된 경로나 존재하지 않는 파일을 요청했다고 응답
            response = 'HTTP/2.0 404 Not Found\r\nContent-Type: text/html\r\n\r\n404 Page Not Found'
    elif method == 'PUT':
        if path == '/update':
            # PUT 메서드와 경로가 '/update'인 경우, 정상적이라고 응답
            response = 'HTTP/2.0 200 OK\r\nContent-Type: text/html\r\n\r\nUpdate Successful'
        else:
            # PUT 메서드와 경로가 '/update'가 아닌 경우, 클라이언트가 잘못된 경로나 존재하지 않는 파일을 요청했다고 응답
            response = 'HTTP/2.0 404 Not Found\r\nContent-Type: text/html\r\n\r\n404 Page Not Found'
    elif method == 'HEAD':
        if path == '/':
            # HEAD 메서드와 경로가 '/'인 경우, 정상적이라고 응답
            response = 'HTTP/2.0 200 OK\r\nContent-Type: text/html\r\n\r\n'
        else:
            # HEAD 메서드와 경로가 '/'가 아닌 경우, 클라이언트가 잘못된 경로나 존재하지 않는 파일을 요청했다고 응답
            response = 'HTTP/2.0 404 Not Found\r\nContent-Type: text/html\r\n\r\n'
    else:
        # 지원하지 않는 메서드인 경우, 메서드 명을 잘못 입력했다고 응답
        response = 'HTTP/2.0 400 Bad Request\r\nContent-Type: text/html\r\n\r\n400 Bad Request'

    # 버전이 'HTTP/2.0'이 아닌 경우, HTTP 버전이 지원되지 않는다고 응답
    if version != 'HTTP/2.0':
        response = 'HTTP/2.0 505 HTTP Version Not Supported\r\nContent-Type: text/html\r\n\r\nHTTP Version Not Supported'
    # response를 return함
    return response

# 서버 소켓 생성 및 연결 대기
serverSocket = socket(AF_INET, SOCK_STREAM)
# 어느 IP든지 클라이언트를 접속받겠다는 의미
serverSocket.bind(('', serverPort))
# 동시에 연결할 수 있는 소켓의 수가 1개
serverSocket.listen(1)

print('The server is ready to receive')

# 서버는 항상 켜져 있어야 함
while True:
    # 클라이언트와 연결된 소켓 수락
    clientSocket, addr = serverSocket.accept()
    while True:
        # 클라이언트로부터 요청 수신
        request = clientSocket.recv(2048).decode()
        if request[0] == '0':
            break

        # 요청을 처리하고 응답 생성
        response = handle_request(request)

        # 응답 전송
        clientSocket.send(response.encode())

    # 클라이언트 소켓 닫기
    clientSocket.close()