def calculate_running_total(n, list_of_numbers):
    sum_of_numbers = 0
    product_of_numbers = 1
    has_zero = False
    has_three = False

    for number in list_of_numbers:
        sum_of_numbers += number
        product_of_numbers *= number

        if number == 0:
            has_zero = True

        if number == 3:
            has_three = True

        if number % 2 == 0:
            if has_zero:
                return 2* sum_of_numbers
            else:
                return sum_of_numbers
        else:
            if has_three:
                return product_of_numbers + 1
            else:
                return product_of_numbers


def get_n_and_generated_list():

    while True:
        try:
            n_str = input("Enter a leght of array: ")
            n = int(n_str)
            if n < 0:
                print("Please enter a positive integer.")
            else:
                return n
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
  n = get_n_and_generated_list()

  list_of_numbers = list(range(1, n +1))

  result = calculate_running_total(n, list_of_numbers)

