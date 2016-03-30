#!/usr/evn/bin/python
#--*-coding:gb2312-*-
'''
这是一个用来计算小于一美元的数字，能够用那些美分组成，要求只有25美分
10美分，5美分三种，求最少硬币数
'''
for t in range(200):
    num=t#input("请输入美元数：")
    print t,
    i=0
    j=0
    k=0
    if num>=25:
        i=num/25
        num-=i*25
        print i,"个25",
        if 25>num>=10:
            j=num/10
            num-=j*10
            print j,"个10",
            if num>=5:
                k=num/5
                num-=5*k
                print k ,"个5,余数是",num
                
            else:
                print "余数是",num
        elif num>=5:
            k=num/5
            num-=5*k
            print k,"个5，余数是",num
        else:
            print "余数是",num
    elif 25>num>=10:
        
        if num>=10:
            j=num/10
            num-=j*10
            print j ,"个10,余数是",num
        elif 10>num>=5:
            num-=5
            k+=1
            print j,"个10,", k ,"个5余数是",num
        else:
            print j,"个10,余数是",num
    elif 10>num>=5:
        num-=5
        k+=1
        print k ,"个5,余数是",num
    else:
        print num








































