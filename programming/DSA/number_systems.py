# decimal to binary
def dectobin(dec):
    bin=[]
    while dec>0:
        r=dec%2
        bin.insert(0,r)
        dec=dec//2
    return bin
decimal_bin=int(input("Enter Decimal number to get Binary Number:"))
binary=dectobin(decimal_bin)
print(*binary,sep="")

# binary to decimal
def bintodec(bin):
    dec=0
    for i in bin:
        if i not in ['0','1']:
            return "Invalid Input!"
        dec=dec*2+int(i)
    return dec
binary1=input("Enter Binary Number to get Decimal Number:")
decimal1=bintodec(binary1)
print(decimal1)

# decimal to octal
def dectooctal(dec):
    oct=[]
    while dec>0:
        r1=dec%8
        oct.insert(0,r1)
        dec=dec//8
    return oct
decimal_1=int(input("Enter Decimal Number to get Octal Number:"))
octal1=dectooctal(decimal_1)
print(*octal1,sep="")

# octal to decimal
def octtodec(oct):
    dec=0
    for i in oct:
        if i not in ['0','1','2','3','4','5','6','7']:
            return "Invalid Input!"
        dec=dec*8+int(i)
    return dec
octal2=input("Enter the Octal Number to get Decimal Number:")
decimal_2=octtodec(octal2)
print(decimal_2)

# decimal to hexadecimal
def dectohex(dec):
    if dec==0:
        return ['0']
    hex_ch="0123456789ABCDEF"
    hex_list=[]
    while dec>0:
        r=dec%16
        hex_list.insert(0,hex_ch[r])
        dec=dec//16
    return hex_list
decimal_3=int(input("Enter Decimal Number to get Hexa Decimal Numbers:"))
hexa1=dectohex(decimal_3)
print(*hexa1,sep="")

# hexadecimal to decimal
def hextodec(hex):
    hex=hex.upper()
    hex_ch="0123456789ABCDEF"
    dec=0
    for i in hex:
        if i not in hex_ch:
            return "Invalid Input!"
        val=hex_ch.index(i)
        dec=dec*16+val
    return dec
hexa=input("Enter the Hexa Decimal Number to get Decimal Number:")
dec_val=hextodec(hexa)
print(dec_val)