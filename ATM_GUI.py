import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize account data
account_data = {}

class ATMApp:
    def __init__(self, root):  # Corrected to __init__
        self.root = root
        self.root.title("ATM Machine")
        self.root.geometry("500x400")  # Increased window size

        # Create a main frame for better layout
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=20)

        # Login frame
        self.login_frame = tk.Frame(self.main_frame)
        self.login_frame.pack(pady=20)

        self.label_user = tk.Label(self.login_frame, text="Username:", font=("Arial", 14))
        self.label_user.grid(row=0, column=0)

        self.entry_user = tk.Entry(self.login_frame, font=("Arial", 14))
        self.entry_user.grid(row=0, column=1)

        self.label_pin = tk.Label(self.login_frame, text="PIN:", font=("Arial", 14))
        self.label_pin.grid(row=1, column=0)

        self.entry_pin = tk.Entry(self.login_frame, show='*', font=("Arial", 14))
        self.entry_pin.grid(row=1, column=1)

        self.btn_login = tk.Button(self.login_frame, text="Login", command=self.login, font=("Arial", 14), bg="blue")
        self.btn_login.grid(row=2, columnspan=2, pady=10)

    def login(self):
        username = self.entry_user.get()
        pin = self.entry_pin.get()

        if username not in account_data:
            # Create a new account with the specified username and fixed PIN
            account_data[username] = {"pin": "1234", "balance": 1000000}

        if account_data[username]["pin"] == pin:
            self.show_menu(username)
        else:
            messagebox.showerror("Error", "Invalid username or PIN")

    def show_menu(self, username):
        self.clear_frame()

        self.menu_frame = tk.Frame(self.main_frame)
        self.menu_frame.pack(pady=30)

        self.label_welcome = tk.Label(self.menu_frame, text=f"Welcome, {username}!", font=("Arial", 16))
        self.label_welcome.grid(row=0, columnspan=2)

        self.btn_balance = tk.Button(self.menu_frame, text="Check Balance", command=lambda: self.show_balance(username), font=("Arial", 14), bg="lightgreen")
        self.btn_balance.grid(row=1, column=0, padx=20, pady=10)

        self.btn_withdraw = tk.Button(self.menu_frame, text="Withdraw", command=lambda: self.withdraw(username), font=("Arial", 14), bg="lightcoral")
        self.btn_withdraw.grid(row=1, column=1, padx=20, pady=10)

        self.btn_deposit = tk.Button(self.menu_frame, text="Deposit", command=lambda: self.deposit(username), font=("Arial", 14), bg="lightyellow")
        self.btn_deposit.grid(row=2, column=0, padx=20, pady=10)

        self.btn_logout = tk.Button(self.menu_frame, text="Logout", command=self.logout, font=("Arial", 14), bg="lightgray")
        self.btn_logout.grid(row=2, column=1, padx=20, pady=10)

    def show_balance(self, username):
        balance = account_data[username]["balance"]
        messagebox.showinfo("Balance", f"Your balance is: ${balance}")

    def withdraw(self, username):
        amount = simpledialog.askinteger("Withdraw", "Enter amount to withdraw:")
        if amount is not None:
            if amount <= account_data[username]["balance"]:
                account_data[username]["balance"] -= amount
                messagebox.showinfo("Success", f"Withdrawn: ${amount}\nRemaining Balance: ${account_data[username]['balance']}")
            else:
                messagebox.showerror("Error", "Insufficient funds")

    def deposit(self, username):
        amount = simpledialog.askinteger("Deposit", "Enter amount to deposit:")
        if amount is not None:
            account_data[username]["balance"] += amount
            messagebox.showinfo("Success", f"Deposited: ${amount}\nNew Balance: ${account_data[username]['balance']}")

    def logout(self):
        self.clear_frame()
        self.login_frame.pack(pady=40)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.pack_forget()

if __name__ == "__main__":  # Corrected to __name__ and "__main__"
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()