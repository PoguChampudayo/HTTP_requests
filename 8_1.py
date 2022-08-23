import requests

def mightest_super_hero():
    url = ('https://akabab.github.io/superhero-api/api/all.json')
    response = requests.get(url)
    return response.json()
    
if __name__ == '__main__':
    information = mightest_super_hero()
    final_list = {}
    for character in information:
        if character['name'] in ['Hulk', 'Captain America', 'Thanos']:
            final_list[character['name']] = character['powerstats']['intelligence']
    print(max(final_list.items(), key=lambda x: x[1])[0])
