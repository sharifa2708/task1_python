#To compare two text files

#creating list containing the sentences of each file
f1 = open("file1.txt").readlines()
f2 = open('file2.txt','r').readlines()



#printing the difference in the 2 files.

#loop cheching if the elements of same index is same
#if not then print both the elements

print("Difference in statement of God and Follower:")
for i in range(0, len(f1)):
    if f1[i]==f2[i]:
        i=i+1
        pass
    else:
        print('-' + f1[i])
        print('+' + f2[i])
        i=i+1
        continue


f1.close()
f2.close()
     

  





