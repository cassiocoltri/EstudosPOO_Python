"""
http://rszalski.github.io/magicmethods/

Obs: Metodos mágicos termiando com __xx__ dois underlines sempre.
"""

class A:

    def __new__(cls, *args, **kwargs):
        print("Eu sou o NEW")
        return object.__new__(cls)

    def __init__(self):
        print("Eu sou o INIT")

    def __call__(self, *args, **kwargs):  # <- __call__ faz o obj se comportar como uma função
        pass


a = A()
