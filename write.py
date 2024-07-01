# with open('./about.txt','w') as file:
#     file.write()
    

# #other work

# with open('./about.txt','a') as file:
#     file.write()

lists=['I am thet paing oo','\nI am 24 years old']

with open('./about.txt','a') as file:
    file.writelines(lists)