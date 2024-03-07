from colorama import Fore, Back, Style # design choice, coloring output etc
import os # allows you to pass system commands, interact with the system 
import zipfile # what we are using to unzip the pass-protected zipfiles
import os.path # to check OS type
import time # debugging purposes
import itertools
import string
from os import system, name
from checksumdir import dirhash # used for hashing


# function used for clearing terminal output
def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

    return

def charTables(charOption):

    # Function holding all the charlist arrays for incremental password cracking

    charlist1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    charlist2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    charlist3 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "?", "&", "*"]
    
    charlist4 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "?", "&", "*", "~", "'", "^", "(", ")", "_", "-", "+","=", "{", "[", "}", "]", "|", ":", ";", '"', ",", ".", "<", ">", "/", "`", "\\"]
    
    charlist5 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
     
    charlist6 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    charlist7 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "?", "&", "*"]

    charlist8 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "?", "&", "*", "~", "'", "^", "(", ")", "_", "-", "+","=", "{", "[", "}", "]", "|", ":", ";", '"', ",", ".", "<", ">", "/", "`", "\\"] 

    charlist9 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
     
    charlist10 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    charlist11 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "?", "&", "*"]

    charlist12 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "?", "&", "*", "~", "'", "^", "(", ")", "_", "-", "+","=", "{", "[", "}", "]", "|", ":", ";", '"', ",", ".", "<", ">", "/", "`", "\\"]

    # If function for choosing charlist

    if charOption == 1:
        characterTable = charlist1
        return characterTable

    if charOption == 2:
        characterTable = charlist2
        return characterTable

    if charOption == 3:
        characterTable = charlist3
        return characterTable

    if charOption == 4:
        characterTable = charlist4
        return characterTable

    if charOption == 5:
        characterTable = charlist5
        return characterTable

    if charOption == 6:
        characterTable = charlist6
        return characterTable

    if charOption == 7:
        characterTable = charlist7
        return characterTable

    if charOption == 8:
        characterTable = charlist8
        return characterTable
    
    if charOption == 9:
        characterTable = charlist9
        return characterTable

    if charOption == 10:
        characterTable = charlist10
        return characterTable

    if charOption == 11:
        characterTable = charlist11
        return characterTable

    if charOption == 12:
        characterTable = charlist12
        return characterTable

    Exiting()

def incremental(targetFile):
    
    # Function to ask user for charlist to use for incremental

    while 1 == 1:   
        print("\n\n")
        print(Fore.MAGENTA + "Please choose what type of character list you want to use to brute force" )
    
        print(Fore.RED + "\n[Speed Ratings]\n")
        quickest = Fore.BLUE + " [quickest]"
        quick = Fore.MAGENTA + " [quick]"
        moderate = Fore.WHITE + " [moderate]"
        slow = Fore.GREEN + " [slow]"
        slowest = Fore.YELLOW + " [slowest]"

        print(quickest, Fore.RED + "Number of trials needed (8 character pass length) n < 300,000,000,000")
        print(quick, Fore.RED + "Number of trials needed (8 character pass length) n < 12,000,000,000,000")
        print(moderate, Fore.RED + "Number of trials needed (8 character pass length) n < 60,000,000,000,000")
        print(slow, Fore.RED + "Number of trials needed (8 character pass length) n < 520,000,000,000,000")
        print(slowest, Fore.RED + "Number of trials needed (8 character pass length) n < 6,100,000,000,000,000 \n\n")
    
        print(Fore.CYAN + "1.) ", Fore.RED + " lowercase letters only a-z (26 chars)", quickest)
        print(Fore.CYAN + "2.) ", Fore.RED + " lowercase letters and numbers a-z 0-9 (36 chars)", quick)
        print(Fore.CYAN + "3.) ", Fore.RED + " lowercase letters, numbers, and some symbols a-z 0-9 !?@#$%& (43 chars)", quick)
        print(Fore.CYAN + "4.) ", Fore.RED + " lowercase letters, numbers, and all symbols a-z 0-9 (68 chars)", slow)
        print(Fore.CYAN + "5.) ", Fore.RED + " uppercase letters only a-z (26 chars)", quickest)
        print(Fore.CYAN + "6.) ", Fore.RED + " uppercase letters and numbers a-z 0-9 (36 chars)", quick)
        print(Fore.CYAN + "7.) ", Fore.RED + " uppercase letters, numbers, and some symbols a-z 0-9 !?@#$%& (43 chars)", quick)
        print(Fore.CYAN + "8.) ", Fore.RED + " uppercase letters, numbers, and all symbols a-z 0-9 (68 chars)", slow)
        print(Fore.CYAN + "9.) ", Fore.RED + " all letters a-z A-Z (52 chars)", moderate)
        print(Fore.CYAN + "10.) ", Fore.RED + "all letters and numbers a-z A-Z 0-9 (62 chars)", slow)
        print(Fore.CYAN + "11.) ", Fore.RED + "all letters, numbers, and some symbols a-z A-Z 0-9 !?@#$%& (69 chars)", slow)
        print(Fore.CYAN + "12.) ", Fore.RED + "all letters, numbers, and all symbols a-z A-Z 0-9 (94 chars)", slowest)    
        print(Fore.CYAN + "99.) ", Fore.RED + "return to main menu")
        print()

        cOption = input(Fore.GREEN + "Bruteforce:Chartable select" + Fore.RED + "> ")
        charOption = int(cOption)

        if charOption > 0 and charOption < 13:
            Table = charTables(charOption)
            length = len(Table)
            init_gen(Table, length, targetFile)
        if charOption == 99:
            Exiting()
        else:
            print(charOption, error)

    return

