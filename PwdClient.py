import socket
import pickle
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 4211))

first_time_connection = True

def validate_password(password_dictionary):
    is_valid = False
    file = pickle.dumps(password_dictionary)  # encode dictionary + characteristics to validate
    client.sendall(file)      # send data
    validation_result = client.recv(1024)    # reviece result of validation from microservice
    # print(validation_result.decode("utf-8"))  # print result of validation
    if validation_result.decode("utf-8") == 'True':
        is_valid = True
    return is_valid
    # return bool(validation_result.decode("utf-8"))

