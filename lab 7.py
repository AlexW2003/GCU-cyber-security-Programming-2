
def ex1():

    import http.client
    from urllib import response
    conn = http.client.HTTPSConnection("www.google.com")
    conn.request("GET","/")
    response = conn.getresponse()
    headers = response.getheaders()
    #print(headers)
    data=response.read().decode("utf-8")
    print(data)

def ex2():
    
    import requests

    response = requests.get('https://postmanecho.com/get')
    print(response.content.decode("utf-8"))
    
    
def ex3():
    import requests
    responce = requests.post(url="https://postman-echo.com/post", data={'name': 'ABC','email':'xyz@gmail.com'})
    print(responce.content.decode("utf-8"))
    responce.close()

def ex4():
    import requests
    
    responce = requests.put(url="https://postman-echo.com/put", data={'name': 'ABC','email':'xyz@gmail.com'})
    print(responce.content.decode("utf-8"))
    print("done")

#question 5 ans put requests are idempotent

def ex6():
    import requests
    from requests.auth import HTTPBasicAuth

    response =requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    print(response.content.decode("utf-8"))

def ex7():
    import requests
    from requests.auth import HTTPBasicAuth

    response = requests.get('https://httpbin.org/basic-auth/admin/admin123', auth=('admin', 'admin123'))
    print(response.content.decode("utf-8"))

ex7()

