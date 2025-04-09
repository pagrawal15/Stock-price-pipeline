def count_users(emails):
    
    domain = []
    for e in emails:
        s = e.split("@")
        domain.append(s[-1])
    
    freq_dict = {}

    for d in domain:
        if d not in freq_dict:
            freq_dict[d] = 1
        else:
            freq_dict[d] += 1
   
    return freq_dict

# Test. cases

if __name__ == "__main__":
    emails = [
    "alice@meta.com",
    "bob@openai.com",
    "carol@meta.com",
    "dave@openai.com",
    "eve@amazon.com"
]
