from socket import *

# 서버의 호스트명과 포트 번호 설정
serverName = 'localhost'
serverPort = 8080

def send_request(Socket, sentence):
    # 요청 메시지 구성
    request = f'{sentence} \r\nHost: {serverName}\r\n\r\n'
    # 요청 메시지를 바이트로 변환하여 서버로 전송
    Socket.send(request.encode())

def receive_response(Socket):
    # 서버로부터 응답 받기, 읽어오는 크기가 2048byte
    response = Socket.recv(2048)
    # 응답을 문자열로 디코딩하여 출력
    print('From Server:', response.decode())

# 클라이언트 소켓 생성 및 서버에 연결
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# handshake 시작
while True:
    # 사용자로부터 입력 받기
    sentence = input()

    # 요청 전송
    send_request(clientSocket, sentence)

    # 입력이 '0'인 경우, handshake 종료
    if sentence == '0':
        break

    # 응답 수신 및 출력
    receive_response(clientSocket)

# 클라이언트 소켓 닫기
clientSocket.close()
