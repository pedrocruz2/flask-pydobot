import json

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
ponto1 = (0,4,5) #VERTICE SUPERIOR ESQUERDO DA BANDEJA 
ponto2 = (5,4,5) #VERTICE SUPERIOR DIREITO DA BANDEJA
ponto3 = (0,0,5) #VERTICE INFERIOR ESQUERDO DA BANDEJA
ponto4 = (5,0,5)#VERTICE INFERIOR DIREITO DA BANDEJA
l = ponto2[0] - ponto1[0] #COMPRIMENTO DA BANDEJA 
h = ponto1[1] - ponto3[1] #ALTURA DA BANDEJA
print(h)
print(l)
layoutInput = input('Insira layout aqui: ')
if armazenar_layout_por_id(layoutInput) is not None:
    layout = armazenar_layout_por_id(layoutInput)
    print(layout['remedios'])
    count = len(layout['remedios'])
    x = ponto1[0]
    y = ponto1[1]
    for i in layout['remedios']:
        print(f"remedio: {i}")
        print(count%layout['nc'])
        if count == len(layout['remedios']): # "Caso base" entre MUITAS ASPAS
            x += l/(layout['nc'] *2)
            base = x
            y -= h/(layout['nl'] * 2)
            print('primeira operação')
            print(f'coordenadas:{(x,y)}')
            count -= 1 
            continue
        if count%layout['nc'] ==0:
            print()
            x = base
            y -= h/layout['nl']
            print('caso troca de linha')
            print(f'coordenadas:{(x,y)}')
            count -= 1 
            continue
        x += l/layout['nc']
        print('caso normal')
        print(f'coordenadas:{(x,y)}')
        count -= 1 
else:
    print('Layout não identificado')



