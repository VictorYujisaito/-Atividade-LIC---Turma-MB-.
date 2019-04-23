def letras_favoritas(letra,frase):
    nL=len(frase)
    c=0
    for i in range(0,nL):
        if frase[i].lower()==letra:
            c=c+1
    print('Sua letra favorita:',letra)
    print('Uma frase importante:',frase)
    print('Sua letra favorita é a letra',letra.lower(),'e ela aparece',c,'vezes na frase','"',frase,'"')
letra=input('Qual é sua letra favorita:')
frase=input('informe a frase:')
letras_favoritas(letra,frase)
