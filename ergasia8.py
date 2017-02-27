#ergasia8 Python
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
api = tweepy.API(auth)
	
#eisodos onomatwn
xrhsths1=raw_input('dwse onoma xrhsth1: ')
xrhsths2=raw_input('dwse onoma xrhsth2: ')

#eisagwgh filwn se listes
k1 = api.get_user(xrhsths1) 
for i in tweepy.Cursor(api.friends).items():
 lista1[i]=i.screen_name
 
k2 = api.get_user(xrhsths2)
for j in tweepy.Cursor(api.friends).items():
 lista2[j]=j.screen_name

#anazhthsh se listes filwn kai ektyposh koinwn
print "oi koinoi filoi twn xrhstwn ",xrhsths1," kai ",xrhsths2," einai: "
for i in lista1:
 for j in  lista2:
  if list1[i]==list2[j]:
   koinos=''.join(list1[i])
   print koinos
   brake
if koinos==0:
 print "kanenas koinos follower"
 
