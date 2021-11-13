#serialization

print "############ using pickling #############"
import cPickle

records=[1,2,3,{1:2},[3,4,5,[5,6,7]]]

f = open("C:\Lalit\temp.txt","w")
cPickle.dump(records,f)

for record in records:
    f.write("%d\n",record)
f.close()

f= open("C:\Lalit\temp.txt","r")
print cPickle.load(f)[4][3][2]
f.close()
