# MY FUNCTIONS
# ============
import time 
import os 
import sys 


# version1
def display_heading(title="Quick Daily Workout (^_^)"):
    print()
    print(title)
    print(len(title) * "=")
    print()
# ==============================

# version2
def display_heading_v1(title="Quick Daily Workout (^_^)", pause=0.1):
    print()
    print(title)
    time.sleep(pause)
    print(len(title) * "=")
    time.sleep(pause)
    print()
# ==============================

def writer1(text="testing", pause=0.1) -> None:
        for letter in text:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(pause)
        print()
        time.sleep(pause * 5)
# ==============================
# writer1()

def hide(): 
    print(os.getcwd())
    
    # stuff to hide
    counter = 0
    all_items = os.listdir()
    stay_hidden = [
        # folders
        "workout-records-all",
        "workout-records-saved", 
        "__pycache__", 

        # files
        "info.txt",
        "workout_exercises.json",
    ]

    for item in all_items:
        counter += 1
        if ".py" in item and item != "main.py":
            print(item)
            os.system(f"attrib +h {item}")
            print("*item hidden*\n")

    for item in stay_hidden:
        counter += 1
        print(item)
        os.system(f"attrib +h {item}")
        print("*item hidden*\n")

    # os.chdir("")
    # os.system("attrib -h lock.py")
    print(f"{counter} items hidden")
    print("**Process complete**")
# ==============================
# hide()


def source_code():
    # print("waiting...")
    everything = ""