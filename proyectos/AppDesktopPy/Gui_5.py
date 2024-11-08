import tkinter as tk
root = tk.Tk()
root.geometry("300x200")
root.title("Frame() Widget")

frame = tk.Frame(root, bg="blue", bd=5)
frame.place(relx=0.5, rely=0.5,anchor=tk.CENTER)

label1 = tk.Label(frame, text="label1", bg="green")
label2 = tk.Label(frame, text="label2", bg="red")

label1.pack()
label2.pack()

root.mainloop()