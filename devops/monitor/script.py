import socket

def checking(checking_result, f):
    if checking_result == 0:
        f.write("opened\n")
    else:
        f.write("closed\n")


def portstatus():
    open('open_ports.txt', 'w').close()
    f = open('open_ports.txt', 'a')
    #8080
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    location = ("3.66.68.27",8080)
    checking_result = a_socket.connect_ex(location)

    checking(checking_result, f)

    a_socket.close()
    
    #8081
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    location = ("3.66.68.27",8081)
    checking_result = a_socket.connect_ex(location)

    checking(checking_result, f)

    a_socket.close()

    #8082
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    location = ("3.66.68.27",8082)
    checking_result = a_socket.connect_ex(location)

    checking(checking_result, f)

    a_socket.close()

    #8083
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    location = ("3.66.68.27",8083)
    checking_result = a_socket.connect_ex(location)

    checking(checking_result, f)

    a_socket.close()

    #8084
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    location = ("3.66.68.27",8084)
    checking_result = a_socket.connect_ex(location)

    checking(checking_result, f)

    a_socket.close()

    #8085
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    location = ("3.66.68.27",8085)
    checking_result = a_socket.connect_ex(location)

    checking(checking_result, f)

    a_socket.close()

    #8086
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    location = ("3.66.68.27",8086)
    checking_result = a_socket.connect_ex(location)

    checking(checking_result, f)

    a_socket.close()

    f.close()


portstatus()