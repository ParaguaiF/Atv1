nome = str(input("Digite seu nome: "))

nomes = {
    "João Silva": 7.5,
    "Maria Oliveira": 9.0,
    "Carlos Souza": 6.8,
    "Ana Santos": 8.2,
    "Pedro Costa": 5.5,
    "Luiza Pereira": 7.9,
    "Felipe Rocha": 4.3,
    "Juliana Lima": 8.7,
    "Marcos Almeida": 6.0,
    "Tatiane Ferreira": 9.5,
    "Ricardo Gomes": 7.1,
    "Amanda Ribeiro": 8.9,
    "Bruno Martins": 5.8,
    "Camila Castro": 6.5,
    "Daniel Braga": 7.7,
    "Elena Nunes": 9.2,
    "Gustavo Henrique": 4.8,
    "Isabela Fontes": 8.4,
    "Lucas Teixeira": 6.2,
    "Patrícia Andrade": 7.3
}

if nome in nomes:

    print(f'Nome encontrado! {nome}, sua nota foi {nomes[nome]}')

else:
    print('Nome não encontrado')
