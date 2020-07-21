print("this program draws a 3 x 3 magic squares where all the vertical, horizontal, and diagonal lines add up to the same number.")

cen = int(input("Choose a number that's going to be in the center: "))
print(" ")

leng = len(str(cen))

while cen < 4 or leng > 4:
    print("input error, try again. The number can't be less than 4 or greater than 9999")
    print(" ")
    cen = int(input("Choose a number that's going to be in the center: "))
    print()

one = 4 + (cen - 5)  
two = 9 + (cen - 5)
thr = 2 + (cen - 5)
four = 3 + (cen - 5)
fv = cen
six = 7 + (cen - 5)
svn = 8 + (cen - 5)
egt = 1 + (cen - 5)
nine = 6 + (cen - 5)

line1 = "ㅡㅡㅡㅡㅡㅡ"
line2 = "ㅡㅡㅡㅡㅡㅡㅡ"
line3 = "ㅡㅡㅡㅡㅡㅡㅡㅡㅡ"
line4 = "ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ"

def drawline():
    if leng == 1:
        print(line1)
    elif leng == 2:
        print(line2)
    elif leng == 3:
        print(line3)
    elif leng == 4:
        print(line4)

print(one, "ㅣ", two, "ㅣ", thr)
drawline()
print(four, "ㅣ", fv, "ㅣ", six)
drawline()
print(svn, "ㅣ", egt, "ㅣ", nine)
