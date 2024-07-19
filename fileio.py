s="Zara is awesome "

# Writing to the file
# with open("zara.txt", "w") as f:
#     f.write(s)
#
# # f=open("zara.txt", "w")
# # f.write(s)
# # f.close()
#
# # Reading to the file
# with open("zara.txt", "r") as f:
#     s=f.read()
#     print(s)
# # f=open("zara.txt", "r")
# # s=f.read()
# # print(s)

# # Appending to the file
with open("zara.txt", "a") as f:
    f.write("boom boom  ")

# # f=open("zara.txt", "a")
# # f.write("Boom boom ")
# # f.close()

# with open("meow.txt", "w") as m:
#     m.write(s)
#
# with open("meow.txt", "r") as m:
#     s=m.read()
#     print(s)

with open("meow.txt", "a") as m:
    m.write("billi bilii ")

