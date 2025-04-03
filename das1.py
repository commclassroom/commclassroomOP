def printSpring():
    print("Хавар болж цэцэгс цэцэглэжээ.")

def printSummer():
    print("Зун болж халуун боллоо.")

def printFall():
    print("Намар болж навч уналаа.")

def printWinter():
    print("Өвөл болж цас орлоо.")

uliral = int(input("Улирлаа оруулна уу (1=Хавар, 2=Зун, 3=Намар, 4=Өвөл): "))

if uliral == 1:
    printSpring()
elif uliral == 2:
    printSummer()
elif uliral == 3:
    printFall()
elif uliral == 4:
    printWinter()
else:
    print("Буруу утга оруулсан байна.")
