"""
file = open("myFile.txt","w")
file.write("myTekst")
file.close()
"""
import bookCreator as bookCreator
import sonya as log
import reader as reader
def main():
    print("1 - külalisteraamat")
    print("2 - ")
    userInput = input("Sinu valik: ")
    if userInput == "1":
        bookCreator.guestBook()
    elif userInput == "2":
        sonya.sonya()
    elif userInput == "3":
        userFile = input("Milline file sa tahad lugeda?")
        reader.readFile(userFile)
        
    else:
        print("vale valik")
        
main()