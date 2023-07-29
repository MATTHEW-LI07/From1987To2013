'''You might be surprised to know that 2013 is the first year since 1987 with distinct digits. The years
2014, 2015, 2016, 2017, 2018, 2019 each have distinct digits. 2012 does not have distinct digits,
since the digit 2 is repeated.
Given a year, what is the next year with distinct digits?
Input Specification
The input consists of one integer Y (0 ≤ Y ≤ 10000), representing the starting year'''


def next_distinct_year(year):
    while True:
        year += 1
        year_str = str(year)
        unique_digits = set()

        for digit in year_str:
            if digit in unique_digits:
                break
                unique_digits.add(digit)
            else:
                return year


next_year = next_distinct_year(int(input_year))

print(next_year)
