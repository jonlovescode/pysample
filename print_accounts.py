# from account_manager import calculate_monthly_interest

def print_accounts(txt):
    with open(txt, 'r') as f:
        for line in f:
            print(line)

if __name__ == '__main__':
    print_accounts('accounts.txt')

