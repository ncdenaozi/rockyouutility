import hashlib as hash
import os

def plusonechar(string1):
    result=[]
    result.append(string1)
    result=[]
    for i in range(ord('9')+1-ord('0')):
        result.append(string1+chr(ord('0')+i))
        result.append(chr(ord('0')+i)+string1)
    for i in range(ord('Z')+1-ord('A')):
        result.append(string1+chr(ord('A')+i))
        result.append(chr(ord('A')+i)+string1)
        result.append(string1+chr(ord('a')+i))
        result.append(chr(ord('a')+i)+string1)
    return result

file1 = open(os.getcwd()+'/formspring/formspring.txt', 'r',encoding='utf-8') 
Lines = file1.readlines() 

password_dictionary=open('rockyou.txt','r',encoding='utf-8') 
passwords=password_dictionary.readlines()
hash_dictionary={}
result=[]
#print(len(Lines[1][:-1])) #64 digit

#print(len(plusonechar(a_password)))

for a_password in passwords:
    a_password=a_password[:-1]
    salt1=plusonechar(a_password)
    for i in salt1:
        hash_dictionary[hash.sha256(i.encode('utf-8')).hexdigest()]=i

count=0 #print 10 password
for i in Lines:
    if i[:-1] in hash_dictionary:
        print(i[:-1]+' '+hash_dictionary[i[:-1]])
        
    else:
        print('no key')
    count+=1
    if count==10:
        break




