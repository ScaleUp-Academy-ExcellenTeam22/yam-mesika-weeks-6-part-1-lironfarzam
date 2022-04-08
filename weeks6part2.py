def my_filter(func, iterable):
    """
    Function to copy the action of filter
    :param func: function to filter out
    :param iterable: iterable object
    :return: anyone who survived the filter
    """
    for i in iterable:
        if func(i):
            yield i


def get_positive_numbers() -> list:
    """
    Receives input from the user.
    The function will return all the positive numbers that the user entered, as a list of int numbers.
    :return: List of positive int numbers
    """
    input_string = input("Enter a series of numbers separated by a comma: ")
    input_list = input_string.split(",")
    int_list = map(lambda x: int(x), input_list)
    positive_list = list(filter(lambda x: x > 0, int_list))
    # # You can write short like that but it feels too busy
    # positive_list = list(filter(lambda x: x > 0, map(lambda x: int(x), input_string.split(","))))
    return positive_list


def timer(func, *args):
    """
    Function receives as a function parameter and other parameters,
    will measure how long a function ran when the same parameters are passed to it
    :param func: Function to run
    :param args: Parameters are passed to it
    :return: The time it took for the function to run
    """
    import time
    start = time.time()
    func(*args)
    end = time.time()

    return end - start


if __name__ == '__main__':

    temp_list_for_test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list_after_filter = list(my_filter(lambda x: x % 2 == 0, temp_list_for_test))
    print(new_list_after_filter)

    # 1,2,3,4,5,6,7,8,8,1,-5,-5,-5,-5,-5,-5,-5,-59
    print(get_positive_numbers())
