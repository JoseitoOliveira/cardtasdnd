
import json



link = 'https://raw.githubusercontent.com/JoseitoOliveira/cartasdnd/master/cartas/'
cartas = []
macros = []

with open('nomes.txt', mode='r', encoding='utf8') as f:
    for nome in f.readlines():
        nome = nome.rstrip()
        link_nome = nome.replace(' ', '%20')
        carta = {'nome': nome.replace('.jpg', ''),
                 'link': f'{link}{link_nome}'}
        cartas.append(carta)


for carta in cartas:
    macro = {
        "attributes": {
            "action": f"[{carta['nome']}]({carta['link']})",
            "istokenaction": False,
            "name": carta['nome'],
            "visibleto": ""
        },
        "macrobar": {
            "color": None,
            "name": None
        }
    }
    macros.append(macro)

to_json = {
    "schema_version": 2,
    "macros": macros
}

with open('magias.json', mode='w', encoding='utf8') as f:
    json.dump(to_json, f, ensure_ascii=False)
