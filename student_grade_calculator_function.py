def grade_student(score):
    """Function to calculate student grade"""
    if score > 100:
        print("Score can't be greater than 100.")
        return
    elif 90 <= score < 101:
        print("You scored an A.")
    elif 80 <= score < 90:
        print("You scored a B.")
    elif 70 <= score < 80:
        print("You scored a C.")
    elif 60 <= score < 70:
        print("You scored a D.")
    elif 50 <= score < 60:
        print("You scored an E.")
    else:
        print("You scored an F.")
    return score


while True:
    prompt = input("What is your score or enter 'q' to exit.\n: ")
    if prompt.lower() == 'q':
        print("Ending program")
        break
    else:
        try:
            prompt = int(prompt)
        except ValueError:
            print("Invalid entry, please type a number(0-100) or 'q' to exit.")
            continue  # Skip to the next iteration of the loop

    graded = grade_student(prompt)
