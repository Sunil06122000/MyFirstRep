import tkinter as tk

class Chatbot():
    def __init__(self, master):
        self.master = master
        self.master.title("Sunil's Chatbot")

        BG_GRAY = "#0E80E2"
        BG_COLOR = "#040F1B"
        TEXT_COLOR = "#EAECEE"
        FONT = "Helvetica 14"
        FONT_BOLD = "Helvetica 13 bold"

        # Label
        self.label1 = tk.Label(master, bg=BG_COLOR, fg=TEXT_COLOR, text="Hey buddy", font=FONT_BOLD, pady=10, width=50, height=1)
        self.label1.grid(row=0, column=0, columnspan=2)

        # Text widget
        self.txt = tk.Text(master, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60, height=20)
        self.txt.grid(row=1, column=0, columnspan=2)

        # Scrollbar
        scrollbar = tk.Scrollbar(self.txt)
        scrollbar.place(relheight=1, relx=0.974)

        # Entry widget
        self.e = tk.Entry(master, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
        self.e.grid(row=2, column=0)

        # Send button
        self.send_button = tk.Button(master, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=self.send)
        self.send_button.grid(row=2, column=1)

    def send(self):
        SEND = "You -> " + self.e.get()
        self.txt.insert(tk.END, "\n" + SEND)

        user = self.e.get().lower()

        if user == "hello":
            self.txt.insert(tk.END, "\n" + "Bot -> Hi there, how can I help?")
        elif user in ["hi", "hii", "hiiii"]:
            self.txt.insert(tk.END, "\n" + "Bot -> Hi there, what can I do for you?")
        elif user == "how are you":
            self.txt.insert(tk.END, "\n" + "Bot -> fine! and you")
        elif user in ["fine", "i am good", "i am doing good"]:
            self.txt.insert(tk.END, "\n" + "Bot -> Great! how can I help you.")
        elif user in ["thanks", "thank you", "now its my time"]:
            self.txt.insert(tk.END, "\n" + "Bot -> My pleasure!")
        elif user in ["what do you sell", "what kinds of items are there", "have you something"]:
            self.txt.insert(tk.END, "\n" + "Bot -> We have coffee and tea")
        elif user in ["tell me a joke", "tell me something funny", "crack a funny line"]:
            self.txt.insert(tk.END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison!")
        elif user in ["goodbye", "see you later", "see yaa"]:
            self.txt.insert(tk.END, "\n" + "Bot -> Have a nice day!")
        else:
            self.txt.insert(tk.END, "\n" + "Bot -> Sorry! I didn't understand that")

        self.e.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    Chatbot(root)
    root.mainloop()