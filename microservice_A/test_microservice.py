import requests

def call_microservice(keyword):
    with open('request.txt', 'w') as file:
        file.write(keyword)
    
    response = requests.post('http://localhost:5000/search')
    print(response.text)
    
    with open('response.txt', 'r') as file:
        result = file.read()
    print(result)

if __name__ == '__main__':
    keyword = 'success'
    call_microservice(keyword)