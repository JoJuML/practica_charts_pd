import requests as rq

def get_beer():
    get = rq.get('https://random-data-api.com/api/beer/random_beer?size=100&is_json=true')

    texto = get.json()
    for i in texto:
        i['blg'] = float(i['blg'].replace('°Blg','')) # the Balling scale corresponding to the percentage of sugars in the solution
        i['alcohol'] = float(i['alcohol'].replace('%','')) # level of alcohol in porcentage
        i['ibu'] = int(i['ibu'].replace(' IBU','')) #“International Bittering Unit,”
        i['id'] = str(i['id'])
    return texto
     