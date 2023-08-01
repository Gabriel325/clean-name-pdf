from . import upperCase_caracter as upperCase

upperCase_caracter_list = upperCase.upperCase_caracter

def change_caracter_in_name(name):
    
    for item in enumerate(name):
        lib_a = ["á" , "â" , "à" , "ä" , "ã"]
        lib_e = ["é" , "ê" , "è" , "ë"]
        lib_i = ["í" , "î" , "ì" , "ï"]
        lib_o = ["ó" , "ô" , "ò" , "ö" , "õ"]
        lib_u = ["ú" , "û" , "ù" , "ü"]
        lib_special = [" " , "_" , "." , ";" , ">" , "<" , "(" , ")"]

        index = item[0]
        letter = item[1]

        match letter:
            case letter if letter in lib_special:
                name[index] = "-"

            case letter if letter in upperCase_caracter_list(lib_a):
                name[index] = "A"

            case letter if letter in upperCase_caracter_list(lib_e):
                name[index] = "E"

            case letter if letter in upperCase_caracter_list(lib_i):
                name[index] = "I"

            case letter if letter in upperCase_caracter_list(lib_o):
                name[index] = "O"

            case letter if letter in upperCase_caracter_list(lib_u):
                name[index] = "U"

            case letter if letter in lib_a:
                name[index] = "a"
          
            case letter if letter in lib_e:
                name[index] = "e"

            case letter if letter in lib_i:
                name[index] = "i"

            case letter if letter in lib_o:
                name[index] = "o"

            case letter if letter in lib_u:
                name[index] = "u"
            
            case "Ç":
                name[index] = "C"

            case "ç":
                name[index] = "c"   
            case _:
                name[index] = letter     
                
    return name