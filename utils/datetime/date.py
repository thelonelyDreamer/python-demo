import re


def date_is_right(date):
    return re.match("\d{4}-\d{2}-\d{2}", date)


date1 = "2021-05-20"
date2 = "202-05-20"
date3 = "221-05-20"
date4 = "202105-20"

print(date1, date_is_right(date1))
print(date2, date_is_right(date2))
print(date3, date_is_right(date3))
print(date4, date_is_right(date4))
