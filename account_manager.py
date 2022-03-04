acc = {}

with open('accounts.txt', 'r') as f:
    for line in f:
        details = line.split('\n')
        details = details[:len(details)-1][0].split('|')
        # print(details)
        acc[details[0]] = details[1:]

# print(acc)

def calculate_monthly_interest(account_number):
    account_balance = acc[account_number][0]
    annual_rate = acc[account_number][1]

    return annual_rate / 12 * account_balance

