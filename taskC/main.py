def DecimalToSeventh(decimal_num):
    seventh_num = ''
    if decimal_num == 0:
        return 0
    while decimal_num > 0:
        remainder = decimal_num % 7
        seventh_num = str(remainder) + seventh_num
        decimal_num //= 7

    return seventh_num

d_input = int(input())
s_output = DecimalToSeventh(d_input)
print(s_output)
