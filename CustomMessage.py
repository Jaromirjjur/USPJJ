import tkinter

def ask_user_choice(message, button1text, button2text):

    choice = {'value': 1}

    def choose_true():
        choice['value'] = 1
        root.destroy()

    def choose_false():
        choice['value'] = 0
        root.destroy()

    root = tkinter.Tk()
    root.title("Select Value Criteria")

    root.attributes('-topmost', True)
    root.focus_force()

    label = tkinter.Label(root, text=message)
    label.pack(padx=20, pady=10)

    button_frame = tkinter.Frame(root)
    button_frame.pack(pady=10)

    btn_1 = tkinter.Button(button_frame, text=button1text, command=choose_true)
    btn_1.pack(side="left", padx=10)

    btn_0 = tkinter.Button(button_frame, text=button2text, command=choose_false)
    btn_0.pack(side="left", padx=10)

    root.mainloop()
    return choice['value']
