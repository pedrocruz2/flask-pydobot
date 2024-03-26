import json
import requests
# Carrega os dados JSON a partir de um arquivo
def carregar_dados():
    with open('layouts.json', 'r') as file:
        dados = json.load(file)
    return dados

# Percorre cada layout e imprime as informações
def percorrer_layouts():
    dados = carregar_dados()
    for layout in dados['layouts']:
        print(f"ID: {layout['id']}, Número de Colunas: {layout['nc']}, Número de Linhas: {layout['nl']}, Remédios: {', '.join(layout['remedios'])}")

# Armazena apenas o layout com o ID especificado
def armazenar_layout_por_id(id_especificado):
    dados = carregar_dados()
    layout_especificado = next((layout for layout in dados['layouts'] if layout['id'] == id_especificado), None)
    if layout_especificado is not None:
        with open(f'layout_{id_especificado}.json', 'w') as file:
            json.dump(layout_especificado, file, indent=4)
        return layout_especificado
    else:
        return None
    
ponto1 = (182.11688232421875,-338.3886413574219,15.28591251373291) #VERTICE SUPERIOR ESQUERDO DA BANDEJA 
ponto2 = (-82.36273956298828,-343.5843811035156,9.381065368652344) #VERTICE SUPERIOR DIREITO DA BANDEJA
ponto3 = (188.03305053710938,-166.6496124267578,10.483986854553223) #VERTICE INFERIOR ESQUERDO DA BANDEJA
ponto4 = (-74.89086151123047,-166.2255096435547,13.807846069335938)#VERTICE INFERIOR DIREITO DA BANDEJA
l = ponto2[0] - ponto1[0] #COMPRIMENTO DA BANDEJA 
h = ponto1[1] - ponto3[1] #ALTURA DA BANDEJA
print(h)
print(l)
base_url = 'http://127.0.0.1:5000/move'
layoutInput = input('Insira layout aqui: ')
if armazenar_layout_por_id(layoutInput) is not None:
    layout = armazenar_layout_por_id(layoutInput)
    print(layout['remedios'])
    count = len(layout['remedios'])
    x = ponto1[0]
    y = ponto1[1]
    z = 15.28591251373291
    for i in layout['remedios']:
        print(f"remedio: {i}")
        print(count%layout['nc'])
        if count == len(layout['remedios']): # "Caso base" entre MUITAS ASPAS
            x += l/(layout['nc'] *2)
            base = x
            y -= h/(layout['nl'] * 2)
            print('primeira operação')
            print(f'coordenadas:{(x,y)}')
            obj = {"xaxis": x,
                   "yaxis": y,
                   "zaxis": z}
            requests.post(base_url,json = obj)
            count -= 1

            continue
        if count%layout['nc'] ==0:
            print()
            x = base
            y -= h/layout['nl']
            print('caso troca de linha')
            print(f'coordenadas:{(x,y)}')
            obj = {"xaxis": x,
                   "yaxis": y,
                   "zaxis": z}
            requests.post(base_url,json = obj)
            count -= 1 
            continue
        x += l/layout['nc']
        print('caso normal')
        print(f'coordenadas:{(x,y)}')
        obj = {"xaxis": x,
               "yaxis": y,
               "zaxis": z}
        requests.post(base_url,json = obj)
        count -= 1 
else:
    print('Layout não identificado')



