#ergasia4 Python
import math
ta=[]
#enhmerwsh xrhsth:
print "*To programma ayto ypologizei thn typikh apoklish twn timwn poy 8a dwsei o xrhsths."
print "*o ypologismos ginetai xwris na ypologizei tis dyo megalyteres kai dyo mikroteres times pou 8a dwsei o xrhsths"
#pernei ws eisodo ton ari8mo twn stoixeiwn pou 8a dwsei o xrhsths:
k=input("Dwse ari8mo twn stoixeiwn: ")
#elegxos
while k<0:
 k=input("OXI ARNHTIKOUS! Dwse ari8mo twn stoixeiwn: ")
#eisagwgh stoixeiwn sthn lista
for i in range(0,k):
 x=input("dwse noumero: ")
 ta.append(x)
#afou den ypologizonte oi 2 megalyteres kai 2 mikroteres times kanw ayto gia na mhn ginei kapoio la8os
if k>=0 and k<=4:
 print "h typikh apoklish twn timwn einai 0.0"
else:
 #aferesh mikroterwn kai megalyterwn timwn:
 ta.remove(max(ta))
 ta.remove(min(ta))
 ta.remove(max(ta))
 ta.remove(min(ta))
 #YPOLOGISMOS:
 PL=len(ta)
 A8=0.0
 A=0.0
 for i in range(0,PL):
  A8=A8+ta[i]
 MO=A8/PL
 for i in range(0,PL):
  A=A+(ta[i]-MO)**2
 K=A/PL
 S=math.sqrt(K)
 #emfanish apotelesmatwn
 print "h typikh apoklish twn timwn einai ",S

