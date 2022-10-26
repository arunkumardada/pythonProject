# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    file1 = open('mytextfile.txt', 'w')
    file2 = open('mytextfile2.txt', 'w')

    X = [] * 10000
    Y = []
    Z = []

    for i in range(1, 10001, 1):
        X.append(i)
    print(X)

    for number in range(1, 10000, 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                Y.append(number)
                file1.write(str(number) + '\n')

    print(Y)
    file1.close()

    for index, value in enumerate(Y, 1):
        if index in Y:
            continue
        else:
            Z.append(Y[index - 1])
            file2.write(str(Y[index - 1]) + '\n')
    print(Z)
    file2.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
