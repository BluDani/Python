mensagem = input('Digite algo: ')

print('O tipo primitivo desse valor é', type(mensagem))
print('Só tem espaços?', mensagem.isspace())
print('É um número?', mensagem.isnumeric())
print('É alfabético?', mensagem.isalpha())
print('É alfanumérico?', mensagem.isalnum())
print('Está em maiúsculo?', mensagem.isupper())
print('Está em minúsculo?', mensagem.islower())
print('Está capitalizada?', mensagem.istitle())


