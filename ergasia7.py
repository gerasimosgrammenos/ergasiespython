#ergasia7 Python
import tweepy
from tweepy import OAuthHandler

lista1=[]
lista2=[]
#ergaleia
consumer_key = '8245OMX5OfSiPNBW372OL3XTu'
consumer_secret = 'ugH7H4pYUL7dlgr1LdRIHReNrbHxpukHoYilwXgsnWiEejebh1'
access_token = '821320749302579201'
access_secret = 'p0ukCKWkb9JBJCWfgZ7O2naIkVvbubyoWM1TZhr9Tq8bw'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#pernei onomata xrhstwn
xrhsths1=raw_input('dwse onoma 1ou xrhsth: ')
xrhsths2=raw_input('dwse onoma 2ou xrhsth: ')

#gia ton xrhsth1 vriskei lekseis
PL1=0
for i in range(1,10):
 x= i.statuses.home.timeline(acreen_name=xrhsths1)
 lista1=list(x)
 PL1=PL1+len(lista1)
 
#gia ton xrhsth2 vriskei lekseis
i=0
PL2=0
for i in range(1,10):
 x= i.statuses.home.timeline(acreen_name=xrhsths2)
 lista2=list(x)
 PL2=PL2+len(lista2)

#ypologizei poios exei perissoteres lekseis sta teleytaia 10 tweets kai emfanizei to onoma tou
if PL1>PL2:
 print "O ",xrhsths1," exei perissoteres lekseis sta teleytaia 10 tweets"
elif PL1<PL2:
 print "O ",xrhsths2," exei perissoteres lekseis sta teleytaia 10 tweets"
else:
 print "Exoun idio ari8mo leksewn sta teleytaia 10 tweets"
