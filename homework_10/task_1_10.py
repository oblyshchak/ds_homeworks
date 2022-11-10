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
    if not isinstance(number_of_month, int):
        raise TypeError("You need to input type 'number', not another type")
    try:
        result = season[number_of_month]
    except KeyError as ke:
        print(f"{ke} - is not a month, pass number from 1 to 12") 
    else:
        print(f"{number_of_month} month is {result}")
        return result

month(89)
        