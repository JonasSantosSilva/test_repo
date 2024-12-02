import tkinter as tk

def show_message():
    label.config(text="Hello, World!")

# Create the main window
root = tk.Tk()
root.title("  Hello World App  ")

# Create a label
label = tk.Label(root, text="                    ", font=("Arial", 50))
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Click Me", command=show_message, font=("Arial", 16))
button.pack(pady=20)

# Run the application
root.mainloop()

