import pyfiglet

def convert(text):
    result = pyfiglet.figlet_format(text)
    return result

def convertwithstyle(text, style):
    result = pyfiglet.figlet_format(text, font=style)
    return result

def typeofstyle(n):
    l = ["", "bubble", "digital", "3-d", "slant", "3x5"]
    return l[n]

def save(text, filename):
    with open(filename, 'w') as f:
        f.write(text)
        f.close()
    print("Saved!")
def main():
    ascii = ""
    print(pyfiglet.figlet_format("The ASCII Art Creator!"))
    print("Convert any text to ASCII Art!!")
    print("Developed by Srijan Dutta\n\n")
    while(True):
        text = input("Enter the text you want to convert:")
        print("Choose from the following font styles(default -> standard):\n1. Bubble\n2. Digital\n3. 3-D\n4. Slant\n5. 3x5\n")
        n = input()
        if len(n) > 0:
            x = int(n)
            style = typeofstyle(x)
            ascii = convertwithstyle(text, style)
        else:
            ascii = convert(text)
        print(ascii)
        x = input("Do you want to save it to text file(y/n)?")
        if x == 'y':
            file = input("Enter the file name:")
            save(ascii, filename=file)
    

if __name__ == "__main__":
    main()
