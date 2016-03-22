# # math库
# # 160315
# import math
# import random
#
# # math.ceil（x） 向上取整
# # a=math.ceil(-0.1)
# # print(a)
# # a=math.ceil(0.1)
# # print(a)
# #
# #
# # # math.copysign(x,y)
# #
# # a=math.copysign(1,1)
# # print(a)
# # a=math.copysign(-10,2)
# # print(a)
# #
# #
# # a=math.degrees(math.pi)
# # print(a)
# #
# # a=math.trunc(-3)
# # print(a)
# #
# # a=math.fabs(-123)
# # print(a)
# #
# # a=5*4*3*2*1
# # print(a)
# # a=math.factorial(5)
# # print(a)
# #
# # a=math.hypot(3,4)
# # print(a)
# #
# # a=random.seed(1)
# # print(a)
# # a=random.seed(1)
# # print(a)
# # a=random.seed(1)
# # print(a)
# # a=random.getstate(
# # a=random.randint(1,4)
#
# # a=random.choice(b)
# # a=random.randrange(1,4)
# # a=random.uniform(1,20)
# # a=random.randrange(1,11,3)
# # a=random.choice('哦阿加莎敌法师哦isdjfoiasj')
# #
# # b=[1,2,1233,1]
# # random.shuffle(b)
# # print(b)
#
#
# # items = [1, 2, 3, 4, 5, 6, 7]
# # random.shuffle(items)
# # print(items)
# # print(a)
#
# #
# # a=[1,2,3,4,5]
# # a.append(1)
# # print(a)
# # a.pop(-1)
# # print(a)
# # a.append(123)
# # a.sort()
# # print(a)
# # a[1]=123123
# # a.sort()
# # print(a)
# # a.reverse()
# # print(a)
# # b=[[1,2,3],[4,5,6],[7,8,9]]
# # c=[row[1] for row in b]
# # print(c)
#
# # # help(map)
# #
# # a={}
# # a["b"]='2'
# # a["c"]="3"
# # a["d"]="4"
# # # print(a)
# # # keys=a.keys()
# # print(keys)
# # key=list(keys)
# # print(key)
# # key.sort()
# # print(key)
# # for i in key:
# #     print(i +"=>"+a[i])
# #
# # for key in sorted(a):
# #     print(key+"=>"+a[key])
# # if not 'f' in a:
# #     print('missing')
# #
# # print(a.try('e'))
# # help(get)
# # from decimal import Decimal
# # a=Decimal(0.1)+Decimal(0.1)+Decimal(0.1)-Decimal(0.3)
# # print(a)
# #
# # import fractions
# # import random
# # seq=[1,3,5,7,9,11,13,15]
# #
# # sum1=0
# # for x in seq:
# #     a=random.sample(seq,3)
# #     sum1+=int(x)
# #     if sum1==30:
# #         print(a)
# #     else:
# #         # print(a)
# # #         continue
# # path='abcdef'
# # print(path[::-2])
# import sys
# def readfile(filename):
#     '''Print a file to the standard output.'''
#     f = file(filename)
#     while True:
#           line = f.readline()
#           if len(line) == 0:
#              break
#           print(line)
#     f.close()
# print "sys.argv[0]---------",sys.argv[0]
# print "sys.argv[1]---------",sys.argv[1]
# print "sys.argv[2]---------",sys.argv[2]
# # Script starts from here
# if len(sys.argv) < 2:
#     print 'No action specified.'
#     sys.exit()
# if sys.argv[1].startswith('--'):
#    option = sys.argv[1][2:]
#    # fetch sys.argv[1] but without the first two characters
#    if option == 'version':
#       print 'Version 1.2'
#    elif option == 'help':
#       print '''"
#            This program prints files to the standard output.
#            Any number of files can be specified.
#            Options include:
#            --version : Prints the version number
#            --help    : Display this help'''
#    else:
#        print 'Unknown option.'
#        sys.exit()
# else:
#     for filename in sys.argv[1:]:
#         readfile(filename)
#
# # s= 'spam'
# # s[0]='x'
# # print(s)
#
#
# a="123123123k123123123k123123kasDasdkasdasdasdk"
# # print(a.split("k"))
# print(a.isalpha())


#
# res="%d...%6d...%-6d...%06d...%-06d" % (x,x,x,x,x)
# res="%s" % x
# print('123123*'+res+'*1')
# res="%7.1s" % x
# print('123123*'+res+'*1')
# res="%-7.1s" % x
# print('123123*'+res+'*1')
#


# x=123456789
# # print("%f" % x)
# # print("%.3f" % x)
# # print("%.8f" % x)
# # a='{5:<s}'.format(99999)
# # print(a)
#
# x=[1,2,3,4]
# x.extend([3,4,5,6])
# x.sort(reverse=True)
# print(x)
# print(x.count(3))
#
# a={"x":1,
#    "y":2}
# b=list(a)
# # b.sort()
# for key in sorted(b):
#     if "z" in b:
#         print(key,a[key])
#     else:
#         print(0)

# a={"a":0,"b":0}
# print(a)
# a={}
# a["a"]=0
# a['b']=0
# print(a)
# a=dict(a=0,b=0)
# print(a)
# a=dict([('a',0),('b',0)])
# # print(a)
# l=[1,2,3,4]
# l[0]=5
# print(l)
# l.append(1)
# print(l)
# l.pop()
# print(l)
# del l[2]
# print(l)
# b=[123,123,123]
# l.extend(b)
# print(l)
# l.insert(123,4)
# print(l)
# l.sort(reverse=True)
# print(l)



# myfile = open('myfile','w')
# myfile.write('hello world \n')
# myfile.write('good bye \n')
# myfile.close()
#
# myfile = open('myfile','rb')
# # for line in myfile:
# #     print(line)
# # a=myfile.readlines()
# a=myfile.readline()
# # print(a)
# x,y,z=1,2,3
# s='stop'
# t=(1,2)
# l=['a','b']
# d=dict(a=1,b=2,c=3)
# myfile = open('myfile','w')
# # print('%s%s%s \n' % (x,y,z))
# myfile.write('%s%s%s \n' % (x,y,z))
# myfile.write(s+'\n')
# myfile.write(str(t)+'\n')
# myfile.write(str(d)+'\n')
# myfile.close()
#
# myfile =open('myfile')
# for line in myfile:
#     print(line)
#
#
#
# # myfile =open('myfile').read()
# # print(myfile)
#
# # int(p)
# p='p'
# print(ord(p))

d=dict(a=1,b=2)
f=open('datafile.pkl','wb')
import pickle
pickle.dump(d,f)
f.close()

f=open('datafile.pkl','rb')
e=pickle.load(f)
print(e)