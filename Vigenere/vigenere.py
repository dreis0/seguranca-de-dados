chave = 'chave'
mensagem = 'testedacifravigenere'

alfabeto = ([chr(i) for i in range(127)])[32:126]

cifra = ''
for i in range(len(mensagem)):
    caracMensagem = mensagem[i]
    caracChave = chave[i % len(chave)]
    cifra += alfabeto[(alfabeto.index(caracMensagem) + alfabeto.index(caracChave)) % len(alfabeto)]

print('Mensagem criptografada: ' + cifra)

decript = ''
for i in range(len(cifra)):
    caracCifra = cifra[i]
    caracChave = chave[i % len(chave)]
    decript += alfabeto[(alfabeto.index(caracCifra) - alfabeto.index(caracChave)) % len(alfabeto)]

print('Mensagem descriptografada: ' + decript)