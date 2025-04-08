def freq_error_mesages(errors,k):
    freq_dict ={}

    for error in errors:
        if error not in freq_dict:
            freq_dict[error] = 1
        else:
            freq_dict[error] += 1
    # sort the dictionary based upon values

    freq_dict_sort = dict(sorted(freq_dict.items(), key = lambda item: (-item[1], item[0])))
    # we extract the top k names
    result = []
    for i in range(k):
        result.append(sorted_errors[i][0])
    return result

#  test cases

if __name__ == "__main__":
    errors = [
        "timeout",
        "disk full",
        "timeout",
        "cpu high",
        "disk full",
        "disk full",
        "cpu high"
    ]

    k = 2

    output = freq_error_messages(errors, k)
    print("Top K Frequent Errors:", output)


