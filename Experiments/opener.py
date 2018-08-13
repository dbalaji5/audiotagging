import numpy as np

#program to create vocabulary of labels from the training data
file = open('train.csv','r')
vocab=[]
words=set()
j=0
for i in file:
	if(j!=0):
		#print(i)
		ls=i.split(",")[1]
		words.add(ls)
	j=j+1
#print(words)
#print(len(words))
all_words=sorted(list(words))
vocab={ all_words[j]:j for j in range(0,len(all_words)) }
print(vocab)
file.close()
k=0
label=[]
file2 = open('train.csv','r')
for iter in file2:
	if(k!=0):
		name=iter.split(",")[1]
		label.append(vocab[name])
	k=k+1
	if(k==1001):
		break

label=np.array(label)
print(label.shape[0])
label2=np.eye(len(all_words))[label]  #command to create one hot vector
print(label2.shape)