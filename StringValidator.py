# todos los caracteres son alfanumericos str.isalnum()
# " alfabeticos isalpha()
# " digitos isdigit()
# " caracteres en minuscula islower()
# " mayuscula isupper()
 

string = input()
test = ['alnum','alpha','digit','lower','upper']
dic = {num : False for num in test}
for i in string:
    if i.isalnum():
        dic['alnum'] = True
    if i.isalpha():
        dic['alpha'] = True
    if i.isdigit():
        dic['digit'] = True
    if i.islower():
        dic['lower'] = True
    if i.isupper():
        dic['upper'] = True
        
for m in dic.values():
    print(m)

