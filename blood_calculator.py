def interface():
    print("Blood calculator")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1 - HDL")
        print("2 - LDL")
        print("3 - Total Cholestrol")
        print("9 - Quit")
        choice = input("Select an option: ")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            TotalChol_driver()
    print("Program ending")


def HDL_driver():
    HDL_in = HDL_input()
    HDL_analy = HDL_analysis(HDL_in)
    HDL_output(HDL_in, HDL_analy)


def LDL_driver():
    LDL_in = LDL_input()
    LDL_analy = LDL_analysis(LDL_in)
    LDL_output(LDL_in, LDL_analy)


def TotalChol_driver():
    TotalChol_in = TotalChol_input()
    TotalChol_analy = TotalChol_analysis(TotalChol_in)
    TotalChol_output(TotalChol_in, TotalChol_analy)


def HDL_input():
    HDL_value = input("Enter the HDL result: ")
    HDL_value = int(HDL_value)
    return HDL_value


def LDL_input():
    LDL_value = input("Enter the LDL result: ")
    LDL_value = int(LDL_value)
    return LDL_value


def TotalChol_input():
    TotalChol_value = input("Enter the Total Cholestrol result: ")
    TotalChol_value = int(TotalChol_value)
    return TotalChol_value


def HDL_analysis(HDL_int):
    if HDL_int >= 60:
        answer = "Normal"
    elif 40 <= HDL_int < 60:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer


def LDL_analysis(LDL_int):
    if LDL_int >= 190:
        answer = "Very High"
    elif 160 <= LDL_int < 190:
        answer = "High"
    elif 130 <= LDL_int < 160:
        answer = "Borderline High"
    else:
        answer = "Normal"
    return answer


def TotalChol_analysis(TotalChol_int):
    if TotalChol_int < 200:
        answer = "Normal"
    elif 200 <= TotalChol_int < 239:
        answer = "Borderline High"
    else:
        answer = "High"
    return answer


def HDL_output(HDL_value, HDL_analy):
    print("The HDL result of {} is considered {}".format(HDL_value, HDL_analy))
    return


def LDL_output(LDL_value, LDL_analy):
    print("The LDL result of {} is considered {}".format(LDL_value, LDL_analy))
    return


def TotalChol_output(TotalChol_value, TotalChol_analy):
    print("The LDL result of {} is considered {}".format(
        TotalChol_value, TotalChol_analy))
    return


if __name__ == "__main__":
    interface()
