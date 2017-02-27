import requests, bs4 ,re


def GetTeams():
    base = "http://www.basquetcatala.cat/clubs/pag"
    add = "/?pernom=&perprovincia="
    equips = {}
    for i in range(1,17):
        if i == 1:
            web = requests.get("http://www.basquetcatala.cat/clubs")
            web.raise_for_status()
            web = bs4.BeautifulSoup(web.text,"html.parser")
            lista = web.select('div #llista-clubs ul li a')
            for i in range(0,len(lista)):
                equips[lista[i].getText()] = lista[i].get("href")
        else:
            web = requests.get(base+str(i)+add)
            web.raise_for_status()
            web = bs4.BeautifulSoup(web.text,"html.parser")
            lista = web.select('div #llista-clubs ul li a')
            for i in range(0,len(lista)):
                equips[lista[i].getText()] = lista[i].get("href")
    print("done")
    return equips

def SearchTeam(equips):
    filtre = []
    ent = str(input().upper())
    for key ,val in equips.items():
        if ent in str(key):
            filtre.append(key)
    for i in range(0,len(filtre)):
        print(str(i+1)+ "-"+filtre[i])
    choice = int(input())-1
    if filtre[choice] in equips:
        url = equips[filtre[choice]]
        return url
        
def ShowCategory(team):
    url = "http://www.basquetcatala.cat" + team
    print(url)
    web = requests.get(url)
    web.raise_for_status()
    web = bs4.BeautifulSoup(web.text,"html.parser")
    cat = web.select('div .equips-llista ')
    print(cat)
    #cat = web.select('div .equips-llista h4')
    #for i in range(0,len(cat)):
     #   print(str(i+1)+"-"+cat[i].getText())

if __name__ == "__main__":
    teams = GetTeams()
    team = SearchTeam(teams)
    ShowCategory(team)
