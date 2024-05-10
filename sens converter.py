def cs2_to_val(cs2_sens):
    cs2 = float(cs2_sens)
    valorant = cs2 / 3.182
    return round(valorant, 2)
    

def val_to_cs2(val_sens):
    valorant = float(val_sens)
    cs2 = valorant * 3.182
    return round(cs2, 2)

def main():
    print('Welcome to my sensitivity converter')
    print('Here you will be able to convert your VALORANT/CS2 sensitivities interchangeably')
    print('Type 1 or 2 to choose the game you want to convert to and from.')
    print('1. CS2 to Valorant')
    print('2. VALORANT to CS2')

    choice = input('----> ')

    if choice == "1":
        cs2_sens = input('Etner your CS2 sens: ')
        val_sens = cs2_to_val(cs2_sens)
        print(f'Your VALORANT sens is: {val_sens}')
    elif choice == "2":
        val_sens = input('Enter your VALORANT sens: ')
        cs2_sens = val_to_cs2(val_sens)
        print(f'Your CS2 sens is: {cs2_sens}')
    else:
        print('Please choose 1 or 2')

if __name__ == "__main__":
    main()
