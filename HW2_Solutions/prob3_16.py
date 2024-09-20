def days(mo, da, leap):
    """
    convert months and days into days since year beginning
    input:
       mo : numeral for the month, 1 – 12
       da : numeral for the day of the month, 1 - 31
       leap : True if leap year, False if not leap year
     output:
        sumdays : number of days since year beginning
     """
    modays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap:
        modays[1] = 29
    sumdays = 0
    for i in range(mo-1):
        sumdays = sumdays + modays[i]
    sumdays = sumdays + da
    return sumdays


# Jan 1, 2021
print('Jan 1, 2021 = ', days(1, 1, False))
# Feb 29, 2020
print('Feb 29, 2020 = ', days(2, 29, True))
# Mar 1, 2022
print('Mar 1, 2022 = ', days(3, 1, False))
# Jun 21, 2024
print('Jun 21, 2024 = ', days(6, 21, True))
# Dec 31, 2020
print('Dec 31, 2024 = ', days(12, 31, True))
