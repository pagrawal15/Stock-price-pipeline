def product_category(data):
    a = {}
    for d in data:
        fruit_list = d.split(':')
        if fruit_list[0] not in a:
            a[fruit_list[0]] = [fruit_list[1]]
        else:
            a[fruit_list[0]].append(fruit_list[1])
    
    return a

if __name__ == "__main__":
    data = [
    "fruit:apple",
    "fruit:banana",
    "veg:carrot",
    "fruit:kiwi",
    "veg:broccoli"
]

print(product_category(data))

