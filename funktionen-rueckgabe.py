# funktionen-rueckgabe.py

def ueberpruefe_zugriff(benutzername, passwort):
    if benutzername =="admin" and passwort == "p":
        return True
    else: 
        return False

zugriff = ueberpruefe_zugriff()

print("Zugriff:", zugriff)

print("Zugriff:", ueberpruefe_zugriff("admin","p"))