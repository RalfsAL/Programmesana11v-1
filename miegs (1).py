a=int(input("Sveiki, ludzu ievadiet savu vecumu - "))
b=int(input("Ievadiet ludzu cik stundas Jus diennakti videji gulat - "))


if 3<=a<=5:
    print("Vecuma grupa no 3-5 gadi")
    
    if b<10:
        print("Jums butu jagul",12-b,"stundas vairak.  Vislabak iesakam iet gulet no 21:00 - 00:00, ka ari iesakam izguleties, jo Neizguloties, cilvekam paaugstinas saslimsanas risks.")
    else: print("Jus gulat nepieciesamo miega daudzumu")
    

if 6<=a<=13:
    print("Vecuma grupa no 6-13 gadi")
    
    if b<10:
        print("Jums butu jagul",10-b,"stundas vairak. Vislabak iesakam iet gulet no 21:00 - 00:00, ka ari iesakam izguleties, jo Neizguloties, cilvekam paaugstinas saslimsanas risks.")
    else: print("Jus gulat nepieciesamo miega daudzumu")

if 14<=a<=17:
    print("Vecuma grupa no 14-17 gadi")
        
    if b<9:
        print("Jums butu jagul",9-b,"stundas vairak. Vislabak iesakam iet gulet no 21:00 - 00:00, ka ari iesakam izguleties, jo Neizguloties, cilvekam paaugstinas saslimsanas risks.")
    else: print("Jus gulat nepieciesamo miega daudzumu")
    
if 18<=a<=25:
    print("Vecuma grupa no 18-25 gadi")
        
    if b<8:
        print("Jums butu jagul",8-b,"stundas vairak. Vislabak iesakam iet gulet no 21:00 - 00:00, ka ari iesakam izguleties, jo Neizguloties, cilvekam paaugstinas saslimsanas risks.")
    else: print("Jus gulat nepieciesamo miega daudzumu")
    
if 26<=a<=64:
    print("Vecuma grupa no 26-64 gadi")
            
    if b<8:
        print("Jums butu jagul",8-b,"stundas vairak. Vislabak iesakam iet gulet no 21:00 - 00:00, ka ari iesakam izguleties, jo Neizguloties, cilvekam paaugstinas saslimsanas risks.")
    else: print("Jus gulat nepieciesamo miega  daudzumu")

if 65<=a<=200:
    print("Vecuma grupa 65+ gadi")
                
    if b<7:
        print("Jums butu jagul",8-b,"stundas vairak. Vislabak iesakam iet gulet no 21:00 - 00:00, ka ari iesakam izguleties, jo neizguloties, cilvekam paaugstinas saslimsanas risks.")
    else: print("Jus gulat nepieciesamo miega daudzumu")
    
if 155<a:
    print("Dati nav piejami sim vecumam")