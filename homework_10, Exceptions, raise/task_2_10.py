def uniq(list_of_numbers):
    try:
        # This will raise ValuError if i cannot be converted to an integer
        check_numbers = [int(i) for i in list_of_numbers]
    except ValueError as ve:
        print(f"List should have values with type numbers")
    except TypeError as te:
        print(f"{te} - is not list. Pass list.")
    else:
        if len(list_of_numbers) != len(set(list_of_numbers)):
            print("it's not uniq list")
            return False 
        print("it's uniq list") 
        return True
    
print(uniq([1, 2]))

    
        