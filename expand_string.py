def expand_string(s):

    result =[]

    for i in range(0,len(s),2):
        current = s[i]
        count = int(s[i+1])
        result.append(current * count)
    return "".join(result)