def init_gen(cTable, leng, targetFile):

    # generates first pass list to initiate the recursive password gen

    print(cTable, leng)
   
    passlist = []
    
    for i in range(0, leng):
        passlist.append(cTable[i])
    pslength = len(passlist)
    CRCbypass(targetFile)
    generate_passwords(cTable, leng, passlist, pslength, targetFile)
    exit()

def generate_passwords(cTable, leng, passlist, pslength, targetFile):
    
    # A recursive function built upon a nested forloop to generate all password
    # permutations

    print(cTable, leng, passlist, pslength)
    newPasslist = []
    file = " hack-station/" + targetFile
    directory = "hack-station"
    md51 = dirhash(directory, 'md5')

    for i in range(0, pslength):
        for j in range(0, leng):
            password = passlist[i] + '' + cTable[j]
            pDisplay = Fore.CYAN + password
            

            print(pDisplay)
            bytePass = bytes(password, 'utf-8')
            with zipfile.ZipFile(targetFile) as zf:
                for name in zf.namelist():
                    try:
                        zf.extractall(path="hack-station", pwd = bytePass)
                    except zipfile.BadZipFile as e:
                        print("CRC CHECK WORKED")
                        md52 = dirhash(directory, 'md5')
                        

                    except RuntimeError:
                        print(Fore.MAGENTA + "[PASS CHECK FAILED]")
            
            md52 = dirhash(directory, 'md5')
            if md51 != md52:
                passFound(password)

            newPasslist.append(passlist[i] + '' + cTable[j])
             

    newPLeng = len(newPasslist)
    generate_passwords(cTable, leng, newPasslist, newPLeng, targetFile)
    return

def CRCbypass(targetFile):
    
    # Function to spit out all bad crc files to make sure bruteforce process
    # isnt stopped

    for i in range(0, 10000):
        passw = hash(i)
        password = str(passw)
        bytePass = bytes(password, 'utf-8')
        crcFile = "hack-station/" + targetFile
        with zipfile.ZipFile(crcFile) as zf:
            for name in zf.namelist():
                try:
                    zf.extractall(path="hack-station", pwd = bytePass)
                except zipfile.BadZipFile as e:
                    print(Fore.GREEN + "[CRC DODGED]")
                except RuntimeError:
                    print(Fore.MAGENTA + "[PASS CHECK FAILED]")

    
    return

def passFound(passw):
    
    # Function to display password when found

    correctPass = Fore.YELLOW + "[PASSWORD FOUND]"
    correctPassword = correctPass.center(73, " ")
    print("\n", correctPassword ,"\n")

    passwo = "     " + passw + "     "
    password = passwo.center(70, "$")
    for i in range(0,4):
        print(Fore.BLUE + "$"*70)
    print(Fore.CYAN + password)
    for i in range(0,4):
        print(Fore.BLUE + "$"*70)

    exit()

def wordlistSelect(targetFile):
    
    # Function to select wordlist

    dir_path = "wordlists"
    
    wordlists = []

    for file_path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file_path)):
            wordlists.append(file_path)
    
    print()
    
    wlength = len(wordlists)

  #  for i in range (0, wlength):
  #      print("[",i+1,"] ", wordlists[i])

    

    # This function will be responsible for using password files and wordlists and
    # testing them against password protected files
    n = 1
    while n == 1:
        for i in range (0, wlength):
            print("[",i+1,"] ", wordlists[i])
        print("\nEnter the number of the wordlist you wish to use.\n")
        listSelect = input(Fore.GREEN + "\nBruteforce:Wordlist Select" + Fore.RED + "> ")
         # exception handling for value errors
        try: 
            wOption = int(listSelect)
            n = 0
        except ValueError:
            print("\nYou did not enter an integer please try again.\n")
            n = 1

    if wOption > 0 and wOption < wlength+1:
            CRCbypass(targetFile)
            wordlist(targetFile, wordlists[wOption-1])
    else:
        print("The option you chose is not available please try again.")

