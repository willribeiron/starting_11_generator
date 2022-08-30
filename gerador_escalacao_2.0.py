from generator import generate_team

print("Welcome to the Tottenham Hotspur's starting 11 generator!")
print('Type the number of your tactical formation option:')
choice = int(input('1 - 3-4-3 | 2 - 3-5-2 | 3 - 4-4-2 | 4 - 4-3-3 '))
if choice == 1:
    generate_team(3, 1, 2, 1, 3)
elif choice == 2:
    generate_team(3, 1, 3, 1, 2)
elif choice == 3:
    generate_team(4, 1, 2, 1, 2)
elif choice == 4:
    generate_team(2, 1, 3, 1, 3)
else:
    print('Type the number of your option only')
