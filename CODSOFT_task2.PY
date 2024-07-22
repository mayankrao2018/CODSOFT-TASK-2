import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")
        return

    operation = operation_var.get()
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result_label.config(text="Cannot divide by zero.")
            return
    else:
        result_label.config(text="Invalid operation selected.")
        return

    result_label.config(text=f"Result: {result:.2f}")

# Create the main window
Mayank_app = tk.Tk()
Mayank_app.title("CALCULATOR")

# Entry fields for input
entry_num1 = tk.Entry(Mayank_app)
entry_num2 = tk.Entry(Mayank_app)

# Radio buttons for selecting operation
operation_var = tk.StringVar()
addition = tk.Radiobutton(Mayank_app, text="+", variable=operation_var, value="+")
subtraction = tk.Radiobutton(Mayank_app, text="-", variable=operation_var, value="-")
multiplication = tk.Radiobutton(Mayank_app, text="*", variable=operation_var, value="*")
division = tk.Radiobutton(Mayank_app, text="/", variable=operation_var, value="/")

# Calculate button
calculate_button = tk.Button(Mayank_app, text="CALCULATE", command=calculate)

# Label to display result
result_label = tk.Label(Mayank_app, text="Result: ")

# Arrange widgets using grid layout
entry_num1.grid(row=0, column=0)
entry_num2.grid(row=0, column=2)
addition.grid(row=1, column=0)
subtraction.grid(row=1, column=1)
multiplication.grid(row=1, column=2)
division.grid(row=1, column=3)
calculate_button.grid(row=2, column=0, columnspan=4)
result_label.grid(row=3, column=0, columnspan=4)

# Start the GUI event loop
Mayank_app.mainloop()
