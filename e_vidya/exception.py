def calculate_sum(list_of_expenditure):
    total=0
    
    try:
        for expenditure in list_of_expenditure:
            total+=expenditure
        print("Total:",total)
        avg=total/no_values
        print("Average:",avg)
    except ZeroDivisionError:
        print("Divide by Zero error")
    except NameError:
        print('Name Error occured')
    except TypeError:
        print("Wrong data type")
    except:
        print('some error occured')
list_of_values=[100,200,300,400,500]
nu_values=len(list_of_values)
calculate_sum(list_of_values)

