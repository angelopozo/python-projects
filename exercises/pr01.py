def askNumber(mensaje, minimum=None, maximum=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimum is not None and valor < minimum:
                print(f"The value must be at least: {minimum}.")
                continue
            if maximum is not None and valor > maximum:
                print(f"The value must be at most: {maximum}.")
                continue
            return valor
        except:
            print("Please, enter a valid number.")

def main():
    print("================================================")
    print("Employee registration and schedules - Program 01")
    print("================================================\n")

    num_emp = askNumber("How many employees will you enter? ", minimum=1)
    ref_hour = askNumber("Enter the reference hour (0-23): ", minimum=0, maximum=23)

    early_count = 0
    earliest_out = 24
    earliest_name = None

    i = 0
    while i < num_emp:
        name = input(f"Name of employee #{i+1}: ").strip()
        in_hour = askNumber(f"Entry hour for {name} (0-22): ", minimum=0, maximum=22)
        out_hour = askNumber(f"Exit hour for {name} (0-23): ", minimum=0, maximum=23)

        if out_hour <= in_hour:
            print("Exit hour must be greater than entry hour. Try again.")
            continue

        if in_hour <= ref_hour:
            early_count += 1

        if out_hour < earliest_out:
            earliest_out = out_hour
            earliest_name = name

        i += 1

    print(f"\nEmployees who entered at or before the reference hour: {early_count}")
    if earliest_name is not None:
        print(f"The employee who left earliest was {earliest_name} at {earliest_out}:00.")

if __name__ == "__main__":
    main()