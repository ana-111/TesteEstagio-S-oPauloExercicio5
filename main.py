# Função para inverter uma string
def inverter_string(s):
    string_invertida = ''
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

# String de exemplo (pode ser alterada ou ser input do usuário)
string_original = "Exemplo de string"

# Chamando a função e exibindo o resultado
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
