import tkinter as tk  # Import tkinter module for GUI

# Function triggered when any button is clicked
def click(event):
    current = entry.get()  # Get current entry text
    text = event.widget.cget("text")  # Get the text of the clicked button

    if text == "=":
        try:
            result = eval(current)  # Evaluate the entered expression
            entry.delete(0, tk.END)  # Clear the entry field
            entry.insert(tk.END, str(result))  # Display the result
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")  # Display error if evaluation fails

    elif text == "C":
        entry.delete(0, tk.END)  # Clear the entry field

    elif text == "%":
        try:
            result = eval(current) / 100  # Calculate percentage
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))  # Display the result
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    else:
        entry.insert(tk.END, text)  # Append clicked button text to entry field


# Initialize main window
root = tk.Tk()
root.title("Enhanced Calculator")
root.geometry("300x500")  # Adjusted height for aesthetic layout

# Entry widget for input/output display
entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief="solid", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Button layout matrix (row by row)
buttons = [
    ["C", "%", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0"]
]

# Create buttons row-wise
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        btn_color = "#2ecc71" if btn_text == "C" else "#dfe6e9"  # Green for 'C', default for others
        btn = tk.Button(
            frame, text=btn_text, font="Arial 18", relief="raised",
            bg=btn_color, fg="black", activebackground="#a29bfe", height=2
        )
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        btn.bind("<Button-1>", click)

# Run the Tkinter event loop
root.mainloop()



