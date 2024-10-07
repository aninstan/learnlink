import random as rd

weapons = ["pistol", "stein", "machete", "granat"]
current_weapon = "ingen"
explosive_equipped = False

def start():
    print("Hjelp! Romvesner har invadert jorden!")
    print("Du er den eneste som kan redde jorden.")
    print("Du kan enten velge å kjempe mot romvesnene eller flykte.")
    choice = input("Hva vil du gjøre? 'Kjempe' eller 'flykte'? ")

    if choice.lower() == "kjempe":
        fight() 
    else:
        flee()

def fight():
    print("Du har valgt å kjempe mot romvesnene. \n Du ser rundt deg. ")
    roll = rd.randint(1, 10)
    if roll < 3:
        print("Du finner ingenting annet enn en stein. \n Det var da veldig uheldig. Du tar med deg steinen uansett." )
        current_weapon = "stein"
    elif roll < 6:
        print("Du finner en pistol. Du tar den med deg.")
    else:
        print("Du har visst endt opp i et våpenlager. Du kan velge mellom en pistol, en rifle eller en granat. Hva vil du ta med deg?")
        choice = input("Hva vil du ta med deg? 'pistol', 'machete' eller 'granat'? ")
        if choice == "pistol":
            print("Du tar med deg en pistol.")
            current_weapon = "pistol"
        elif choice == "machete":
            print("Du tar med deg en machete.")
            current_weapon = "machete"
        else:
            print("Du tar med deg en granat.")
            current_weapon = "granat"
    print("Du ser en gruppe romvesner komme mot deg. Du har ingen andre valg enn å kjempe.")
    print("Du ser at romvesnene har våpen. Du ser at de er i overlegen antall.")
    print("Du ser at det er en vei til venstre og en vei til høyre.")
    choice = input("Hvilken vei vil du ta? 'Venstre' eller 'høyre'? ")

    romvesner = rd.randint(2, 5)
    roll = rd.randint(1, 10)

    if choice.lower() == "venstre":
        print("det er ", romvesner, "romvesner på veien.")
        if current_weapon == "ingen":
            print("Du har ingen våpen. Du blir tatt til fange.")
            prisoner()
        elif current_weapon == "stein":
            print("Du kaster steinen mot romvesnene. Du treffer en av dem, men de er for mange.")
            print("Du blir tatt til fange.")
            prisoner()
        elif current_weapon == "pistol":
            print("Du skyter mot romvesnene. Du treffer flere av dem. De løper vekk.")
            towards_alien_ship()
        elif current_weapon == "machete":
            print("Du løper mot romvesnene med macheten. Du klarer å drepe en.")
            if romvesner > 2 and roll < 5:
                print("De andre romvesnene dreper deg.")
                return "Game Over"
            else:
                towards_alien_ship()
        elif current_weapon == "granat":
            print("Du kaster granaten mot romvesnene. Du dreper alle sammen.")
            towards_alien_ship()


def towards_alien_ship():
    print("Du beveger deg mot romskipet. Du ser at det er flere romvesner der.")
    print("Om du kan sprenge skipet, kan du redde jorden.")

        


def flee():
    print("Du har valgt å flykte fra romvesnene. \n Du ser deg rundt. Du er ikke så langt unna Andøya, hvor ISAR har tenkt å skyte opp en rakett.")
    print("Den er egntlig ikke laget for mennesker, men du har ikke noe valg. Du må ta den.")
    print("Du må framdeles komme deg til launchpaden. Du ser en bil. \nVil du ta den, og håpe du ikke krasjer, eller satser du på at bussen kommer?")
    choice = input("Hva vil du gjøre? 'Bil' eller 'buss'? ")
    if choice == "bil":
        roll = rd.randint(1, 10)
        if roll > 5:
            print("Det er heldivis strake veien og få biler. Du kjører til launchpaden uten problemer.")
            safe_at_launchpad()
        else:
            print("Du krasjer. Du kommer deg ikke til launchpaden, og er nå i grøften utenfor Andøya.")
            print("Du ser en bil komme. Vil du prøve å stoppe den, eller vil du prøve å gå til fots?")
            choice = input("Hva vil du gjøre? 'Stopp bil' eller 'gå til fots'? ")
            if choice == "Stopp bil":
                print("Bilen stopper. Sjåføren er en hyggelig dame som tilbyr deg skyss til Andøya.")
                safe_at_launchpad()
            else:
                print("du går til fots, med romvesnene hakk i hæl. Du blir tatt til fange.")
                prisoner()

def prisoner():
    print("Du er tatt til fange av romvesnene. Du blir ført til en celle.")
    print("Du ser deg rundt. Du ser en skarp gjenstand på gulvet. Vil du prøve å stikke av?")
    choice = input("Hva vil du gjøre? 'Ja' eller 'Nei'? ")
    if choice == "Ja":
        print("Du prøver å stikke av. Du klarer å komme deg ut av cellen, men møter fort på en vakt.")
        print("Du har den skarpe gjenstanden i hånden. Vil du prøve å angripe vakten?")
        choice = input("Hva vil du gjøre? 'Ja' eller 'Nei'? ")
        if choice == "Ja":
            roll = rd.randint(1, 10)
            if roll > 5:
                print("Du klarer å overmanne vakten. Du tar våpenet hans og løper ut av romskipet.")
                print("Du ser en bil komme. Vil du prøve å stoppe den, eller vil du prøve å gå til fots?")
                choice = input("Hva vil du gjøre? 'Stopp bil' eller 'gå til fots'? ")
                if choice == "Stopp bil":
                    print("Bilen stopper. Sjåføren er en hyggelig dame som tilbyr deg skyss til Andøya.")
                    safe_at_launchpad()
                else:
                    print("du går til fots, med romvesnene hakk i hæl. Du blir tatt til fange.")
                    prisoner()
            else:
                print("Vakten overmannet deg. Du blir tatt til fange igjen.")
                print("De tar ikke sjansen igjen. Du dør i cellen.")
                return "Game Over"

def safe_at_launchpad():
    print("Du er trygt framme ved launchpaden. Du ser rakettene stå klare. Du hører en stemme bak deg.")
    print("Det er en av forskerne fra ISAR. Han forteller deg at rakettene ikke er laget for mennesker.")
    print("Du har ikke noe valg. Du må ta en av rakettene.")
    print("Du ser to raketter. Den ene er en sot rakett, med et lite vindu på toppen. Den andre er en stor rakett, som er laget for å sende ut flere hundre satteliter.")
    choice = input("Hvilken vil du ta? '1' eller '2'? ")
    if choice == 1:
        print("Du tar rakett 1. Du setter deg inn i setet. Du ser en knapp merket 'Launch'.")
        print("Du trykker på knappen. Rakett 1 skyter opp i luften. Du ser jorden bli mindre og mindre.")
        print("Du har klart det! Du har rømt fra jorden!\n Uheldivis er det ingen som kan redde jorden fra romvesnene.")
        return "Du vant!"
    if choice == 2:
        print("Du tar rakett 2. Du kryper inn i lasterommet. Du finner ingen måte å launche på.")
        print("Du hører en stemme over høytaleren utenfor: 'Evakuer stasjonen umiddelbart! Romvesnene har kommet hit!'")
        print("Romvesnene sprenger raketten du var gjømt i. Du dør i eksplosjonen.")
        return "Game Over"

start()