import sys
import re



file_name = sys.argv[0]

def read():
    if len(sys.argv) < 2:
        print("wrong number of parameters")
        return

  

    try:
        with open(file_name, "r") as file:
            text = file.read()
        numbers = re.findall(r'\b\w+\b', text)
        sort_parameters(numbers)
        return parameters
    except: FileNotFoundError
    print("The file doesn't exist")



def sort_parameters(parameters):
    a = parameters[0]
    for i in range(1, parameters.length):
        if parameters[i]%a < parameters[i+1]%a:
            aux = parameters[i]
            parameters[i+1] = parameters[i]
            parameters[i] = aux
    try:
        with open(file_name, "w") as file:
            text = file.write(parameters)
    except: FileNotFoundError
    return parameters



if __name__ == '__main__':
    read()