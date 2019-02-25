#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:25:52 2019

@author: yannick
"""

import collections
import math
import sympy

ALPHABET_SIZE=26

def caesar_alphabet_encrypt(char,key):
    """encrypts a character with Caesar encryption 
    based on the letters of the alphabet"""
    ord_of_encrytion=(ord(char)-ord("A")+key)%ALPHABET_SIZE
    return chr(ord_of_encrytion+ord("A"))

def caesar_alphabet_encrypt_str(string,key):
    """encrypts a string with Caesar encryption 
    based on the letters of the alphabet"""
    str_encrypted=""
    for char in string:
        str_encrypted+=caesar_alphabet_encrypt(char,key)
    return str_encrypted

def caesar_alphabet_decrypt(char,key):
    """decrypts a character with Caesar encryption 
    based on the letters of the alphabet"""
    ord_of_deciphered=(ord(char)-ord("A")-key)%ALPHABET_SIZE
    return chr(ord_of_deciphered+ord("A"))

def caesar_alphabet_decrypt_str(string,key):
    """decrypts a string with Caesar encryption 
    based on the letters of the alphabet"""
    str_decrypted=""
    for char in string:
        str_decrypted+=caesar_alphabet_decrypt(char,key)
    return str_decrypted

def most_frequent_letter(message):
    """find the most frequent letter in the message and return it"""
    return most_frequent_letters(message,1)[0]

def most_frequent_letters(message,number_of_letters_to_return):
    """find the most @number_of_letters_to_return frequent letter in the message and return it"""
    m=message.replace(" ","")
    return [w[0] for w in collections.Counter(list(m)).most_common(number_of_letters_to_return)]

def most_frequent_words(message,number_of_letters,number_of_words_to_return) :
    """find the @number_of_words_to_return most frequent words"""
    n_letters_words=[w for w in message.split(" ") if len(w)==number_of_letters]
    return [w[0] for w in collections.Counter(n_letters_words).most_common(number_of_words_to_return)]
    
    
def caesar_find_key(message_encrypted,method_number):
    """try to find the key of the Caesar encryption 
    based on the frequent letters (fl) of the alphabet. The method number 
    determines which letter we want to consider as most frequent in decrypted
    message"""
    fl_in_french=["E","S","A","I"]
    fl_in_encrypted_message=most_frequent_letter(message_encrypted)
    return ord(fl_in_encrypted_message)-ord(fl_in_french[method_number])%ALPHABET_SIZE
            
def caesar_decrypt_message(message_encrypted,method_number):
    """try to encrypts a whole message with Caesar encryption 
    based on the letters of the alphabet (the key is not known)."""
    caesar_key=caesar_find_key(message_encrypted,method_number)
    if caesar_key is not None:
        return caesar_alphabet_decrypt_str(message_encrypted,caesar_key)
    
def caesar_ascii_encrypt(char,key):
    """encrypts a character with Caesar encryption 
    based on ascii table"""
    ord_of_encrytion=(ord(char)+key)%128
    return chr(ord_of_encrytion)

def caesar_ascii_decrypt(char,key):
    """decrypt a character with Caesar encryption 
    based on ascii table"""
    ord_of_deciphered=(ord(char)-key)%128
    return chr(ord_of_deciphered)

def vigenere_decrypt_str(key,message_encrypted):
    """decrypt a message encrypted with Vigenere encryption.. @key is a list
    of the shifts in one block"""
    message_e=message_encrypted.replace(" ","")
    message_d=""
    key_size=len(key)
    for i,letter in enumerate(message_e):
        message_d+=caesar_alphabet_decrypt(letter,key[i%key_size])
    return message_d

def vigenere_find_key(message_encrypted,methods):
    """Try to find vigenere key using methods-based considerations.. In this
    case we know the key size but not the key elements"""
    message_e=message_encrypted.replace(" ","")
    block_size=len(methods)
    key=list()
    for i,method_number in enumerate(methods):
        key.append(caesar_find_key(message_e[i::block_size],method_number))
    return key
    
def vigenere_decrypt_message(message_encrypted,methods):
    """Try to decrypt message encrypted with vigenere encryption using 
    methods-based considerations.. In this case we know the key size but 
    not the key elements"""
    key=vigenere_find_key(message_encrypted,methods)
    return vigenere_decrypt_str(key,message_encrypted)
    
def enigma_encrypt_message(message,mobile_anneau):
    """encrypt a @message with enigma machine encryption using 
    @mobile_anneau""" 
    fixed_anneau="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_encrypted=""
    for i,letter in enumerate(message):
        message_encrypted+=mobile_anneau[(i+fixed_anneau.find(letter))%ALPHABET_SIZE]
    return message_encrypted

def reverse(string):
    """reverse a string
    Example: "abc"->"cba"
    """
    return string[::-1]

def enigma_decrypt_message(message_encrypted,mobile_anneau):
    """decrypt a @messsage with enigma machine encryption using 
    @mobile_anneau"""
    fixed_anneau="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message_encrypted_reversed=reverse(message_encrypted)
    message_decrypted=""
    for i,letter in enumerate(message_encrypted_reversed):
        message_decrypted=fixed_anneau[(mobile_anneau.find(letter)+i\
                                        -(len(message_encrypted)-1))%ALPHABET_SIZE]+\
    message_decrypted
    return message_decrypted

def des8_block_encryption(int_list_block,key):
    """DES encryption of block of 8 characters"""
    if len(int_list_block)!=8 or len(key)!=4:
        exit()
    else:
        new_block=int_list_block[4:8]+[(int_list_block[1]+key[0])%10,\
                                (int_list_block[2]+key[1])%10,\
                                (int_list_block[3]+key[2])%10,\
                                (int_list_block[0]+key[3])%10]
        return new_block

def des8_block_n_encryption(n,int_list_block,key):
    """DES encryption of block of 8 characters 
    repeated n times"""
    new_block=int_list_block
    for i in range(n):
        new_block=des8_block_encryption(new_block,key)
    return new_block
    
def des8_block_decryption(int_list_block,key):
    """DES decryption of block of 8 characters"""
    if len(int_list_block)!=8 or len(key)!=4:
        exit()
    else:
        new_block=[(int_list_block[7]-key[3])%10,\
                   (int_list_block[4]-key[0])%10,\
                   (int_list_block[5]-key[1])%10,\
                   (int_list_block[6]-key[2])%10]+int_list_block[0:4]
        return new_block

def des8_block_n_decryption(n,int_list_block,key):
    """DES decryption of block of 8 characters 
    repeated n times"""
    new_block=int_list_block
    for i in range(n):
        new_block=des8_block_decryption(new_block,key)
    return new_block

def relative_ord(letter):
    """ord of letter compared 
    to "A" """
    return ord(letter)-ord("A")

def relative_chr(n):
    """letter at position @n compared 
    to "A" position"""
    return chr(n+ord("A"))

def verify_fermat_n_test(n,number):
    """Verify if number respect fermat n test. 
    p verify fermat n test if n**(p-1) congru 1 modulo p"""
    if number<2 or type(number)!=int:
        print("Not a valid number")
        return False
    return pow(n,number-1,number)==1

def verify_fermat_ns_list_tests(list_of_n,number):
    """Verify if number respect fermat tests for all of n listed in list_of_n"""
    return all([verify_fermat_n_test(n,number) for n in list_of_n])

def power(number,result):
    """get power such as: number**power = result"""
    power=round(math.log(result,number)) #because of imprecision
    if number**power==result:
        return power
    return None

def bezout_coefs(a,n):
    """get bezout's coefficients of a and n such as ax+nk=gcd(a,n)"""
    if n==0: return (1,0)
    else:
        u,v=bezout_coefs(n,a%n)
        return v,u-(a//n)*v
       
def cm_eq_solution(a,b,n):
    """resolv ax congru b modulo n equation and return x"""
    gcd=math.gcd(a,n)
    if b%gcd==0:
        x_,k_=bezout_coefs(a,n)
        return int(x_*b/gcd)
    print("Cm equation have not solution")
    return None
    
def rsa_private_key(n,e):
    """return private key of rsa encryption with public parameters n and e.
    I'm talking about the "d" in our course """
    p,q=0,0
    try:
        p,q=list(sympy.ntheory.factorint(n))
    except ValueError:
        print("The parameter n must be the product of two prime numbers!")
    ø=(p-1)*(q-1)
    return cm_eq_solution(e,1,ø)%ø

def rsa_decrypt(x,n,e):
    """decrypt message x encrypted with rsa of parameters n , e"""
    return pow(x,rsa_private_key(n,e),n)

def rsa_decrypt_list(list_x,n,e):
    """decrypt messages x in list_x encrypted with rsa of parameters n , e"""
    private_key=rsa_private_key(n,e)
    return [pow(x,private_key,n) for x in list_x]

def message_block_code(block):
    """this function make the correspondance AAAAA=>0, AAAAB=>1, ...
    (example for size=5)"""
    code=0
    size=len(block)
    for i,letter in enumerate(block):
        code+=relative_ord(letter)*(ALPHABET_SIZE**(size-i-1))
    return code

def message_block_decode(code,size):
    """this function make the correspondance 0=>AAAA, 1=>AAAB, ...
    (example for size=4)"""
    message=""
    for i in range(size):
        message=relative_chr(code%ALPHABET_SIZE)+message
        code=code//ALPHABET_SIZE
    return message