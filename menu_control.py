import time 
from colorama import Fore, Back 

# MINE
from Workout import Workout
from common_lock import lock_master 
# ==============================

w1 = Workout()

# main menu
def display_main_menu(pause=0.1):
    main_menu_sections = [
        "1. WORKOUT!", 
        "2. View exercises", 
        "3. View health information", 
        "4. View saved workouts", 
        "5. Calcualte BMI", 
        "6. View all workout records", 
        "^_^ View source code", 
        "\n",
        "quit | exit | esc"
    ]

    # heading
    title = "Quick Daily Workout (^_^)"

    # display
    print()
    print("=" * 25)
    print()
    print(title)
    time.sleep(pause)
    print(len(title) * "-")
    time.sleep(pause)
    print("Minimum number of sets: 1\n")
    time.sleep(pause)

    # displaying options
    for a in main_menu_sections:
        print(a)
        time.sleep(pause)
    print()
    print("=" * 25)
# ==================================================
# display_main_menu()


sections = {
    "1": w1.workout_gen,
    "2": w1.display_exercises,
    "3": w1.show_health_info, 
    "4": w1.display_workout_records, 
    "5": w1.bmi, 
    "6": w1.display_workout_records, 
}

def main_menu_control():
    display_main_menu()

    correct_input = False 
    while not correct_input: 
        option = input("\n> ")
        try: 
            if option == "6": 
                folder = "workout-records-saved"
                w1.display_workout_records(folder)

            if option == "^_^":
                lock_master(w1.show_code)

            if option in ["esc", "exit", "quit"]:
                break

            else: 
                sections[option]()
            correct_input = True 

        except:
            print("*an error has occurred*")

# =============================
# main_menu_control1()