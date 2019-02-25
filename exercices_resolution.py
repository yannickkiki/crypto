#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:25:52 2019

@author: yannick
"""

import tp_funcs as tf
from itertools import combinations
import sympy
import math

"""
#-------TP Code cesar application-------#
message_encrypted="vcfgrwqwfsbhfsntowbsobgfsbhfsnqvsnjcigsghqsoixcifrviwtshse"\
"icwbsgojsnjcigdogeisjcigoihfsgofhwgobgjcigbsrsjsnqwfqizsfrobgzsgfisgzsgxcifg"\
"cijfopzsgeiojsqzsggwubsgrsjchfsdfctsggwcbdofzseiszsghhcbashwsf"
message_decrypted=tf.caesar_decrypt_message(message_encrypted,0)
if message_decrypted is not None:
    print(f"Decrypted message : {message_decrypted}")
"""

"""
#-------TP 02, piste bleue------------#
message="ZCNUVJ LUYLNQL GXA PFPPJ LV XHKSA UFLPX HXJJ UFPPYL GXAGQSG JZV SHKSLGY ZCNUV XHGSZ CALE XHKSAG JZVJSNJ LUY UCNUG JA UFPPY ZCJUU FCGH"
print(tf.vigenere_decrypt_message(message,[0,0,0]))
"""

"""
#-------TP machine Enigma, piste verte------------#
numeric_message=tf.des8_block_n_decryption(2,[3,4,8,0,1,4,8,1],[3,1,4,1])
print(numeric_message)
alphabetic_message=""
for digit in numeric_message:
    alphabetic_message+=tf.relative_chr(digit)
print(alphabetic_message)
"""

"""
#---------TP Machine Enigma , piste bleue---------#       
message_encrypted="RFWOFLNLBAVDKWS"
c1=[13, 13, 4, 14, 7, 7, 14, 12, 23, 13, 19, 15, 19, 5, 14]
c2=[15, 1, 4, 21, 16, 11, 21, 0, 1,9, 17, 14, 22, 9, 0]
message_decrypted=""
for i,l in enumerate(message_encrypted):
    message_decrypted+=tf.caesar_alphabet_decrypt(l,c1[i]+c2[i])
print(message_decrypted)
"""

"""
#-------TP Machine Enigma, piste rouge----------#
#key="ABC"
def generate_keys(alphabet,key_size):
    combins=list(combinations(alphabet,key_size))
    keys=list()
    for c in combins: keys.append(''.join(list(c)))
    return keys

letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",\
         "R","S","T","U","V","W","X","Y","Z"]
#keys=generate_keys(letters,3)
keys=["ABL"]
#print(keys)
reference_anneau="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
""
message_encrypted="AAA" #initialisation
for i in range(3):
    key_letter_position=reference_anneau.find(key[i])
    mobile_anneau=reference_anneau[key_letter_position:]+\
    reference_anneau[:key_letter_position]
    message_encrypted=tf.enigma_encrypt_message(message_encrypted,\
                                                mobile_anneau)
print(message_encrypted)
""
for key in keys:
    message_decrypted="TTMMCVB XEV SHILG ZTJGJY X FDOC GC TZYV ZVINWX KT ETUXS TYPTXE UM FMD APRXEVJ EW"
    message_decrypted=message_decrypted.replace(" ","")
    for i in range(3):
        key_letter_position=reference_anneau.find(key[2-i])
        mobile_anneau=reference_anneau[key_letter_position:]+\
        reference_anneau[:key_letter_position]
        message_decrypted=tf.enigma_decrypt_message(message_decrypted,\
                                                    mobile_anneau)
    print(f"Key: {key}, Message found: {message_decrypted}")
    #Mot qui suit: toison , Source: Google
"""

"""
#-------TP 04, piste verte----------#
Résultat: 79 (fait aux yeux)
"""

"""
#-------TP 04, piste bleue----------#
mobile_anneau="ERXBYQDCNFPTMJKSWILVAOUZHG"
message_encrypted="IXELVOJEPBVQWYNUISO"
message_decrypted=""
while "METEO" not in message_decrypted:
    mobile_anneau=mobile_anneau[1:]+mobile_anneau[0]
    message_decrypted=tf.enigma_decrypt_message(message_encrypted,mobile_anneau)
