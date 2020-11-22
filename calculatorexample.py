'''
Updating a label’s text is a little convoluted – we can’t simply update the text using a normal Python string. Instead, we have to provide the label with a special tkinter string variable object, and set a new value on the object whenever we want the text in the label to change.

We have defined a handler which cycles to the next text string in the sequence, and used the bind method of the label to bind our new handler to left clicks on the label. It is important to note that this handler takes an additional parameter – an event object, which contains some information about the event. We could use the same handler for many different events (for example, a few similar events which happen on different widgets), and use this parameter to distinguish between them. Since in this case we are only using our handler for one kind of event, we will simply ignore the event parameter.

Putting it all together
Now we can use all this information to create a simple calculator. We will allow the user to enter a number in a text field, and either add it to or subtract it from a running total, which we will display. We will also allow the user to reset the total:
'''

from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
my_gui = Calculator(root)
root.mainloop()