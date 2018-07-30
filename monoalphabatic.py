pt=input("Enter Plain Text:").lower()
key=input("Enter Key:").lower()
k=[]
index=[]
for i in range(1,27):
  index.append(i)
for i in key:
  if i not in k:        # to avoid duplicate entry of same char 
    k.append(i)
print("key:",k)
ab=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
sabdic=dict(zip(index,ab))
for i in range(len(k)):
    ab.remove(k[i])
#print("after removing key: \n",ab)
for i in range(len(k)):
    ab.insert(i,k[i])
#print("after inserting key char:\n",ab)
ptxt=[]
for i in pt:
  ptxt.append(i)
#print("plaintext list:",ptxt)     #print statement  plaintext in list form              
#print("index is:",index)     #simply print index from 1 to 26 in a list form
enabdic=dict(zip(index,ab))
#print(enabdic)       #prints dictionary of normal abc with index
#print(sabdic)          #prints dictionary after getting modified by key with index
enindex=[]
for i in ptxt:
  c=i
  for key in sabdic.keys():
    if sabdic[key]==c:
      enindex.append(key)
#print(enindex)       #print indext position for plaintext
etext=[]
for i in enindex:
  etext.append(enabdic.get(i))
print("Encrypted Text is:","".join(etext))
