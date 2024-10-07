def sjakkbrett_farge(pos):
    tall = int(pos[1])              #gir variabelen tall verdien til andre del av argumentet
  
    if ((ord(pos[0]) + tall)) % 2 == 0:
        print(ord(pos[0]) + tall)
        return "Svart"            
    return "Hvit"       

print(sjakkbrett_farge("a1")) # Skal returnere "svart"
print(sjakkbrett_farge("d3")) #skal returnere "hvit"
print(sjakkbrett_farge("f6")) #skal returnere "svart"