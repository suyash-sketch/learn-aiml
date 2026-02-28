# l = [12,16,13,19, 17]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i

# print(sec_largest, largest)


#Determine if the list is sorted
a = [12,13,14,15,16]

for i in range(len(a) -1):
    if a[i] < a[i + 1]:
        continue
    else:
        print("The list is not sorted")
        break
else:
    print("The list is sorted")