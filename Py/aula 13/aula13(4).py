import requests

def retorna_response(url):
    response=requests.get(url)
    return response.text

if __name__=="__main__":
    response=retorna_response("https://globallab.org/en/#.Ygw0TcnMI2w")
    print(response)
