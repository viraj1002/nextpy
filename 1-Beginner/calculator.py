import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("300x400")

        self.current_input = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.entry = tk.Entry(master, textvariable=self.result_var, font=("Arial", 20), bd=10, insertwidth=4, width=14, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(master, text=button, padx=20, pady=20, font=("Arial", 16), command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(master, text="C", padx=20, pady=20, font=("Arial", 16), command=self.clear_last).grid(row=row_val, column=0)
        tk.Button(master, text="AC", padx=20, pady=20, font=("Arial", 16), command=self.clear_all).grid(row=row_val, column=1)

    def button_click(self, value):
        current_display = self.result_var.get()

        if current_display == "ERR":
            self.result_var.set("0")
            return

        if value in '0123456789':
            if len(self.current_input) < 8:
                self.current_input += value
                self.result_var.set(self.current_input)

        elif value in '+-*/':
            if current_display != "ERR":
                self.current_input += value
                self.result_var.set(self.current_input)

        elif value == '=':
            if current_display != "ERR":
                try:
                    result = str(self.calculate_result())
                    self.result_var.set(result)
                except:
                    self.result_var.set("ERR")

    def calculate_result(self):
        return eval(self.current_input)

    def clear_last(self):
        current_display = self.result_var.get()
        if current_display != "ERR" and len(self.current_input) > 1:
            self.current_input = self.current_input[:-1]
            self.result_var.set(self.current_input)
        else:
            self.result_var.set("0")
            self.current_input = ""

    def clear_all(self):
        self.result_var.set("0")
        self.current_input = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
