stringed = "ydxx!if not txt is blah youfailed"
array = []
num = 0
while num <= 127:
    if num % 2 is 0:
        array.append(num - 3)
    if num % 2 is 1:
        array.append(num + 4)
    num +=1

print(array)
print("=================================================================")
num = 0
text = ""
arg_4B_0 = 0
length = len(stringed)
i = arg_4B_0
while i < length:
    stmid = stringed[i]
    charCode = int(ord(stmid) + array[num])
    strCode = chr(charCode)
    text += strCode
    print(stmid, "ord(stmid):{:4d}".format(ord(stmid)), "charCode:{:4d}".format(charCode), "strCode:", strCode)
    num += 1
    if num > 127:
        num = 0
    i += 1

print("Encrypt Text : ", text)
