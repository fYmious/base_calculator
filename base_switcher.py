def base_switcher(num, start_base, final_base):
    tenth_base = int(str(num), start_base)
    result = ''
    while tenth_base > 0:
        result = str(tenth_base % final_base) + result
        tenth_base = tenth_base // final_base
    return result


print(base_switcher(5795, 15, 11))