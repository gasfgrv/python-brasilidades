import requests

class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self.cep = cep
        else:
            raise ValueError('CEP inválido!')

    def __str__(self):
        return self.format_cep()

    def cep_eh_valido(self, cep):
        return len(cep) == 8

    def format_cep(self):
        return '{}-{}'.format(self.cep[:5], self.cep[5:])

    def acessa_via_cep(self):
        url = 'https://viacep.com.br/ws/{}/json/'.format(self.cep)
        response = requests.get(url)
        dados = response.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
