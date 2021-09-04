from colorama import Fore, Style
n, m = map(int, input().split())
print('\n x ', end='   ')
for k in range(1, m+1):
    print(Fore.YELLOW + str(k).zfill(2), end='    ')
print('\n')
print(Style.RESET_ALL, end='')
for i in range(1, n+1):
    print(Fore.YELLOW + str(i).zfill(2), end='    ')
    print(Style.RESET_ALL, end='')
    for j in range(1, m+1):
        if i==j:
            print(Fore.YELLOW + str(i*j).zfill(2), end='    ')
            print(Style.RESET_ALL, end='')
        else:
            print(str(i*j).zfill(2), end='    ')
    print('\n')
