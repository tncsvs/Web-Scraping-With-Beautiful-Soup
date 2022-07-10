from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'http://www.listelese.com/istanbul/ecza-depolari/listesi'
r = requests.get(url)
Soup = BeautifulSoup(r.content, 'html5lib')
name = Soup.findAll('div', class_="row s_block_4_s115")
id=0
with open('Eczane.csv','w',encoding='utf-8',newline='') as f :
        thewriter = writer(f)
        header = ['id','depo_name','sehir','semt','adres']
        thewriter.writerow(header)
        treng = str.maketrans("çğıöşüÇİĞÖŞÜ", "cgiosuCIGOSU")
        for i in name:
                depo_name = i.find('a').text
                depo_name = depo_name.strip()
                depo_name = depo_name.replace("\n","")
                depo_name = depo_name.translate(treng)


                sehir = i.find('div', class_='col-md-1 col-xs-6').text
                sehir = sehir.strip()
                sehir = sehir.replace("\n","")
                sehir = sehir.translate(treng)


                semt = i.find('div', class_='col-md-2 col-xs-6').text
                semt = semt.strip()
                semt = semt.replace("\n", "")
                semt = semt.translate(treng)


                adres = i.find('address').text
                adres = adres.strip()
                adres = adres.replace("\n", "")
                adres = adres.translate(treng)

                id += 1
                data = [id,depo_name,sehir,semt,adres]
                thewriter.writerow(data)










