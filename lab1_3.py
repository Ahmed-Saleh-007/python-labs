
#problem3 combine_strs

def combine_strs(a, b):
    a_front = a[0:len(a) // 2   if len(a) % 2 == 0 else ((len(a) // 2) + 1)]
    a_back  = a[((len(a) // 2)) if len(a) % 2 == 0 else ((len(a) // 2) + 1):len(a)]
    b_front = b[0:len(b) // 2   if len(b) % 2 == 0 else ((len(b) // 2) + 1)]
    b_back  = b[((len(b) // 2)) if len(b) % 2 == 0 else ((len(b) // 2) + 1):len(b)]
    combined_str = (a_front + b_front) + (a_back + b_back)
    return combined_str

print(combine_strs("abecd", "abcd"))
