# f= open("test.txt","w+")
# for i in range(10):
#      f.write("This is line %d\r\n" % (i+1))
# f.close() 

aux = "holaZEO"

s = "This be a string"
if aux.upper().find("ZEO") == -1:
    print("No 'is' here!")
else:
    print ("Found 'is' in the string.")