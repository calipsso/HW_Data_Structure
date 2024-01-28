class Queue:
    def __init__(self):
        self.prvky = ["kamil", "peter"]
    def prazdny(self):
        if (len(self.prvky)) == 0:
            return "Prazdny"
        else:
            return "Nieje prazdny, zvol volbu 4 pre podrobny vypis"
    def pridaj_prvok(self):
        prvok = input()
        self.prvky.append(prvok)
        return f"pridal si {prvok}"
    def odober_prvok(self):
        prvok = input()
        self.prvky.remove(prvok) # pop ak chcem podla pozicie
        return f"odobral si {prvok}"
    def vypis_prvkov(self):
        return self.prvky
        #for prvok in self.prvky:
            #return prvok
#class Menu:
    #@staticmethod
    #def Vyber_z_menu():
        #print("Vyber z menu:")
        #print("1. Zisti stav zoznamu")
        #print("2. Pridaj prvok")
        #print("3. Odober prvok")
        #print("4. Vypis prvkov")
def Vyber_z_menu():
        print("Vyber z menu:")
        print("1. Zisti stav zoznamu")
        print("2. Pridaj prvok")
        print("3. Odober prvok")
        print("4. Vypis prvkov")

queue = Queue()
while True:
    #Menu.Vyber_z_menu()
    Vyber_z_menu()
    while True:
        try:
            vyber = int(input("zadaj volbu: "))
            break
        except:
            print("zadavaj len cisla")
    if vyber == 1:
        print(queue.prazdny())
    if vyber == 2:
        print(queue.pridaj_prvok())
    if vyber == 3:
        print(queue.odober_prvok())
    if vyber == 4:
        print(queue.vypis_prvkov())
