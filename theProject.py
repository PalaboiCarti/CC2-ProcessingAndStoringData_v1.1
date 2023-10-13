import math
import pandas as pd
#user profile

def user_profile():
    def get_name():
        while True:
            name = input("Enter name: ")
            if any(char.isalpha() or char.isspace() or not char.isprintable() for char in name):
                return name
            else:
                print("Error: Your name should contain letters, spaces, or special characters. Try again.")

    def get_age():
        while True:
            age_str = input("Enter age: ")
            if age_str.isdigit():
                age = int(age_str)
                if age > 0:
                    return age
                else:
                    print("Error: Your age can't be negative. Try again.")
            else:
                print("Error: Your age should be a whole number. Please try again.")
    
    def get_degree():
        while True:
            degree = input("Enter degree: ")
            if degree.isprintable():
                return degree
            else:
                print("Error: Your degree should be printable characters. Try again.")

    
    def get_email():
        while True:
            email = input("Enter email: ")
            if isinstance(email, str) and "@" in email:
                return email
            else:
                print("Error: Your email should be a valid email address with '@'. Please try again.")
    
    def get_hobbies():
        user_hobbies = []
        for i in range(3):
            new_hobby = input(f"Enter hobby {i+1}: ")
            user_hobbies.append(new_hobby)
        return user_hobbies
    
    def get_skills():
        user_skills = []
        for i in range(3):
            new_skill = input(f"Enter skill {i+1}: ")
            user_skills.append(new_skill)
        return user_skills
    
    def display_profile():
        name = get_name()
        age = get_age()
        degree = get_degree()
        email = get_email()
        user_hobbies = get_hobbies()
        user_skills = get_skills()
    
        print("~~~~~~~~~~~~~~~~~")
        print("Ｐｒｏｆｉｌｅ")
        print("~~~~~~~~~~~~~~~~~")
        print(f"( ๑‾̀◡‾́)σ Hello! My name is {name}!")
        print(f"==> I am {age} years old.")
        print(f"==> My degree is {degree}.")
        print(f"==> My email is {email}.")
        print(f"==> My hobbies are: {', '.join(user_hobbies)}.")
        print(f"==> My skills are: {', '.join(user_skills)}.")
    display_profile()


def item_list():   
    def initial_list(chores):
        df = pd.DataFrame({'House Chores': chores})
        print("Initial List:")
        print(df)
    
    def add_to_list(chores):
        new_chores = []
        for i in range(5):
            new_chore = input(f"Enter item {i + 1}: ")
            new_chores.append(new_chore)
        chores.extend(new_chores)
        df = pd.DataFrame({'Updated House Chores': chores})
        print("~~~~~~~~~~~~~~~~~")
        print(df)
    
    def main():
        print("~~~~~~~~~~~~~~~~~")
        print("Ｙｏｕｒ Ｌｉｓｔ")
        print("~~~~~~~~~~~~~~~~~")
        # Items list
        chores = ['wash dishes', 'buy dish soap', 'think about life', 'wash a random thing', 'tell your mom you love her']
    
        initial_list(chores)
        add_to_list(chores)
    
    if __name__ == "__main__":
        main()


#set a

    def set_A():
        def square():
            while True:
                try:
                    sideLength = float(input("Enter a value for a side length: "))
                    area = sideLength ** 2
                    print(f"The area of the square is: {area:.2f}")
                    return
                except ValueError:
                    print("Error: Please enter a valid numeric value for the side length.")
        
        def triangle():
            while True: 
                try:
                    width = float(input("Enter a value for width: "))
                    height = float(input("Enter a value for height: "))
                    area = 0.5 * width * height
                    print(f"The area of the triangle is: {area:.2f}")
                    return
                except ValueError:
                    print("Error: Please enter valid numeric values for the width and height.")
        
        def circle():
            while True:
                try:
                    radius = float(input("Enter a value for radius: "))
                    area = math.pi * (radius ** 2)
                    print(f"The area of the circle is: {area:.2f}")
                    return
                except ValueError:
                    print("Error: Please enter a valid numeric value for the radius.")
        
        def rectangle():
            while True:
                try:
                    width = float(input("Enter a value for width: "))
                    height = float(input("Enter a value for height: "))
                    area = width * height
                    print(f"The area of the rectangle is: {area:.2f}")
                    return
                except ValueError:
                    print("Error: Please enter valid numeric values for width and height.")
        
        def trapezoid():
            while True:
                try:
                    base1 = float(input("Enter a value for the first base: "))
                    base2 = float(input("Enter a value for the second base: "))
                    height = float(input("Enter a value for height: "))
                    area = 0.5 * (base1 + base2) * height
                    print(f"The area of the trapezoid is: {area:.2f}")
                    return
                except ValueError:
                    print("Error: Please enter valid numeric values for the bases and height.")
        
        def retry():
            select = input("Would you like to make another conversion? (y/n): ").strip().lower()
            if select == "y":
                return True
            elif select == "n":
                print("Alright. See you again.")
                return False
            else:
                print("Error: Invalid input. Please enter 'y' or 'n'.")
                return retry()
        
        def shapeSelect():
            while True:
                try:
                    select = int(input("""Select your shape
    1. Square
    2. Triangle
    3. Circle
    4. Rectangle
    5. Trapezoid
    """))
                    if select in [1, 2, 3, 4, 5]:
                        if select == 1:
                            square()
                        elif select == 2:
                            triangle()
                        elif select == 3:
                            circle()
                        elif select == 4:
                            rectangle()
                        elif select == 5:
                            trapezoid()
                        if not retry():
                            break
                    else:
                        print("Error: Invalid input. Please enter a number between 1 and 5.")
                except ValueError:
                    print("Error: Invalid input. Please enter a valid number between 1 and 5.")
        
        def main():
            shapeSelect()
        
        main()
    
    if __name__ == "__main__":
        setA()
        
def main():
    user_profile()
    print("~~~~~~~~~~~~~~~")
    item_list()
    set_A()

main()
