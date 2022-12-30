def min_max(data):
    result_min = data[0]
    result_max = data[0]
    for i in data:
        if i > result_max:
            result_max = i
        elif i < result_min:
            result_min = i

    return result_min,result_max
# ja pjerdole kurwa jego mac....
