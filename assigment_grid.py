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
root.geometry("350x150")

# Labels
label1 = tk.Label(root, text="Enter first number")
label1.grid(row=0, column=0, padx=5, pady=5, sticky='e')

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)

label2 = tk.Label(root, text="Enter second number")
label2.grid(row=1, column=0, padx=5, pady=5, sticky='e')

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)

# Button to compute sum
button = tk.Button(root, text="Compute Sum", command=compute_sum)
button.grid(row=2, column=1, padx=5, pady=10, sticky='w')

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=3, column=1, padx=5, pady=5, sticky='w')

# Run the application
root.mainloop()