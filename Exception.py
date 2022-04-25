# Exceptions are three types:
#   - called
#   - raised
#   - launched

# First method to handle exception
def get_half_even_number(number):
    if number % 2 == 0:
        return number / 2
    else:
        message = ("This Function only supports halving even numbers. "
                   f"Received: {number}")
        raise Exception(message)


print(get_half_even_number(3))


# Second method
def increase_percent(initial_value, after_value):
    try:
        return (after_value / initial_value) * 100
    except ZeroDivisionError:
        return 0
    except Exception as error:
        print("Uh oh, unexpected error occurred !")
        raise error
