import tkinter
import factor as fact_mod
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import END

"""
Given a single positive whole integer, display all possible factors of it
Unless it is a prime, then display a message that it is a prime
"""


class FactorGUI:
    def __init__(self):
        """
        initialize core window
        """
        self.main_window = tkinter.Tk()

        # main window title
        self.title = tkinter.Tk.wm_title(self.main_window,
                                         string="Factor Calculator"
                                         )
        # main window
        self.window_size = tkinter.Tk.wm_minsize(self.main_window,
                                                 width=600, height=500)
        # menubar
        self.menubar = tkinter.Menu(self.main_window)
        self.options = tkinter.Menu(self.menubar, tearoff=0)
        self.options.add_separator()
        self.options.add_command(label="Quit", command=self.main_window.destroy)

        self.menubar.add_cascade(label="Tools", menu=self.options)

        # frames of main window
        self.top_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.scroll_frame = tkinter.Frame()

        self.prompt_label = tkinter.Label(self.top_frame,
                                          text="Number to factor: ",
                                          font=("Arial Bold", 15))

        self.factor_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side="left")
        self.factor_entry.pack(side="left")

        self.calc_btn = tkinter.Button(self.middle_frame, text="Factor!",
                                       command=self.num_validate)
        self.quit_btn = tkinter.Button(self.middle_frame, text="Quit",
                                       command=self.main_window.destroy)

        self.describe_label = tkinter.Label(self.bottom_frame,
                                            text="Factors available",
                                            font=("Arial Bold", 15))

        self.describe_label.pack(side='left')

        self.calc_btn.pack(side="left")
        self.quit_btn.pack(side="left")

        self.scroll = scrolledtext.ScrolledText(
            self.scroll_frame,
            wrap='word',
            width=30,
            height=20,
            font=("Arial", 17),
            bg='beige'
        )

        # pack the app
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        self.scroll_frame.pack()
        self.main_window.config(menu=self.menubar)

        tkinter.mainloop()

    def num_validate(self):
        """
        checks num
        """
        num = self.factor_entry.get()

        try:
            num = int(num)
        except ValueError or TypeError:
            messagebox.showerror(title="Wrong number", message=str(num) + " is not a whole number!")
            return

        if num < 0:
            messagebox.showerror(title="Wrong number", message=str(num) + " is not a positive number!")
            return

        self.calculate(num)

    def calculate(self, num):
        """
        call factor_mod
        """
        result = fact_mod.factors(num)
        result = fact_mod.clean_up(result)

        if not result:
            self.scroll.delete(1.0, END)
            self.scroll.insert('insert', format(num, ",") + " is a prime number!")
            self.scroll.pack()
        else:
            self.scroll.delete(1.0, END)

            for i in range(0, len(result)):
                self.scroll.insert('insert', "#" + str(i + 1) + ": " + result[i] + "\n")

            self.scroll.pack()


myGUI = FactorGUI()
