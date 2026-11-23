def get_valid_number(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n < 0:
                print("Value cannot be negative")
            else:
                return n
        except ValueError:
            print("Invalid input (must be an integer)")


def subject_score(subject_name):
    score = get_valid_number(f"What is your score in {subject_name}: ")
    coef = get_valid_number(f"What is the coefficient of {subject_name}: ")

    total = score * coef
    print(f"Your {subject_name} score x Coef:", total)

    return total, coef


def main():
    print("This software calculates your average for a sequence")

    
    math_score, math_coef = subject_score("Mathematics")
    f_math_score, f_math_coef = subject_score("Further Mathematics")
    chem_score, chem_coef = subject_score("Chemistry")
    ict_score, ict_coef = subject_score("ICT")
    phy_score, phy_coef = subject_score("Physics")

    # Totals
    T_score = math_score + f_math_score + chem_score + ict_score + phy_score
    T_coef = math_coef + f_math_coef + chem_coef + ict_coef + phy_coef

    print("Your total score is:", T_score)
    print("Your total coefficient is:", T_coef)

    average = T_score / T_coef
    print(f"Your average is: {average:.2f}")

    # Grade
    if average > 16:
        print("Excellent")
    elif average > 14:
        print("Very Good")
    elif average > 9:
        print("Good")
    else:
        print("Poor")


main()
input("Press enter to exit...")