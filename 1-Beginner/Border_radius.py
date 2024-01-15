import tkinter as tk

class BorderRadiusPreviewer:
    def __init__(self, master):
        self.master = master
        master.title("Border-radius Previewer")

        self.top_left_label = tk.Label(master, text="Top-Left:")
        self.top_left_entry = tk.Entry(master)
        self.top_left_label.grid(row=0, column=0)
        self.top_left_entry.grid(row=0, column=1)

        self.top_right_label = tk.Label(master, text="Top-Right:")
        self.top_right_entry = tk.Entry(master)
        self.top_right_label.grid(row=0, column=2)
        self.top_right_entry.grid(row=0, column=3)

        self.bottom_left_label = tk.Label(master, text="Bottom-Left:")
        self.bottom_left_entry = tk.Entry(master)
        self.bottom_left_label.grid(row=1, column=0)
        self.bottom_left_entry.grid(row=1, column=1)

        self.bottom_right_label = tk.Label(master, text="Bottom-Right:")
        self.bottom_right_entry = tk.Entry(master)
        self.bottom_right_label.grid(row=1, column=2)
        self.bottom_right_entry.grid(row=1, column=3)

        self.update_button = tk.Button(master, text="Update Preview", command=self.update_preview)
        #self.copy_button = tk.Button(master, text="Copy CSS", command=self.copy_to_clipboard)

        self.update_button.grid(row=2, column=0, columnspan=2)
        #self.copy_button.grid(row=2, column=2, columnspan=2)

        self.preview_box = tk.Canvas(master, width=200, height=200, bg="lightblue", bd=2, relief="solid")
        self.preview_box.grid(row=3, column=0, columnspan=4)

    def update_preview(self):
        try:
            top_left = int(self.top_left_entry.get())
            top_right = int(self.top_right_entry.get())
            bottom_left = int(self.bottom_left_entry.get())
            bottom_right = int(self.bottom_right_entry.get())

            self.preview_box.config(borderwidth=2, relief="solid", highlightthickness=0)
            self.preview_box.create_rectangle(0, 0, 200, 200, outline="#333", width=2, tags="border")
            self.preview_box.create_rectangle(1, 1, 199, 199, fill="lightblue", outline="")
            self.preview_box.create_rectangle(0, 0, top_left, top_left, outline="#333", fill="")
            self.preview_box.create_rectangle(200 - top_right, 0, 200, top_right, outline="#333", fill="")
            self.preview_box.create_rectangle(0, 200 - bottom_left, bottom_left, 200, outline="#333", fill="")
            self.preview_box.create_rectangle(200 - bottom_right, 200 - bottom_right, 200, 200, outline="#333", fill="")
        except ValueError:
            pass

    def copy_to_clipboard(self):
        try:
            css_value = f"border-radius: {self.top_left_entry.get()}px {self.top_right_entry.get()}px " \
                        f"{self.bottom_left_entry.get()}px {self.bottom_right_entry.get()}px;"
            self.master.clipboard_clear()
            self.master.clipboard_append(css_value)
            self.master.update()
            tk.messagebox.showinfo("Copied", "CSS copied to clipboard!")
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BorderRadiusPreviewer(root)
    root.mainloop()
