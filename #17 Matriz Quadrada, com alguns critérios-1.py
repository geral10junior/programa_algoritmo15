def criar_matriz(tamanho):
  if tamanho == 0 :
    return 
  else :
    matriz = []
    for i in range(1,(N+1)):
          lista_temporaria = []
          contador = i
          for j in range(N):
              lista_temporaria.append(abs(contador))
              if(contador == 1):
                  contador -= 3
              else:
                  contador -= 1
          matriz.append(lista_temporaria)
    return matriz
cond = True
while cond:
    N = int(input())
    matriz = criar_matriz(N)
    if matriz :

      for i in range(N):
          texto = ''
          for j in range(N):
              texto += " %3d" %matriz[i][j]
          print(texto[1:])
      print("")
    else:
      cond = False