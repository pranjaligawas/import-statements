while True:
    choice = int(input('\nEnter Choice:\n1.Add\t2.Sub\n3.Mul\t4.Div\n5.Exponent\t6.Exit'))
    match choice:
        case 1:
            print('Addition')
            fn = int(input('Enter first number'))
            sn = int(input('Enter second number'))
            print('Addition = ', fn+sn)
        case 2:
            print('Subtraction')
            fn = int(input('Enter first number'))
            sn = int(input('Enter second number'))
            print('Subtraction = ', fn-sn)
        case 3:
            print('Mulplication')
            fn = int(input('Enter first number'))
            sn = int(input('Enter second number'))
            print('Mulplication = ', fn*sn)
        case 4:
            print('Division')
            fn = int(input('Enter first number'))
            sn = int(input('Enter second number'))
            print('Division = ', fn/sn)
        case 5:
            print('Exponent')
            fn = int(input('Enter first number'))
            sn = int(input('Enter second number'))
            print('Ans = ', fn**sn)   
        case 6:
            print('Exit')
            break
        case _:
            print('Invalid input')
