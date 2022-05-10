#!/usr/bin/env python
# coding: utf-8

# In[67]:


print('************** Python Calculator **************')
print()
print()
print('1. Soma')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')
print()
opcao = input('Digite sua opção: ')
print()

if int(opcao) == 1:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    soma = int(num1)+int(num2)
    print('A soma dos números é: ' + num1 + ' + ' + num2 + ' = ' + str(soma))
    
elif int(opcao) == 2:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    subt = int(num1)-int(num2)
    print('A subtração dos números é: ' + num1 + ' - ' + num2 + ' = '  + str(subt))


elif int(opcao) == 3:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    mult = int(num1)*int(num2)
    print('A multiplicação dos números é: ' + num1 + ' * ' + num2 + ' = '  + str(mult))


elif int(opcao) == 4:
    num1 = input('Digite o primeiro número: ')
    num2 = input('Digite o segundo número: ')
    div = int(num1)/int(num2)
    print('A divisão dos números é: ' + num1 + ' / ' + num2 + ' = '  + str(div))

else:
    print('Código Invalido')


# In[ ]:





# In[ ]:




