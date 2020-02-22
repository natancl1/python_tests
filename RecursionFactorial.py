#Factorial of a number using recursive function

def myFactorial(x):
    if x == 1 :
        return 1
    else :
        return x * myFactorial(x - 1)

print('\033[1;33m=-\033[m'*25)
print('\033[1;34m{:^50}\033[m'.format('FACTORIAL CALCULATOR'))
print('\033[1;33m=-\033[m'*25)

number = int(input('\033[1;33m|\033[m \033[1mEnter a \033[1;34mnumber\033[m \033[1mto calculate your \033[1;34mfactorial:\033[m '))
numberfactorial = myFactorial(number)
print('\033[1;33m|\033[m \033[1mFactorial of \033[1;31m{}\033[m \033[1mis equal to \033[1;32m{}\033[m'.format(number, numberfactorial))

print('\033[1;33m=-\033[m'*25)
