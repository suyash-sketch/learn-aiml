# d = {10:100, 20:200, 30:300, 40:400}

# # print(d)

# # d[10] = 1000
# # print(d)

# # d.update({50:500})
# # print(d)

# # for i in d:
# #     print(d[i])


# # Deep copy 
# # a = [1,2,3,4,5]

# # b = a

# # b[0] = 100 # even if the value is not given to list 'a' this copies 100 to a

# # print(a)

# #shallow copy
# b = a.copy()

# b[0] = 200

# print(a)
# print(b)


#Merge two dictionary
# d1 = {10:100, 20:200, 30:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)

a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]

d = {}
for i in a:
    if i in d.keys():
        d[i] +=1
    else:
        d[i] = 1

print(d)
 
