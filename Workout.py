import random 
import time 
import sys 
import json 
import os 

# MINE
from common import * 
# =======================================


class Workout:
    """
    Docstring

    """
    
    def __init__(self):
        # private attributes - use double underscore
        
        # loading json
        with open("workout_exercises.json") as f:
            self.data = json.load(f)

        # text file
        # with open("info.txt", "r") as f:
        #     print(f.read())
        
   
    def __str__(self) -> str:
        s = ""
        return s 
    
    # ------------------------

    # 1) GENERATE WORKOUT
    def select_workout_type(self) -> str:
        workout_types = [
            "calisthenics", 
            "weights", 
            "mixed"
        ]

        for t in workout_types:
            print(workout_types.index(t) + 1, end=") ")
            print(t.capitalize())

        # user input
        print("\nSelect your workout type")
        valid_input = False 
        while not valid_input:
            option = input("\n> ")
            if option not in ["1", "2", "3", "4", "5"]:
                print("*Invalid input*")
        
            else:
                valid_input = True
                return workout_types[int(option)-1]
    # =============================================

    # creating the workout
    def workout_gen(self):
        # loading json 
        # with open("workout_exercises.json") as f:
        #     data = json.load(f)

        # getting user input (string)
        a = self.select_workout_type()

        # display workout
        os.system("cls")
        time.sleep(2)
        display_heading_v1(a)

        # sets. reps, time
        # user_sets = [1, 2, 3]
        user_time = [20, 30, 60]
        user_reps = [5, 10, 20, 30]

        # cali and weights
        if a != "mixed":
            dict_cali = self.data[a]
            
            for a in dict_cali:
                if a == "abs_static" or a == "static":
                    # print(f"{Back.WHITE}{a}{Back.RESET}")
                    print(f"{a}")
                    print(f"- exercise: \t\t{random.choice(dict_cali[a])}")
                    print(f"- minumum time: \t{random.choice(user_time)} seconds")

                else: 
                    # print(f"{Back.WHITE}{a}{Back.RESET}")
                    print(f"{a}")
                    print(f"- exercise: \t\t{random.choice(dict_cali[a])}")
                    print(f"- minumum reps: \t{random.choice(user_reps)} reps")
                print("\n")

        # mixed
        else:
            mix = []
            for m in self.data["mixed"]:

                # randomly select one exercise per list
                for d in (self.data[m]):
                    # print(d)
                    mix.append(random.choice(self.data[m][d]))

            # mixing the order of the exercises
            random.shuffle(mix)

            # display workout
            print("\nExercises: ", len(mix))
            for exercise in mix: 
                # time 
                if exercise in "holding":
                    print(exercise)
                    print(f"- minumum time: \t{random.choice(user_time)} seconds")

                # reps
                else: 
                    print(exercise)
                    print(f"- minumum reps: \t{random.choice(user_reps)} reps")
                print("\n")
    # ===================================
    

    # 2) DISPLAY EXERCISES
    # calisthenics
    def display_cali(self):
        for a in self.data["calisthenics"]:
            print(a.capitalize())

            for b in self.data["calisthenics"][a]:
                print("- ", b)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    # ==============================================
    # display_cali()

    def display_exercises(self):
        display_heading("VIEW EXERCISES")

        for a in self.data:
            print(a.capitalize())

            if a == "calisthenics":
                self.display_cali()

            else: 
                for b in self.data[a]:
                    print(f"- {b}")
                print("-------------------------\n")
    # ==============================================
    # display_exercises()


    # 3) HEALTH INFO
    def show_health_info(self):
        print("HEALTH ADVICE")
        print("==============\n")
            
        with open("info.txt", "r") as f:
            print(f.read())
    # =================================


    # 4) and 6) SAVED WORKOUTS
    # def display_workout_records(self, dir_name="workout-records-saved"):
    def display_workout_records(self, dir_name="workout-records-all"):
        display_heading("VIEW SAVED WORKOUTS")

        # chaninging dir
        os.chdir(dir_name)

        # display files in a dir
        print("files in: ")
        print(os.getcwd())

        folder = os.listdir()
        print("Enter the corresponding number to view the file")
        for file in os.listdir():
            print(f"{(os.listdir()).index(file) + 1}) {file}")
        print()

        # loop
        correct_input = False 
        while not correct_input:
            # user input
            option = input("> ")
            try:
                file = os.listdir()[int(option)-1]
                print(file)
                f = open(file, "r")
                print(f.read())
                correct_input = True 

            except KeyboardInterrupt:
                print("---user quit---")

            except:
                print("*error*")
    # ==============================
    # display_saved_workouts()


    # 5) BMI
    def bmi(self):
        display_heading("BMI calculator")

        mass = input("Enter your mass (kg): ")
        height = input("Enter your height (m): ")
        try:
            mass, height = float(mass), float(height)
            bmi = mass / (height ** 2)

        except:
            print("*value error*")

        # mass = float(mass)
        # height = float(height)

        # print(type(mass))
        # print(type(height))


        # display result
        print("\nYour Body Mass Index is:", bmi)

        if bmi < 18.5:
            print("You are underweight")
        elif 18.5 < bmi < 24.9:
            print("You are in a healthy weight range")
        elif 25 < bmi < 29.9:
            print("You are overweight")
        elif 30 < bmi < 35:
            print("You may suffer from obesity")
        elif 35 < bmi:
            print("You should consider bariatric surgery")
    # ===========================================
    # bmi()


    def non_bmi(self):
        r = """
        A new study found that your waist-to-hip 
        ratio might be a more accurate measure of what’s a 
        healthy weight for you than your BMI
        """

        c = """
        How to Calculate Your Waist-to-Hip Ratio
        To get your waist-to-hip ratio, divide the measurement around your waist 
        by the measurement around your hips.

        For example, if your waist has a 30-inch circumference and your 
        hips have a 35-inch circumference, you would divide 30 by 35. 
        Your waist-to-hip ratio would be 0.86.

        According to the World Health Organization (WHO), 
        a waist-to-hip ratio above 0.85 is “high risk” 
        for women, and a waist-to-hip ratio above 0.9 is high risk for men.
        """

        i = """
        Stanford said that a person’s waist-to-hip ratio 
        is by far a better tool to use than BMI as it considers 
        the area where fat is most likely to be problematic—the waist.

        BMI can’t differentiate fat mass from lean mass, or subcutaneous 
        (good fat) from visceral fat (bad fat).
        — IRFAN KHAN

        """

        d = """
            A hip measurement describes the circumference around the widest point of the 
            pelvic, or hip, bones. A waist measurement measures 
            the circumference of the waistline or the narrowest point 
            between the ribs and the hips.
        """


        print(r)

        print(c)

        # links
        print("link1")
        print("https://www.verywellhealth.com/waist-circumference-and-diabetes-1087703")

        print("link2")
        print("https://www.usatoday.com/story/college/2014/07/21/better-than-bmi-4-ways-to-track-your-health-besides-the-scale/37393045/")

    # ===========================================
    # non_bmi()


    # 7) SOURCE CODE
    def show_code(self): 
        display_heading("SOURCE CODE")
        writer1("https://github.com/trpl-A")
    # ===================================

# _____________________________
# testing class
# workout1 = Workout()

# 1
# workout1.workout_gen()

# 2
# workout1.display_exercises()

# 3
# workout1.show_health_info()

# 4 and 6
# folder = "workout-records-saved"
# workout1.display_workout_records()

# 5
# workout1.bmi() workout1.non_bmi()

# 7
# workout1.show_code()
# _____________________________

# <END>