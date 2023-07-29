def input_user():
    input_numbers = []
    range_N = input("Please enter a number")

    for i in range(0, int(range_N)):
        num = input("Enter a number")
        input_numbers.append(num)

    for n, i in enumerate(input_numbers):
        print("tt = ", n)
        if i == find_num:
            print(n+1)
            break

    if n>=int(range_N): print(-1)

