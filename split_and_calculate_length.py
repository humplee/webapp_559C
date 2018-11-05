import re
fo=open("DavidChenTweets1.txt")
line=fo.read
pattern=re.compile(r"b'.+'|b\".+\"")
linelist=pattern.findall(line)
counter=0
the_length=0
for j in linelist:
    counter+=1
    the_length+=len(j)
if counter!=0:
    avg=the_length/counter
print(avg)
