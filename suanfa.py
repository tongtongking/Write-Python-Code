#!/usr/evn/bin/python
#--*-coding:gb2312-*-
'''
����һ����������С��һ��Ԫ�����֣��ܹ�����Щ������ɣ�Ҫ��ֻ��25����
10���֣�5�������֣�������Ӳ����
'''
for t in range(200):
    num=t#input("��������Ԫ����")
    print t,
    i=0
    j=0
    k=0
    if num>=25:
        i=num/25
        num-=i*25
        print i,"��25",
        if 25>num>=10:
            j=num/10
            num-=j*10
            print j,"��10",
            if num>=5:
                k=num/5
                num-=5*k
                print k ,"��5,������",num
                
            else:
                print "������",num
        elif num>=5:
            k=num/5
            num-=5*k
            print k,"��5��������",num
        else:
            print "������",num
    elif 25>num>=10:
        
        if num>=10:
            j=num/10
            num-=j*10
            print j ,"��10,������",num
        elif 10>num>=5:
            num-=5
            k+=1
            print j,"��10,", k ,"��5������",num
        else:
            print j,"��10,������",num
    elif 10>num>=5:
        num-=5
        k+=1
        print k ,"��5,������",num
    else:
        print num








































