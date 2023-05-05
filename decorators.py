def plus_one(number):
    def add_one(number):
        return number + 1


    result = add_one(number)
    return result
x = plus_one(4)
print(x)