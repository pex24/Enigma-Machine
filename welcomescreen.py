import tkinter as tk
import enigma
import rotor

my_machine2 = enigma.EnigmaMachine(rotor.RotorI(), rotor.RotorII(), rotor.RotorIII(), rotor.ReflectorB())




def run():
    my_machine2.run_machine()
    my_machine2.int_to_output()


def add_message():
    my_message = encode.get()
    my_machine2.message_to_list(my_message)

# Create the window
window = tk.Tk()
window.title('Enigma Machine')

# Create entry area
label = tk.Label(text='Welcome to the Enigma Machine', font=20)
encode = tk.Entry(master=window, width=30)
result = tk.Label(master=window)

# Add buttons
Run = tk.Button(master=window, text='Run Machine', command=run)
Quit = tk.Button(master=window, text="QUIT", fg="red", command=window.destroy)
Message = tk.Button(master=window, text='Add message', command=add_message)

# Organize Screen
label.grid(row=0, column=0)
encode.grid(row=1, column=0)
result.grid(row=4, column=0, pady=2)
Run.grid(row=4, column=0, pady=5)
Message.grid(row=2, column=0, pady=10)
Quit.grid(row=5, column=0, pady=10)

window.mainloop()
