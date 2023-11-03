#Lab 6 


def ex1():
    import http.client
    from urllib import response
    conn = http.client.HTTPConnection("www.python.org")
    conn.request("GET","/")
    response= conn.getresponse()
    print(type(response))
    print(response.status, response.reason)
    data=response.read()
    print(data)

def ex2():
    import http.client
    from urllib import response
    conn = http.client.HTTPConnection("www.python.org")
    conn.request("GET","/")
    response = conn.getresponse()
    headers = response.getheaders()
    print(headers)
    data=response.read()
    print(data)
    print(len(data))

def ex3():
    import urllib.request
    import urllib.parse
    from urllib import response
    url="http://www.python.org"
    response = urllib.request.urlopen("http://www.python.org",timeout=30)
    content = response.read(600)
    print(content)
    

def ex4():
    import urllib.request
    import urllib.parse
    from urllib import response
    url="http://www.python.org"
    response = urllib.request.urlopen("http://www.python.org",timeout=30)
    content = response.read(600).decode("utf-8")
    print(content)

def ex5():
    import urllib.request
    import urllib.parse
    from urllib import response
    response = urllib.request.urlopen("http://www.google.com",timeout=30)
    content = response.read().decode("utf-8")
    print(content)

def ex6():
    pass