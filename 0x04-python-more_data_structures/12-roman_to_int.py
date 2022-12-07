#!/usr/bin/python3
def to_subtract(list_num):
    sub = 0
    max_list = max(list_num)
    for i in list_num:
        if max_list > i:
            sub += i
    return (max_list - sub)


def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return (0)

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    last_rom = 0
    list_num = [0]
    for ch in roman_string:
        for r_num in list(rom_n.keys()):
            if r_num == ch:
                if rom_n.get(ch) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [rom_n.get(ch)]
                else:
                    list_num.append(rom_n.get(ch))
                last_rom = rom_n.get(ch)

    num += to_subtract(list_num)
    return (num)
