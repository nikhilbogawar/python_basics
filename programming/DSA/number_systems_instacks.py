# Q1 - Decimal to Binary
def dectobin(dec):
    bin = []
    while dec > 0:
        r = dec % 2
        bin.insert(0, r)
        dec = dec // 2
    return bin

dec = int(input())
dec = abs(dec)

if dec == 0:
    print("Zero")
else:
    bin = dectobin(dec)
    print(*bin, sep="")

#----------------------------------------------------------------------------

# Q3 - Decimal to Hexadecimal
dec = int(input())
hexdec = []
dec = abs(dec)

if dec == 0:
    print("Given Input is Invalid.")
else:
    while dec > 0:
        r = dec % 16
        if r <= 9:
            hexdec.append(str(r))
        else:
            hexdec.append(chr(r + 55))
        dec = dec // 16
    hd = "".join(hexdec)
    print(hd[::-1])

#-------------------------------------------------------------------------

# Q4 - Binary to Decimal
bin = input()
dec = 0
c = 0

for i in range(len(bin) - 1, -1, -1):
    ch = bin[i]
    if ch == '0' or ch == '1':
        val = int(ch)
        dec += val * (2 ** c)
        c += 1
    else:
        print("Invalid Input.")
        break
else:
    print(dec)

#-----------------------------------------------------------------------------

# Q5 - Binary to Octal
bin = input().strip()
dec = 0
c = 0

for i in range(len(bin) - 1, -1, -1):
    ch = bin[i]
    if ch == '0' or ch == '1':
        val = int(ch)
        dec += val * (2 ** c)
        c += 1
    else:
        print("Invalid Input")
        break
else:
    if dec == 0:
        print("0")
    else:
        def dectooct(dec):
            octal = []
            while dec > 0:
                r = dec % 8
                octal.insert(0, r)
                dec = dec // 8
            return octal
        octal = dectooct(dec)
        print(*octal, sep="")

#-------------------------------------------------------------------

# Q7 - Octal to Binary
octal = input().strip()
dec = 0
c = 0
valid = True

for i in range(len(octal) - 1, -1, -1):
    ch = octal[i]
    if ch >= '0' and ch <= '7':
        val = int(ch)
        dec += val * (8 ** c)
        c += 1
    else:
        print("Invalid Input")
        valid = False
        break

if valid:
    if dec == 0:
        print("0")
    else:
        def dectobin(dec):
            bin = []
            while dec > 0:
                r = dec % 2
                bin.insert(0, r)
                dec = dec // 2
            return bin
        bin = dectobin(dec)
        print(*bin, sep="")

#--------------------------------------------------------------------

# Q8 - Octal to Decimal
octal = input().strip()
if octal.startswith('-'):
    octal = octal[1:]

dec = 0
c = 0

for i in range(len(octal) - 1, -1, -1):
    ch = octal[i]
    if ch >= '0' and ch <= '7':
        val = int(ch)
        dec += val * (8 ** c)
        c += 1
    else:
        print("Invalid Input")
        break
else:
    print(dec)

#--------------------------------------------------------------------

# Q9 - Octal to Hexadecimal
octal = input().strip()
if octal.startswith('-'):
    octal = octal[1:]

dec = 0
c = 0

for i in range(len(octal) - 1, -1, -1):
    ch = octal[i]
    if ch >= '0' and ch <= '7':
        val = int(ch)
        dec += val * (8 ** c)
        c += 1
    else:
        print("Invalid Input")
        break
else:
    hexdec = []
    while dec > 0:
        r = dec % 16
        if r <= 9:
            hexdec.append(str(r))
        else:
            hexdec.append(chr(r + 55))
        dec = dec // 16
    hd = "".join(hexdec[::-1])
    print(hd)

#--------------------------------------------------------------------

# Q10 - Hexadecimal to Binary
hd = input().strip().upper()
dec = 0
c = 0
valid = True

for i in range(len(hd) - 1, -1, -1):
    ch = hd[i]
    if (ch >= '0' and ch <= '9') or (ch >= 'A' and ch <= 'F'):
        val = int(ch) if ch.isdigit() else ord(ch) - 55
        dec += val * (16 ** c)
        c += 1
    else:
        print("Invalid Characters")
        valid = False
        break

if valid:
    if dec == 0:
        print("0")
    else:
        def dectobin(dec):
            bin = []
            while dec > 0:
                r = dec % 2
                bin.insert(0, r)
                dec = dec // 2
            return bin
        bin = dectobin(dec)
        print(*bin, sep="")

#----------------------------------------------------------------------

# Q11 - Hexadecimal to Decimal
org_bin = input().strip()
bin = org_bin.replace('-', "")
bin = bin.upper()

dec = 0
c = 0

for i in range(len(bin) - 1, -1, -1):
    ch = bin[i]
    if (ch >= '0' and ch <= '9') or (ch >= 'A' and ch <= 'F'):
        val = int(ch) if ch.isdigit() else ord(ch) - 55
        dec += val * (16 ** c)
        c += 1
print(f"{org_bin} -> {dec}")

#---------------------------------------------------------------------------

# Q12 - Hexadecimal to Octal
hd = input().strip()
neg = hd.startswith('-')
hexd = hd[1:].upper() if neg else hd.upper()

dec = 0
c = 0
valid = True

for i in range(len(hexd) - 1, -1, -1):
    ch = hexd[i]
    if (ch >= '0' and ch <= '9') or (ch >= 'A' and ch <= 'F'):
        val = int(ch) if ch.isdigit() else ord(ch) - 55
        dec += val * (16 ** c)
        c += 1
    else:
        print("Invalid Input")
        valid = False
        break

if valid:
    if dec == 0:
        octal = "0"
    else:
        def dectooct(dec):
            octal = []
            while dec > 0:
                r = dec % 8
                octal.insert(0, str(r))
                dec = dec // 8
            return "".join(octal)
        octal = dectooct(dec)

    if neg:
        print(f"{hd} -> {octal}")
    else:
        print(octal)

#----------------------------------------------------------------------------

# binary to hexa decimal
bin=input().strip()
dec=0
c=0
valid=True
for i in range(len(bin)-1,-1,-1):
    ch=bin[i]
    if ch=='0' or ch=='1':
        val=int(ch)
        dec+=val*(2**c)
        c+=1
    else:
        print("Invalid input")
        valid=False
        break
if valid==True:
    if dec==0:
        print('0')
    else:
        hexdec=[]
        while dec>0:
            r=dec%16
            if r<=9:
                hexdec.append(str(r))
            else:
                hexdec.append(chr(r+55))
            dec=dec//16
        hd="".join(hexdec)
        print(hd[::-1])

#-------------------------------------------------------------------------

# decimal to octal
def dectooct(dec):
    oct=[]
    while dec>0:
        r=dec%8
        oct.insert(0,r)
        dec=dec//8
    return oct
dec=int(input())
if dec==0:
    print("ZERO")
elif dec<0:
    print("INVALID Input")
else:
    oct=dectooct(dec)
    print(*oct,sep="")