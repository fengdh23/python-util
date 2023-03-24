from decimal import getcontext, Decimal

getcontext().prec = 3000

division = Decimal(1) / Decimal(998001)

division_str = str(division)
decimals_str = division_str.split('.')[1]

counter = 0

for _ in range(999):
    lower_bound = counter *3
    upper_bound = lower_bound +3
    digits = decimals_str[lower_bound:upper_bound]
    digits_int = int(digits)
    counter__text = f"{counter:03d}"
    number_text = f"{counter:03d}"
    if counter__text == number_text:
        pass
    else:
        print(f'{counter__text} - {number_text}') # 998 0999
    counter +=1