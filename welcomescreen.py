import tkinter as tk
from tkinter import *
import enigma
import rotor

my_machine = enigma.EnigmaMachine(rotor.RotorI(), rotor.RotorII(), rotor.RotorIII(), rotor.ReflectorB())


def rotor_selection():
    """Allows for the rotor to be selected within the tkinter interface"""
    rotor_num1 = slow_rotor.get()
    if rotor_num1 == 1:
        my_machine.slow_rotor = rotor.RotorI()
    elif rotor_num1 == 2:
        my_machine.slow_rotor = rotor.RotorII()
    elif rotor_num1 == 3:
        my_machine.slow_rotor = rotor.RotorIII()

    rotor_num2 = medium_rotor.get()
    if rotor_num2 == 1:
        my_machine.medium_rotor = rotor.RotorI()
    elif rotor_num2 == 2:
        my_machine.medium_rotor = rotor.RotorII()
    elif rotor_num2 == 3:
        my_machine.medium_rotor = rotor.RotorIII()

    rotor_num3 = fast_rotor.get()
    if rotor_num3 == 1:
        my_machine.fast_rotor = rotor.RotorI()
    elif rotor_num3 == 2:
        my_machine.fast_rotor = rotor.RotorII()
    elif rotor_num3 == 3:
        my_machine.fast_rotor = rotor.RotorIII()


def run():
    """Runs Enigma Machine and Updates Rotor Position on screen"""
    my_machine.run_machine()
    my_machine.int_to_output()
    my_result.set(my_machine.output)

    fast_rotor_position.config(text=my_machine.fast_rotor.show_position())
    medium_rotor_position.config(text=my_machine.medium_rotor.show_position())
    slow_rotor_position.config(text=my_machine.slow_rotor.show_position())


def add_message():
    """Attempts to add entered message to the machine
    Will raise pop up error message if invalid char is entered"""
    message = encode.get()
    for letter in message:
        if letter.upper() not in my_machine.alphabet:
            error_message = tk.Toplevel()
            error_message.title('Error Invalid Character')
            error_char = tk.Label(master=error_message, text=letter, fg='red')
            error_label = tk.Label(master=error_message, text=' is an invalid Character')
            error_button = tk.Button(master=error_message, text='Return', fg="red", command=error_message.destroy)
            error_char.grid(row=0, column=0)
            error_label.grid(row=0, column=1)
            error_button.grid(row=1, column=1)
            return
        my_machine.message_to_list(message)


"""The collection of menu functions"""


def about():
    with open('InfoScreen.txt') as file_object:
        popup_text = file_object.read()

    about_popup = tk.Toplevel()
    about_popup.title('About')
    about_text = tk.Label(master=about_popup, text=popup_text, bd=10)
    about_exit = tk.Button(master=about_popup, text='Return', fg="red", command=about_popup.destroy)
    about_text.grid(row=0, column=0)
    about_exit.grid(row=1, column=0)


# Create the window
window = tk.Tk()
window.title('Enigma Machine')
window.geometry("800x400")
window.option_add('*tearOff', False)

my_result = tk.StringVar()
my_result.set('Result will be displayed here')

# Create entry area
label = tk.Label(text='Enter Message to be encoded', width=30).grid(row=0, column=0)
encode = tk.Entry(master=window, width=20)
encode.grid(row=1, column=0)
result = tk.Label(master=window, textvariable=my_result, font=("helvetica",10)).grid(row=8, column=0, pady=5)

# Add buttons
Add_Message = tk.Button(master=window, text='Add message', command=add_message).grid(row=2, column=0, pady=5)
Run_machine = tk.Button(master=window, text='Run Machine', command=run).grid(row=4, column=0, pady=5)

# Reset = tk.Button(master=window, text='Reset Machine', command= reset_machine)

"""Rotor Selection"""
slow_rotor = IntVar()
slow_rotor.set(1)
tk.Radiobutton(text='Rotor I', variable=slow_rotor, value=1).grid(row=11, column=0)
tk.Radiobutton(text='Rotor II', variable=slow_rotor, value=2).grid(row=12, column=0)
tk.Radiobutton(text='Rotor III', variable=slow_rotor, value=3).grid(row=13, column=0)
tk.Label(text='Choose a slow rotor').grid(row=10, column=0)

medium_rotor = IntVar()
medium_rotor.set(2)
tk.Radiobutton(text='Rotor I', variable=medium_rotor, value=1).grid(row=11, column=1)
tk.Radiobutton(text='Rotor II', variable=medium_rotor, value=2).grid(row=12, column=1)
tk.Radiobutton(text='Rotor III', variable=medium_rotor, value=3).grid(row=13, column=1)
tk.Label(text='Choose a medium rotor').grid(row=10, column=1)

fast_rotor = IntVar()
fast_rotor.set(3)
tk.Radiobutton(text='Rotor I', variable=fast_rotor, value=1).grid(row=11, column=3)
tk.Radiobutton(text='Rotor II', variable=fast_rotor, value=2).grid(row=12, column=3)
tk.Radiobutton(text='Rotor III', variable=fast_rotor, value=3).grid(row=13, column=3)
tk.Label(text='Choose a fast rotor').grid(row=10, column=3)

tk.Button(master=window, text='Configure Rotors', command=rotor_selection).grid(row=3,
                                                                          column=0, pady=5)

"""Display Rotor Positions"""
rotor_positions = tk.StringVar()
rotor_positions.set('A,A,A')
global fast_rotor_position
tk.Label(text='Current Rotor Positions').grid(row=0, column=1)
fast_rotor_position = tk.Label(text=my_machine.fast_rotor.show_position())
fast_rotor_position.grid(row=1, column=1)
medium_rotor_position = tk.Label(text=my_machine.medium_rotor.show_position())
medium_rotor_position.grid(row=2, column=1)
slow_rotor_position = tk.Label(text=my_machine.slow_rotor.show_position())
slow_rotor_position.grid(row=3, column=1)

"""Creates the menu"""
menu = Menu(window)

menu_welcome = Menu(menu)
menu.add_cascade(menu=menu_welcome, label="Welcome")

menu_about = Menu(menu)
menu.add_cascade(menu=menu_about, label='About')
menu_about.add_command(label="About", command=about)

menu_exit = Menu(menu)
menu.add_cascade(menu=menu_exit, label="Quit")
menu_exit.add_command(label="Exit", command=window.destroy)

window['menu'] = menu

window.mainloop()
