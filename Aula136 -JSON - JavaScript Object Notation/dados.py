"""
http://exchangeratesapi.oi/
http://api.exchangeratesapi.io/latest
"""

clientes_dicionarios = {
    1: {
        'nome': 'Luiz',
        'sobranome': 'Miranda',
        'idade': 25,
        'altura': 1.80,
        'peso': 80.53,
    },
    2: {
        'nome': 'Maria',
        'sobranome': 'Oliveira',
        'idade': 52,
        'altura': 1.67,
        'peso': 57,
    },
    3: {
        'nome': 'Pedro',
        'sobrenome': 'Faria',
        'idade': 32,
        'altura': 1.95,
        'peso': 113,
    }
}

clientes_json = """
{
    "1": {
        "nome": "Luiz Ot\u00e1vio",
        "sobranome": "Miranda",
        "idade": 25,
        "altura": 1.80,
        "peso": 80.53
    },
    "2": {
        "nome": "Maria",
        "sobranome": "Oliveira",
        "idade": 52,
        "altura": 1.67,
        "peso": 57
    },
    "3": {
        "nome": "Pedro",
        "sobrenome": "Faria",
        "idade": 32,
        "altura": 1.95,
        "peso": 113
    }
}
"""