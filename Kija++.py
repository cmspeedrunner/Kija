num_to_char = {value+1:char for value, char in enumerate(R"""ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-={}|[]\;:'"<>,./? m""")}
def find_between(s, first, last):
        try: return [start:=s.index(first)+len(first), end:=s.index(last,start), s[start:end]][-1]
        except ValueError: return ""

try: 
    with open(flnm:=str(input("Enter file name to run:\n")),'r') as file: contents = file.read().strip()
except(FileNotFoundError):
    print("\n\033[31m\033[1m\033[4m"+flnm+"\033[0m")
    print("\033[31m\033[1m^"*len(flnm)+"\n")
    print("\033[31m\033[1m\033[4m'"+flnm+"' File not found in working directory.\033[0m")
    print("\033[35m\033[1m\033[4mHelp: Try changing working directory to the location of your file or drag the file into your working directory\033[0m\n")

try: contents = contents.splitlines()
except(NameError): exit()

def anal(): print(eval(''.join((content:=find_between(item, "(",")"), newlist:=[int(string) for string in content.split("-")], gewlist:=[num_to_char[num] if num in num_to_char else num for num in newlist])[-1] if item.split("(")[0] == ">>" else '')))
for i, item in enumerate(contents): anal()
