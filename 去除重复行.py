#coding=utf-8
fin = open("input.txt",'r')
fout = open('output.txt','a+')
bufferedlines = []
while(fin and (line = fin.readline())):
    i = 0;
    for(i=0;i<len(bufferedlines);++i):
        if(line == bufferedlines[i]):
            break;
    if i == len(bufferedlines):
        bufferedlines.append(line)
        fout.write(line)