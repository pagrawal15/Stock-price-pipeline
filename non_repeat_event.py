def non_repeat_event(events):
    freq = {}

    for i in events:
        if i not in freq:
            freq[i] =1
        else:
            freq[i] += 1
    
    for  e in events:
        if freq[e] == 1:
            return e
    
    return 'NO Unique Value'


#  Test cases

if __name__ == "__main__":
    print(non_repeat_event(["click", "scroll", "click", "zoom", "scroll", "hover"]))  # zoom
    print(non_repeat_event(["a", "b", "a", "b"]))  # NO_UNIQUE