print(f"Message decrypted: {message_decrypted}")
#Result: Message decrypted: BLIZZARDMETEOBERLIN donc on parle de Berlin
"""

"""
#-------TP 04, piste rouge----------#
n=262158157939114458143411
prime_number=sympy.prevprime(1+int(math.sqrt(n)))
while True:
    operand,r=divmod(n,prime_number)
    if r==0 and sympy.isprime(operand):
        print(f"p={prime_number}, q={operand}")
        break
    else:
        prime_number=sympy.prevprime(prime_number)
#Résultat: p=, q=
""" 

"""
#-------TP 05, piste verte----------#
Solution: 38
"""

"""
#-------TP 05, piste bleue----------#
number=2
while True:
    if not sympy.isprime(number) and tf.verify_fermat_ns_list_tests([3,5],number):
        print(f"Good number is : {number}")
        break
    number+=1
#Good number is : 1541
"""

"""
#-------TP 05, piste rouge----------#
p,n,ka,kb=123457,54321,66475,61625
found=True
for a in range(100000):
    for b in range(100000):
        if pow(kb,a,p)==pow(ka,b,p) and pow(n,a,p)==ka and pow(n,b,p)==kb:
            result=n**(a*b)%p
            print(f"a: {a}, b: {b}, N: {result}")
            exit()
"""
"""
#---dont care---#
comp_a=0
while not found and comp_a<5:
   big1=p*comp_a+ka
   a=tf.power(ka,big1)
   if a is not None:
       big2=kb**a
"""

"""
#-------TP 06, piste verte----------#
codes_encrypted,n,e=[1,15,20,19,11,28],33,29
codes_decrypted=tf.rsa_decrypt_list(codes_encrypted,n,e)
words_encrypted="TPO HOHJDQFH HQFXXJ YHCPA PE GEBHOYR".split(" ")
words_decrypted=[tf.caesar_alphabet_decrypt_str(w_enc,codes_decrypted[i]) \
                 for i,w_enc in enumerate(words_encrypted)]
