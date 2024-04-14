import re


def ask_and_check_card_for_invalid_entry():
    while True:
        credit_card = input("Enter your credit card numbers: ")
        contains_letters = re.search("[a-zA-Z]", credit_card)
        if contains_letters or len(credit_card) < 13:
            print("Please enter a value without letters. You can't enter an empty value. ")
        else:
            print()
            print("Checking credit card details...")
            print("Please wait..")
            # Return the digits-only version of the credit card
            return re.sub(r'\D', '', credit_card)


def check_if_card_valid(card_digits_only):
    sum_odd_digits = 0
    sum_even_digits = 0
    total = 0

    # Reverse the card number for easier iteration
    reversed_card_digits = card_digits_only[::-1]

    # Sum all the odd digits
    for i in reversed_card_digits[::2]:
        sum_odd_digits += int(i)

    # Double and sum all the even digits
    for i in reversed_card_digits[1::2]:
        i = int(i) * 2
        if i >= 10:
            sum_even_digits += i // 10 + i % 10
        else:
            sum_even_digits += i

    # Add sum of odd and even digits
    total += (sum_even_digits + sum_odd_digits)

    if total % 10 == 0:
        return True, card_digits_only
    else:
        return False, card_digits_only


def check_card_issuer(valid, card_number):
    if valid:
        if card_number.startswith('34') and len(card_number) == 15 \
                or card_number.startswith('37') and len(card_number) == 15:
            print(f"Card Issuer: American Express\n"
                  f"Card No: {card_number}\n"
                  f"Status: Valid")
        elif card_number.startswith('4') and len(card_number) == 16:
            print(f"Card Issuer: Visa\n"
                  f"Card No: {card_number}\n"
                  f"Status: Valid")
        elif card_number.startswith('5610') and len(card_number) == 16:
            print(f"Card Issuer: Australian Bankcard\n"
                  f"Card No: {card_number}\n"
                  f"Status: Valid")
        elif card_number.startswith('5') and len(card_number) == 16 \
                or card_number.startswith('2') and len(card_number) in [13, 16]:
            print(f"Card Issuer: Mastercard\n"
                  f"Card No: {card_number}\n"
                  f"Status: Valid")
        elif card_number.startswith('6') and len(card_number) == 16:
            print(f"Card Issuer: Discover\n"
                  f"Card No: {card_number}\n"
                  f"Status: Valid")
        elif card_number.startswith('3') and len(card_number) == 14:
            print(f"Card Issuer: Diners Club\n"
                  f"Card No: {card_number}\n"
                  f"Status: Valid")
        elif card_number.startswith('35') and len(card_number) == 16 \
                or card_number.startswith('3') and len(card_number) in [15, 16]:
            print(f"Card Issuer: JCB (Japan Credit Bureau)\n"
                  f"Card No: {card_number}\n"
                  f"Status: Valid")
    else:
        print(f"Card Issuer: Unknown\n"
              f"Card No: {card_number}\n"
              f"Status: Invalid")


while True:
    card_number = ask_and_check_card_for_invalid_entry()
    valid, card_digits_only = check_if_card_valid(card_number)
    check_card_issuer(valid, card_digits_only)
    print()
    if input("Would you like to check another credit card? Y/N: ").lower() != 'y':
        print("Thank you for using this service!")
        break
