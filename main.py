import sys
import tkinter.messagebox as msg
import turtle,pandas
screen = turtle.Screen()
screen.setup(460,307)
screen.bgpic("animals.gif")
animals=pandas.read_csv("coo_animals.csv")
animals_list=animals.animal.tolist()
animals_guessed=[]
def restarting():
    global animals_list,animals
    msg.showinfo("restarting", "Let's restart the game")
    animals_guessed.clear()
    screen.clear()
    screen.bgpic("animals.gif")
    animals_list = animals.animal.tolist()



def navigator(x_cor,y_cor):
    new_pointer=turtle.Turtle()
    new_pointer.hideturtle()
    new_pointer.penup()
    new_pointer.color("red")
    new_pointer.goto(x_cor,y_cor)
    new_pointer.showturtle()

while len(animals_guessed) < 11 :

    user_input = screen.textinput\
        (f"You Guessed {len(animals_guessed)} of 11 ", "Select an animal!")\
        .title()

    if user_input in animals_list and user_input not in animals_guessed:
        animals_guessed.append(user_input)
        animals_list.remove(user_input)
        navigator(animals[animals["animal"]==user_input].x.iloc[0],
                  animals[animals["animal"]==user_input].y.iloc[0])

    elif user_input in animals_list and user_input in animals_guessed:
        msg.showinfo("Warning","This Animal is repeated !!")

    elif user_input.lower() == "exit":
        msg.showinfo("Endgame",f"Thank You !! Your score is {len(animals_guessed)}")
        with open("unguessed.csv","w")as file:
            for animal in animals_list:
                file.write(animal+",")
        sys.exit(0)


    elif user_input.lower() == "restart":
       restarting()

    else:
        msg.showinfo("Invalid choice","please enter a valid choice !")

else:
    msg.showinfo("Congrats message","Congratulations!!! You Won")


screen.mainloop()