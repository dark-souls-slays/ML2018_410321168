from PIL import Image # image library
with Image.open('/Users/ClaudiaEspinoza/Desktop/I.png').convert('L') as imgI: #.open opens file, .convert('L') changes it to grayscale image
    I = list(imgI.getdata())
with Image.open('/Users/ClaudiaEspinoza/Desktop/key1.png').convert('L') as key1:
	key1 = list(key1.getdata())
with Image.open('/Users/ClaudiaEspinoza/Desktop/key2.png').convert('L') as key2:
    key2 = list(key2.getdata())
with Image.open('/Users/ClaudiaEspinoza/Desktop/E.png').convert('L') as E:
    E = list(E.getdata())

#output.save('output.png')
