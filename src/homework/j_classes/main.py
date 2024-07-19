from class_a import die


def main():
    d = die()
    while True:
        d.roll()
        print(d)
        continue_rolling = input("Do you want to roll again? (yes/no): ").strip().lower()
        if continue_rolling != 'yes':
            break


if __name__ == '__main__':
    main()