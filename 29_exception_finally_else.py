def get_value():
    result = None
    try:
        x, y = map(int, input('Enter two numbers: ').split())
        result = x / y
    except ZeroDivisionError as error:
        print('Error: ' + str(error))
    except ValueError as error:
        print('Error: ' + str(error))
    else:
        print('Program was finished without errors')
    finally:
        if result is not None:
            print(f'Result: {result}')
        else:
            print('Something went wrong')


get_value()
