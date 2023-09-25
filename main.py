import locale

# Setting locale to system default
locale.setlocale(locale.LC_ALL, '')

# Request user input valid initial investment and rate
while True:
    try:
        principal = float(input('Please enter initial investment as a whole number. If initial investment is $1,000 please enter 1000: '))
        if principal <= 0:
            print("Please enter a number greater than zero.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")
while True:
    try:
        rate = float(input('Please enter rate as a whole number. If the rate is 5% please enter 5: '))
        if rate <= 0:
            print("Please enter a number greater than zero.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")
print()

# Calculates total interest and year 1 total
total_interest = principal * rate / 100
total = total_interest + principal

# Calculates the loop threshold which is 2 times the initial investment
threshold = 2 * principal

# Initialize year counter to 1
year = 1

# Formats total to local currency and displays year 1 total investment
dollar_value = locale.currency(total, grouping=True)
print('For year: {1} your total investment is: {0}'.format(dollar_value, year))

# Displays consecutive years and total investment till threshold met
while total < threshold:
    total_interest = total * rate / 100
    total += total_interest
    dollar_value = locale.currency(total, grouping=True)
    year += 1
    print('For year: {1} your total investment is: {0}'.format(dollar_value, year))