def wordlist(targetFile, wFile):

    #function to read wordlist file and test passwords

    print(wFile)
    print(targetFile)
    directory = "hack-station"
    wDirectory = "wordlists"
    md51 = dirhash(directory, 'md5')
    zipF = directory + "/" + targetFile
    
    fileCommand = wDirectory + "/" + wFile
    file1 = open(fileCommand, 'r')
    count = 0
    while True:
        count += 1

        wPassword = file1.readline().replace("\n", "")
        pDisplay = Fore.CYAN + wPassword
        print(pDisplay)

        if not wPassword:
            print(" END OF WORDLIST REACHED ")
            break
        bytePass = bytes(wPassword, 'utf-8')
        with zipfile.ZipFile(zipF) as zf:
            for name in zf.namelist():
                try:
                    zf.extractall(path="hack-station", pwd = bytePass)
                except zipfile.BadZipFile as e:
                    print(Fore.GREEN + "[CRC CHECK DODGED]")
                    md52 = dirhash(directory, 'md5')
                        
                except RuntimeError:
                    print(Fore.MAGENTA + "[PASS CHECK FAILED]")
                md52 = dirhash(directory, 'md5')
                if md51 != md52:
                    passFound(wPassword)
    exit()

def options():
    # This function will ask user whether they brute forcing WPA handshakes or
    # zip protected files
    while 1 == 1:
        print("\n\n")
        print(Fore.MAGENTA + "Please choose what type of files you wish to brute force" )
        print(Fore.CYAN + "1.) ", Fore.RED + " Password Protected Files ")
        print(Fore.CYAN + "2.) ", Fore.RED + " WPA handshake PCAP Files ")
        print(Fore.CYAN + "99.) ", Fore.RED + "To exit out of program ")
        print()    
        fOption = input(Fore.GREEN + "Bruteforce:options" + Fore.RED + "> ")
    
        if fOption == '1':
            fileOptions()
        if fOption == '2':
            wpaOptions()
        if fOption == '99':
            Exiting()
        else:
            print(fOption, error)

def fileOptions():
    
    # function to get file that user wants to brute force

    t = os.system("pwd")
    print(t)
    while 1 == 1:
        print(Fore.MAGENTA + "\nPlease enter password protected file you wish to crack ")
        targetPath = input(Fore.GREEN + "\nBruteforce: File Select"+ Fore.RED + "> ")
        
        check = os.path.exists(targetPath)
        
        # checks if file exists

        if check == False:
            print("\n ERROR >>> File doesnt exist \n")
        if check == True:
            command = "cp "
            command2 = " hack-station"
            fCommand = command + targetPath + command2
            
            os.system(fCommand)
            fTarget = targetPath.rfind("/")
            targetFile = targetPath[fTarget+1:]
            print(targetFile)
            break

    while 1 == 1:
        print("\n\n")
        print(Fore.MAGENTA + "Please choose what type of brute forcing you intend to do" )
        print(Fore.CYAN + "1.) ", Fore.RED + " Incremental ")
        print(Fore.CYAN + "2.) ", Fore.RED + " Wordlists ")
        print(Fore.CYAN + "99.) ", Fore.RED + "Return to main menu")
        print()

        hackOption = input(Fore.GREEN + "Bruteforce:Cracking Method" + Fore.RED + "> ")
    
        # menu options

        if hackOption == '1':
            incremental(targetFile)
        if hackOption == '2':
            wordlistSelect(targetFile)
        if hackOption == '99':
            options()
        else:
            print(hackOption, error)


    # If user picked zip protected files they will be brought to this function
    # to decide whether they want to do incremental encryption or wordlist
    # cracking
    


        return

def wpaOptions():
    # WIP
    return
def Exiting():
    clear()
    quit()

def mainMenu():
    # initializes everything

    a = "             ____          ___               __          \n"
    b = "            /  _/______   / _ )_______ ___ _/ /_____ ____\n"
    c = "           _/ // __/ -_) / _  / __/ -_) _ `/  '_/ -_) __/ \n"
    d = "          /___/\__/\__/ /____/_/  \__/\_,_/_/\_\|__/_/    \n"
    n = a + b + c + d

    toolName = n.center(100, " ")
    print(Fore.WHITE + toolName)

    # Fore. from colorama library
    welcomeMessage = Fore.MAGENTA + " " + Fore.YELLOW + "a python bruteforce tool "
    Version = Fore.MAGENTA + "Ver: " + Fore.YELLOW + " 1.0.0"
    Github = Fore.MAGENTA + "Github: " + Fore.YELLOW + "https://github.com/AP0LL0916/Capstone-Bruteforce "

    welM = welcomeMessage.center(70, " ")
    Ver = Version.center(70, " ")
    Git = Github.center(70, " ")

    print(Fore.RED + "[---]", Fore.BLUE + welM, Fore.RED + "[---]")
    print(Fore.RED + "[---]", Fore.BLUE + Ver, Fore.RED + "[---]")
    print(Fore.RED + "[---]", Fore.BLUE + Git, Fore.RED + "[---]")
    
    stCheck = "hack-station"
    if os.path.exists(stCheck) == False:
        os.system("mkdir hack-station")

    options()

error = " is not an available choice please enter your desired option's number."
mainMenu()


