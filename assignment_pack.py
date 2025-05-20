import tkinter as tk

def compute_sum():
    try:
        number1 = int(entry1.get())
        number2 = int(entry2.get())
        result = number1 + number2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Sum Calculator")
root.geometry("400x300")

# First number
label1 = tk.Label(root, text="Enter first number")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

# Second number
label2 = tk.Label(root, text="Enter second number")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

# Compute Button
button = tk.Button(root, text="Compute Sum", command=compute_sum)
button.pack()

# Result Label
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run the application
root.mainloop()