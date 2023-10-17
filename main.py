from menu_control import main_menu_control
import os 

def main():
    rerun = True 

    while rerun: 
        os.system("cls")
        main_menu_control()
        confirm_rerun = input("\nRerun? (y/n) \n> ")
        if confirm_rerun == "n":
            rerun = False 

# ==============================
if __name__ == "__main__":
    main()
    print("\n<END OF PROGRAM>")
# ==============================