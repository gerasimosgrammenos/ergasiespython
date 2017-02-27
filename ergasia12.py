#ergasia12 Python
import Tkinter
import urllib2
import json
import webbrowser
#synarthsh gia to pathma tou koumpiou pou 8a syndesei programma me syntagh
def koumpi():
 ALLO=list(MT[4])
 del ALLO[0:16]
 del ALLO[-1]
 OLE=''.join(ALLO)
 webbrowser.open(OLE)
#eisagwgh stoixeiwn
print ("Peinas kai Den exeis lefta gia delivera.. Se noiw8w.. Gi ayto yparxei ayto to programma gia sena.. eykoles syntages me to pathma enws koumpiou! ")
faghto=(raw_input("Ti 8es na fas? : "))
#diamorfwsh telikhs diey8ynshs (link+faghto=LST)
link='http://food2fork.com/api/search?key=a5446eeff2c051ff5c431acbc7b6cb46&q='
LST=list(link)
LST.extend([faghto])
metavlhth=''.join(LST)
#"anazhthsh" sthn diey8ynsh gia faghto
response = urllib2.urlopen(metavlhth)
selida = response.read()
selida=selida.replace("<br>","")
selida=selida.strip()
grammes=selida.split("\n")
MT= grammes[0].split(",")
xy=list(MT[3])
#diagrafh perittwn stoixeiwn gyro apo to onoma tou faghtou
del xy[0:10]
ky=''.join(xy)
#emfanish faghtou
print "Sou vrhka mia syntagh sxetikh me ayto pou 8es na fas : ",ky
#"anazhthsh" sthn diey8ynsh gia tyxaia mpyra
resp = urllib2.urlopen('https://api.punkapi.com/v2/beers/random')
sel = resp.read()
sel=sel.replace("<br>","")
sel=sel.strip()
gram=sel.split()
MT1= gram[0].split(",")
ko=list(MT1[1])
#diagrafh perittwn stoixeiwn gyro apo to onoma ths mpyras
del ko[0:7]
ko=''.join(ko)
#emfanish tyxaias mpyras kai faghtou
print "Synodepse to faghto: ",ky," me mia mpyra: ",ko
#pathma koumpiou kai syndesh me thn istoselida poy exei thn syntagh
top = Tkinter.Tk()
B = Tkinter.Button(top, text ="Deite thn syntagh EDW", command = koumpi)
B.pack()
top.mainloop()