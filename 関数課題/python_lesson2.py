def get_prime_number(number):
    numbers = []

    for i in range(2, number + 1):
        flag = True

        for j in numbers:    # 修正
            if i % j ==0:
                flag = False
                break

        if flag == True:
            numbers.append(i)

    print(numbers)

get_prime_number(100)