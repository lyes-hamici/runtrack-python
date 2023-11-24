liste=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for x in range(len(liste)):    
    liste.append(liste[x])
message = input('Entrez votre message a coder : ')
clé = int(input('Entrez votre clé ( entre 1 et 25 ) : '))  



def chiffrage_lettre(lettre,liste,clé): #Coder le messagr en choissient la clé de cryptage
    for i in range(len(liste)):
        if lettre==' ':     
            return ' '
        elif liste[i]==lettre:
            return str(liste[i+clé])
    return '?'  
message_chiffré = str()
for lettre in message:
    message_chiffré += chiffrage_lettre(lettre,liste,clé)

print("--------------------------")

print("Message Coder :",message_chiffré)

print("--------------------------")

def message_a_décodé(message_codé,clé): #Décoder le code en ayant la clé de cryptage
 liste=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  
message_codé = input("rentrez votre message codé : ")
clé = int(input("rentrez votre clé : "))
message = [(ord(i)-clé) for i in message_codé]
message_décodé = [chr(i) for i in message]
final = "".join(message_décodé)

print("--------------------------")
print("Message décoder :",final)
print("--------------------------")

     
    
    

def decode_cesar_force_brute(phrase): #Brut force le code cesar
    for x in range(0,27):
        result = ""
        alpha = "abcdefghijklmnopqrstuvwxyz"
        alpha_maj= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in phrase:
            if i in alpha or i in alpha_maj:
                if i.isupper() == True:
                    i = alpha_maj[alpha_maj.index(i)-x]
                    result += str(i)
                else:
                    i = alpha[alpha.index(i)-x]
                    result += str(i)
            elif i == " ":
                result += " "
            elif i == "'":
                result += "'"
            else:
                result += "?"
        result += "\n"
        print(result)


print("Brute force :")
print(decode_cesar_force_brute("qf uqfyjktwrj"))