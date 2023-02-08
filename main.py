def main():
    ##################################################
    # Comlete your code here
    val1 = int(input('Value one : '))
    val2 = int(input('Value two : '))
    val3 = int(input('Value three : '))
    sum = val1 + val2 + val3; avg = sum/3
    print (f'\nValues:',val1, val2, val3)
    print(f'Total: \t\t{sum}\nAverage: \t{avg:.2f}')
    ##################################################

    pass


if __name__ == '__main__':
    main()
