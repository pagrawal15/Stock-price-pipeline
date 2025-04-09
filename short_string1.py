def short_string(s):
    prev = s[0]
    cnt = 1
    result = []

    for i in range(1,len(s)):
        if s[i] == prev:
            cnt+=1
        else:
            result.append(prev+str(cnt))
            prev = s[i]
            cnt = 1
    result.append(prev + str(cnt))

    compressed = "".join(result)
    return compressed if len(compressed) <len(s) else s

# test cases
if __name__ == "__main__":
    print(short_string("aaabbcccaaa"))  # a3b2c3a3
    print(short_string("abc"))         # abc
    print(short_string("a"))           # a
    # print(short_string(""))            # (empty string)
