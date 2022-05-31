def antallMynter(tyvekroner, femkroner, krone):
    return tyvekroner + femkroner + krone
print(antallMynter(4, 5, 6))

def reisende():
    alder1 = (int(input("Skriv alder: ")))
    alder2 = (int(input("Skriv alder: ")))
    if alder1 > 18 and alder2 < 18:
        return True
    if alder1 < 18 and alder2 < 18:
        return None
    if alder1 > 18 and alder2 > 18:
        return None
print(reisende())

def sjekkPositiv(tallene):
    for tall in tallene:
        if (tall < 0):
            return True

print(sjekkPositiv([1,2,-3]))

def Bill():
    for BillettKjøp in [1]:
        if BillettKjøp >= 0:
            return True
        elif BillettKjøp <= 0:
            return False
print(Bill())

Billett = int(input("Tast inn din alder: "))
def b():
    if Billett <= 18:
        spørsmål = input("Reiser barnet alene? [J/n]: ")
        if spørsmål == "N" or "n":
            return 0
        if spørsmål == "j" or "J":
            return 25
    if Billett > 18 and Billett < 67:
        return 50
    elif Billett >= 67:
        return 25
print(b())

class Helpdesk:
     Ansatt1 = "Opptatt"
     Ansatt2 = "Ledig"
     Ansatt3 = "Ledig"  
     Ansatt4 = "Opptatt"

     def Ansat1():
          if Helpdesk.Ansatt1 == "Ledig":
               return -1

          if Helpdesk.Ansatt1 == "Opptatt":
               return 1

     def Ansat2():
          if Helpdesk.Ansatt2 == "Ledig":
               return -1
          if Helpdesk.Ansatt2 == "Opptatt":
               return 3
     def Ansat3():
          if Helpdesk.Ansatt3 == "Ledig":
               return -1
          if Helpdesk.Ansatt3 == "Opptatt":
               return 1
     def Ansat4():
          if Helpdesk.Ansatt4 == "Ledig":
               return -1
          if Helpdesk.Ansatt4 == "Opptatt":
               return 2

     def RingTil():
          BrRT = 3
          if BrRT == 0:
               if Helpdesk.Ansatt1 == "Opptatt":
                    return Helpdesk.Ansat2()
               elif Helpdesk.Ansatt1 == "Ledig":
                    return Helpdesk.Ansat1()

          if BrRT == 1:
               if Helpdesk.Ansatt2 == "Ledig":
                    return Helpdesk.Ansat2()
               elif Helpdesk.Ansatt2 == "Opptatt":
                    return Helpdesk.Ansat3()

          if BrRT == 2:
               if Helpdesk.Ansatt3 == "Ledig":
                    return Helpdesk.Ansat3()
               elif Helpdesk.Ansatt3 == "Opptatt":
                    return Helpdesk.Ansat2()

          if BrRT == 3:
               if Helpdesk.Ansatt4 == "Ledig":
                    return Helpdesk.Ansat4()
               if Helpdesk.Ansatt4 == "Opptatt":
                    return Helpdesk.Ansat2()
          else:
               return "Ikke Gyldig"
               exit()

     def gyldig(liste):
         BrRT = 0
         perkere, snudd = [],[]
         for verdi in liste:
             if verdi == -1:
                 BrRT+=1
                 continue
             if verdi != -1:
                 perkere.append([BrRT,verdi])
                 BrRT+=1

         BrRT=0
         for verdi in perkere:
            temp1,temp2 = verdi[-1],verdi[0]
            snudd.append([temp1,temp2])
            BrRT+=1
         for perkere1 in perkere:
            for snudd1 in snudd:
                if perkere1 == snudd1:
                    return False
         return True

list = [Helpdesk.Ansat1(), Helpdesk.Ansat2(), Helpdesk.Ansat3(), Helpdesk.Ansat4()]
print(list)
print(Helpdesk.RingTil())
if __name__ == '__main__':
    print(Helpdesk.gyldig([-1, -1, 0, 2]))
