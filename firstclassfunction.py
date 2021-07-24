# dictionary comprehension

mydictionary = 1, "pradeep", "age"}
print (mydictionary)
print (mydictionary[0])
print (mydictionary[1])

users = [(0, "bob", "xyz"), (1, "pradeep", "abc"), (2, "sandy", "def")]
username_mapping ={user[1]:user for user in users}
print (username_mapping)

# print ((lambda x,y:x+y)(3,4))

# def double(x):
#     return x*x
#
# sequence = [5,2,3,4]
#
# #result = [x*x for x in sequence]
# #result = [double(x) for x in sequence]
# result = list(map(double,sequence))
# print (result)


# def add(x,y):
#     #print (x+y)
#     return (x+y)
#
# print(add(3,3))
# add(2,3)
# rr=add(2,3)
# print (rr)


# def join_string(*args):
#     result =""
#     items = [item for item in args]
#     print(items)
#     for i in items:
#         if (len(result)==0):
#             result = i
#         else:
#             print (i)
#             result = result +"."+ i
#     return result
#
# print (join_string("pradeep,dds"))

# def test_args(*args):
#     lists = [item for item in args]
#     print (lists)
#
# test_args('Sun','Rain','Storm','Wind')

#
# def first_class(func,args):
#     return func(args)
#
# args="abc,pad"
#
# print (first_class(join_string,args))
#
