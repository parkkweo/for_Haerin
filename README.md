# Overview

This microservice searches and downloads images based on specific keywords.

It communicates via text files.

This microservice is designed to be used with Haerin's To-Do List program, displaying an image upon task completion.

## Communication Contract

### Requesting Data from the Microservice

To request data from the microservice, write the keyword to a file named `request.txt` and send a POST request to the `/search` endpoint.

#### Example Request
1. Write the keyword to `request.txt`:

2. Send a POST request to the microservice:
```
import requests

def call_microservice(keyword):
    # Write the keyword to request.txt
    with open('request.txt', 'w') as file:
        file.write(keyword)
    
    # Call the microservice
    response = requests.post('http://localhost:5000/search')
    print(response.text)
    
    # Read the response from response.txt
    with open('response.txt', 'r') as file:
        result = file.read()
    print(result)

if __name__ == '__main__':
    keyword = 'cat'
    call_microservice(keyword)
```

## Receiving Data from the Microservice

The microservice will write the search result to a file named response.txt.

The content of response.txt will contain either the path to the downloaded image or a message indicating that no image was found.

### Example Response

After sending the request, read the response from response.txt:

Image saved at static/images/success_image.jpg

or

No image found

## UML Sequence Diagram

![image](https://github.com/user-attachments/assets/fa466efe-c37d-4424-b078-fd5fcd95c229)
