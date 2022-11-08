def month(number_of_month):
    season = {
        1 :'January',
        2 : 'February',
        3 : 'March',
        4 : 'April', 
        5 : 'May',
        6 : 'June',
        7 : 'July',
        8 : 'August',
        9 : 'September', 
        10 : 'October',
        11 : 'Novemver',
        12 : 'December'
    }
    try:
        result = season[number_of_month]
    except KeyError as ke:
        print(f"{ke} - number is not in range(1, 12)") 
    except TypeError as te:
        print(f"{te} You need to input type 'number', not another type")
    else:
        return print(f"{number_of_month} month is {result}")

month(9)
        