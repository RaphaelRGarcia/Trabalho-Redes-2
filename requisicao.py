import requests

url = 'https://youtube.com'
i=0
while(i<1000):
    response = requests.get(url)
    print(response.status_code)  # Código de status da resposta
    print(i)
    i+=1