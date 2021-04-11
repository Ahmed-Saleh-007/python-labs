def locations_of_char_in_str(string, char):
    lst = []
    for i in range(len(string)):
        if (string[i] == char):
            lst.append(i)       
    return lst

print(locations_of_char_in_str("Google", 'o'))