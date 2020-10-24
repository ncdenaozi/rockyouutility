import hashlib as hash
import os

file1 = open(os.getcwd()+'/linkedin/SHA1.txt', 'r',encoding='utf-8') 
Lines = file1.readlines() 
#print(len(Lines[1][:-1])) 40 char with hex code

password_file=open('rockyou.txt','r',encoding='utf-8') 
passwords=password_file.readlines()
hash_dictionary={}
hash_dictionary_zero={}

for a_password in passwords:
    hash_dictionary[hash.sha1(a_password[:-1].encode('utf-8')).hexdigest()]=a_password[:-1] #for those start with non-00000
    hash_dictionary_zero['00000'+hash.sha1(a_password[:-1].encode('utf-8')).hexdigest()[5:]]=a_password[:-1] # for thoese start with 00000

count=0 #print 10 password
for i in Lines:
    if i[:-1] in hash_dictionary:
        print(i[:-1]+' '+hash_dictionary[i[:-1]])
        count+=1
    if i[:-1] in hash_dictionary_zero:
        print(i[:-1]+' '+hash_dictionary_zero[i[:-1]])
        count+=1
    if count==10:
        break






