import pandas as pd
import app.store as store
from app import charts

def transform():
    id = []
    uid = []
    brand = []
    name = []
    style = []
    hop = []
    yeast = []
    malts = []
    ibu = []
    alcohol = []
    blg = []

    for i in store.get_beer():
        id.append(i['id'])
        uid.append(i['uid'])
        brand.append(i['brand'])
        name.append(i['name'])
        style.append(i['style'])
        hop.append(i['hop'])
        yeast.append(i['yeast'])
        malts.append(i['malts'])
        ibu.append(i['ibu'])
        alcohol.append(i['alcohol'])
        blg.append(i['blg'])
    
    dic = { 'id':id , 'uid':uid , 'brand':brand ,'name':name, 'style':style, 'hop':hop, 'yeast':yeast,
            'malts':malts, 'ibu':ibu, 'alcohol':alcohol, 'blg':blg}
    new = pd.DataFrame(dic)
    return new

def main():
    df = transform()
    print('STATICS OF BEER´S PRODUCCTION')
    print(df.describe())
    print('MAXIM KIND OF BEER')
    print(df.max())
    print('MINIM KIND OF BEER')
    print(df.min())
    
    charts.chart_boxplot(df['ibu'].values)

    charts.chart_scatter(df['alcohol'].values,df['ibu'].values)

if __name__=='__main__':
    main()
