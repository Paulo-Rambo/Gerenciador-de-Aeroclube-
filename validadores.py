from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

'''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
'''@@@@@@@@@@@               Validação para testar se CPF é válido                @@@@@@@@@@@'''
'''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''

""" 
    try:
        value
    except ValueError:
        raise ValidationError(
            _('Digite apenas números!'),
            params={'value': value},
            code='invalid',
        )

    except IndexError:
        raise ValidationError(
            _('Quantidade errada de números.'),
            params={'value': value},
            code='invalid',
        )
"""

# Checa a quantidade de números do cpf, se estiver errado retorna True (BOLEANO###quantidade_de_numeros)
# Se tem quantidade errada de números coloca quantidade maior de números para nao dar erro de compilação e seta a execução da mensagem de erro para usu


def validate_cpf(value, cpf_repete_num=True, cpf_valida_numeros=True, quantidade_de_numeros=True):                      # value é o número do cpf
    if len(str(value)) == 11:
        quantidade_de_numeros = False

    if quantidade_de_numeros:
        raise ValidationError(
            _('CPF possui quantidade incorreta de números.'),
            params={'value': value},
            code='invalid',
        )

# ve se os números são repetidos, se for retorna True (BOLEANO###cpf_repete_num)
    indice = 1
    value_temp = str(value)
    for num1 in value_temp:
        while indice < len(value_temp):
            if num1 != value_temp[indice]:
                cpf_repete_num = False
                break
            else:
                indice += 1

# checa se os ultimos 2 números correspondem com os outros (BOLEANO###cpf_valida_numeros)
    value_temp = list(value)
    multiplica = 0
    multiplicador1 = 10

    for num in range(9):
        multiplica += multiplicador1 * int(value_temp[num])
        multiplicador1 -= 1
    resto1 = (multiplica * 10) % 11

    multiplica = 0
    multiplicador2 = 11

    for num in range(10):
        multiplica += multiplicador2 * int(value_temp[num])
        multiplicador2 -= 1
    resto2 = (multiplica * 10) % 11

    if resto1 == 10:
        resto1 = 0
    if resto2 == 10:
        resto2 = 0

    if int(value_temp[9]) == resto1 and int(value_temp[10]) == resto2:
        cpf_valida_numeros = False

# Checa a quantidade de números do cpf, se estiver errado retorna True (BOLEANO###quantidade_de_numeros)

    if cpf_repete_num or cpf_valida_numeros:
        raise ValidationError(
            _('CPF inválido.'),
            params={'value': value},
            code='invalid',
        )


'''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''
'''@@@@@@@@@@@        Validação para testar se usuário já tem perfil salvo        @@@@@@@@@@@'''
'''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''

from django.contrib.auth.models import User



'''
def validate_perfil(value):
     if value == 3:                     # variável importada de views(utilizada em function view usuario_view)
        raise ValidationError(
            _('Você já possui cadastro de perfil! Entre em contato com administrador para alterar!.'),
            params={'value': value},
            code='invalid',
        )'''

