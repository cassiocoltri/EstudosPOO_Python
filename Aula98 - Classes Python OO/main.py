from pessoa import Pessoa  # Importando a Classe Pessoa criada no outro arquivo.

# p1 e p2 estão sendo instanciandos a partir da Classe Pessoa.

# Recebendo no self:
#            nome / idade:
p1 = Pessoa("Luiz", 29)  # Estou instanciando a var p1 com o molde/Classe Pessoa.
p2 = Pessoa("Pedro", 32)  # Eles aqui estão apenas apontando para endereços deiferentes.

# OBs: Cada "molde" já esta recebendo Nome e idade pq na CLASSE já expecíficamos que vai receber os parâmentros:
# __init__(self, nome, idade, comendo=False, falando=False):

print(p1.nome)

p1.comer("maça")  # falar que esta comendo...
p1.comer("maça")  # aqui vai dizer que já esta comendo...
p1.falar("macacheira")  # vai dizer que não pode falar pq esta comendo.
p1.parar_comer()  # parou de comer.
p1.falar("macacheira")  # agora ele vai falar sobre assunto...
p1.comer("beterraba")  # vai dar erro de não pode comer falando
p1.parar_comer()  # mandado para de comer.
p1.parar_de_falar()  # mandado parrar de falar
p1.falar("gatos")  # mandado falar sobre outro assunto.

# OBs: Caso não mandasse parar de falar, ele entraria no IF de já estar falando sobre alguma coisa
# e não mudaria o assunto.

print("#" * 40)

p2.ano_de_nascimento()
