# Fonction récursive pour calculer le n-ième terme de la suite de Fibonacci

def fibonacci(n):
    if n <= 0:
        return "Entrée invalide"
    elif n == 1 :
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

adresses_IP=["192.168.0.1","10.0.0.1","172.16.0.1","200.100.50.1","169.254.0.1"]
print(f"la premiere adresse dans la listest:{adresses_IP[0]}")
print("la derniere adresse dans la list est:",adresses_IP[-1])
print("la troisieme adresse dans la list est:",adresses_IP[2])
adresses_IP.append("172.31.0.1")
adresses_IP.remove("200.100.50.1")
print(adresses_IP)
print(len(adresses_IP))
if "192.168.0.1" in adresses_IP:
    print("l'adresses est dans la list")
else:
    print("l'dresses n'est pas dans la list")


def ip_class(V):

    HP = int(V.split('.')[0])

    if 1 <= HP <= 126:
        return "Class A"
    elif 128 <= HP <= 191:
        return "Class B"
    elif 192 <= HP <= 223:
        return "Class C"
    else:
      return "adress ip not vlaid"

print("the class of 10.0.0.1 is:",ip_class(adresses_IP[1]))


adresses_IP.sort()
print("Liste triée :", adresses_IP)


TP = all(ip.startswith("192.") for ip in adresses_IP)
if TP:
    print(" Toutes les adresses sont de classe C ")
else:
    print(" Pas toutes les adresses sont de classe C ")

public = 0
for i in adresses_IP:
    if  ip_class(i):
        public+= 1


print("Total public IP addresses:",public)