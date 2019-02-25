#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 22:58:27 2019

@author: yannick

import sympy
import math

n=262158157939114458143411
prime_number=sympy.prevprime(1+int(math.sqrt(n)))
while True:
    operand,r=divmod(n,prime_number)
    print(operand,r)
    if r==0 and sympy.isprime(operand):
        print(f"p={prime_number}, q={operand}")
        break
    else:
        prime_number=sympy.prevprime(prime_number)
        print(prime_number)
#Résultat: p=512011737421, q=512015914439
        
n=262158157939114458143411
prime_number=sympy.prevprime(1+int(math.sqrt(n)))
while True:
    operand=n/prime_number
    if int(operand)==operand and sympy.isprime(int(operand)):
        print(f"p={prime_number}, q={int(operand)}")
        break
    else:
        prime_number=sympy.prevprime(prime_number)
#Résultat: p=512011737421, q=512015914439, not sure
        
sympy.ntheory.factorint(25) 

print("1")
"""

message="v ubcfb osu ymoqsuu n cxqfj dqmfnu ub vjcfqu juz amqjmruz zmsscfusb bquflu\
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

import tp_funcs as tf
mfl=tf.most_frequent_letters(message,10)