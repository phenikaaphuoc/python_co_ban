
map = {
    10:"A",
    11:"B",
    12:"C",
    13:"D",
    14:"E",
    15:"F"
}
for value in range(9):
    map[value] = value
    
def convert10tobase(value,base = 2):
    result = ""
    while value >0:
        result = str(map[value%base]) +result
        value = value//base
        
    return result

    

if __name__ =="__main__":
    value = 31
    base = 16
    print(convert10tobase(value,base))