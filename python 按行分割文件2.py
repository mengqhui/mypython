import sys;
import re;
#-*- coding:cp936 -*-
if(__name__=="__main__"):
    delim1='\t';
    delim2=',';
    fid_input=file(str(sys.argv[1]),'r');
    fid_output=file(str(sys.argv[2]),'w');
    n=int(sys.argv[3]);
    p=re.compile('(^\s+|\s+$)');
    amount_in=[];
    amount_total=[];
    amount_entire=[];
    lines=fid_input.readlines();
    fid_input.close();
    for tmp in lines:
        line=p.sub('',tmp);
        temps=line.split(delim1);
        amount_in.append(temps[2]);
        amount_total.append(temps[3]);
        amount_entire.append(temps[4]);
    data1=delim2.join(amount_in);
    data2=delim2.join(amount_total);
    data3=delim2.join(amount_entire);
    str1="["+data1+"]";
    str2="["+data2+"]";
    str3="["+data3+"]";
    fid_output.write(str1);
    fid_output.write('\n');
    fid_output.write(str2);
    fid_output.write('\n');
    fid_output.write(str3);
    fid_output.write('\n');
    print '%s has finished, congratulations!'%str(sys.argv[0]);
