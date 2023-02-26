flnm = str(input("Enter file name to run:\n"))
num_to_char = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
               11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S',
               20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z',
               27: '0', 28: '1', 29: '2', 30: '3', 31: '4', 32: '5', 33: '6', 34: '7', 35: '8',
               36: '9', 37: '!', 38: '@', 39: '#', 40: '$', 41: '%', 42: '^', 43: '&', 44: '*',
               45: '(', 46: ')', 47: '_', 48: '+', 49: '-', 50: '=', 51: '{', 52: '}', 53: '|',
               54: '[', 55: ']', 56: '\\', 57: ';', 58: ':', 59: '\'', 60: '\"', 61: '<', 62: '>',
               63: ',', 64: '.', 65: '/', 66: '?', 67: ' ',68: 'm'}
btt = [60,56,30,30,54,27,57,30,32,68,8,5,12,12,15,63,67,20,8,9,19,67,9,19,67,11,9,10,1,56,27,30,30,54,27,68,60]
str = "\033[0;35mHELLO, THIS IS KIJA\033[0m"
def find_between( s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""

#####---CATCHING FILENOTFOUND ERROR---#####
try:
    with open(flnm,'r') as file:
        contents = file.read()
        contents = contents.strip()
        

except(FileNotFoundError):
    print("\n\033[31m\033[1m\033[4m"+flnm+"\033[0m")
    print("\033[31m\033[1m^"*len(flnm)+"\n")
    print("\033[31m\033[1m\033[4m'"+flnm+"' File not found in working directory.\033[0m")
    print("\033[35m\033[1m\033[4mHelp: Try changing working directory to the location of your file or drag the file into your working directory\033[0m\n")
try:
    contents = contents.splitlines()
except(NameError):
    exit()

def anal():

    idx = item.split("(")[0]

    if idx == ">>":
        content = find_between(item, "(",")")
        original_list = content.split("-")
        newlist = []
        gewlist = []
        
        
    for string in original_list:
        newlist.append(int(string))
    
    for num in newlist:
        if num in num_to_char:
            gewlist.append(num_to_char[num])
        else:
            gewlist.append(num)
    result = ''.join(gewlist)
    print(eval(result))


for i, item in enumerate(contents):
    anal()