print(words_decrypted)
"""

"""
#-------TP 06, piste bleue----------#
message=tf.rsa_decrypt(611574858,3055461121,3)
#message: 314159265
"""

"""
#-------TP 06, piste rouge----------#
n,e=2035153,5
message_encrypted="ANRNK CKGAG EJILP AKNKV BRJPX ATUDR BRJNR BYNLL BINJP AJAHR BLZBH AAEEN CVPSB DZFZN CMLGZ"
codes_encrypted=[tf.message_block_code(block) for block in message_encrypted.split(" ")]
codes_decrypted=tf.rsa_decrypt_list(codes_encrypted,n,e)
blocks_decrypted=[tf.message_block_decode(cd,4) for cd in codes_decrypted]
message_decrypted=""
for block in blocks_decrypted: message_decrypted+=block
print(message_decrypted)
#message: MERC IPOU RCEM OOCT OUSN OSVO EUXD EREU SSIT EDAN SVOS PROC HAIN SPRO JETS
#message reviewed: MERCI POUR CE MOOC TOUS NOS VOEUX DE REUSSITE DANS VOS PROCHAINS PROJETS
#solution: PROJETS
"""

"""
#----Devoir Cryptographie, RII5,2016-2017, Partie 1----#
message_encrypted="v ubcfb osu ymoqsuu n cxqfj dqmfnu ub vjcfqu juz amqjmruz\
 zmsscfusb bquflu\
auoquz hfszbms zwfba ju wusbms qusbqu ncsz ju vmo z uddmqvcfb n uxfbuq ju\
xusb wcoxcfz fj eczzc qcefnuwusb jc emqbu xfbquu no ijmv nuz wcfzmsz nu jc\
xfvbmfqu ecz czzul qcefnuwusb vueusncsb emoq uweuvauq kou z usrmoddqu us\
wuwu buwez kou jof os bmoqifjjms nu emozzfuqu ub nu zciju\
ju acjj zusbcfb ju vamo vofb ub ju xfuog bcefz c j osu nu zuz ugbquwfbuz\
osu cddfvau nu vmojuoq bqme xczbu emoq vu nuejmfuwusb fsbuqfuoq ubcfb\
vjmouu co woq ujju quequzusbcfb zfwejuwusb os usmqwu xfzcru jcqru nu ejoz\
n os wubqu ju xfzcru n os amwwu n usxfqms kocqcsbu vfsk csz c j uecfzzu\
wmozbcvau smfqu cog bqcfbz cvvusbouz ub iucog\
hfszbms zu nfqfruc xuqz j uzvcjfuq fj ubcfb fsobfju n uzzcpuq nu\
equsnqu j czvuszuoq wuwu cox wufjjuoquz uemkouz fj dmsvbfmsscfb qcquwusb\
cvboujjuwusb n cfjjuoqz ju vmoqcsb ujuvbqfkou ubcfb vmoeu ncsz jc ymoqsuu\
v ubcfb osu nuz wuzoquz n uvmsmwfu eqfzuz us xou nu jc zuwcfsu nu jc acfsu\
zms ceecqbuwusb ubcfb co zuebfuwu hfszbms kof cxcfb bqusbu suod csz ub\
zmoddqcfb n os ojvuqu xcqfkouog co nuzzoz nu jc vauxfjju nqmfbu wmsbcfb\
jusbuwusb fj z cqqubc ejozfuoqz dmfz us vauwfs emoq zu quemzuq c vackou\
ecjfuq zoq osu cddfvau vmjjuu co woq dcvu c jc vcru nu j czvuszuoq j\
usmqwu xfzcru xmoz dfgcfb no qurcqn v ubcfb os nu vuz emqbqcfbz cqqcsruz\
nu bujju zmqbu kou juz puog zuwijusb zofxqu vujof kof eczzu osu jurusnu\
zmoz ju emqbqcfb nfzcfb ifr iqmbauq xmoz qurcqnu\
c j fsbuqfuoq nu j ceecqbuwusb nu hfszbms osu xmfg zovquu dcfzcfb usbusnqu\
osu zuqfu nu smwiquz kof cxcfusb bqcfb c jc eqmnovbfms nu jc dmsbu jc xmfg\
eqmxuscfb n osu ejckou nu wubcj mijmsrou wfqmfq buqsu usvczbqu ncsz ju woq\
nu nqmfbu hfszbms bmoqsc os imobms ub jc xmfg nfwfsoc nu xmjowu wcfz juz\
wmbz ubcfusb usvmqu nfzbfsvbz ju zms nu j ceecqufj no bujuvqcs vmwwu ms\
nfzcfb emoxcfb ubqu czzmoqnf wcfz fj s p cxcfb covos wmpus nu j ubufsnqu\
vmwejubuwusb hfszbms zu nfqfruc xuqz jc dusubqu fj ubcfb nu zbcboqu dquju\
ejobmb eubfbu ub zc wcfrquoq ubcfb zmojfrsuu ecq jc vmwifscfzms ijuou\
osfdmqwu no ecqbf fj cxcfb juz vauxuog bquz ijmsnz ju xfzcru scboqujjuwusb\
zcsrofs jc euco noqvfu ecq ju zcxms rqmzzfuq juz jcwuz nu qczmfq uwmozzuuz\
ub ju dqmfn nu j afxuq kof xuscfb nu equsnqu dfs"
message_decrypted=message_encrypted[:]
most_fl=tf.most_frequent_letters(message_encrypted,5)
#most_fw=tf.most_frequent_words(message_encrypted,2,6)
message_decrypted=message_decrypted.replace("u","E")
message_decrypted=message_decrypted.replace("c","S")
message_decrypted=message_decrypted.replace("j","L")
mp=message_decrypted[:]
for i,letter in enumerate(message_decrypted):
    if letter.islower(): mp=mp[:i]+"*"+mp[i+1:]
print(mp)
"""
    