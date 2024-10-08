import tkinter
import customtkinter

# def startSolve():
#     try:
#         const1 = const1.get()


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Recursive Relation Solver")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert Constants: ")
title.pack(padx=10,pady=10)

# Link input
constant_var = tkinter.IntVar()
const1 = customtkinter.CTkEntry(app, width=350, height=40, textvariable=constant_var)
const1.pack(padx=10,pady=0)

#Solve
#solve = customtkinter.CTkButton(app, text="Solve", command=startSolve)

# Run App
app.mainloop()