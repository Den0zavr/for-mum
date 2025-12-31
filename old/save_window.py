import tkinter as tk
import pandas as pd
from singleton_for_path import FilePathSingleton
from suffixHandler import handleSuffix
from tkinter import Toplevel, Button, Label, Entry, StringVar, filedialog


class save_file_window(Toplevel):
    def __init__(self):
        super().__init__()
        extensions = [".xlsx", ".xls"]
        self.selected_option = StringVar(self)
        self.selected_option.set(extensions[0])
        self.title("Сохранение файла")
        self.geometry("400x200")
        self.resizable(1, 1)
        self.entry = Entry(self, 
                           width = 45)
        self.entry.pack()
        self.label = Label(self,
                     text = "Выбери расширение из списка")
        self.label.pack()
        self.dropdown_menu = tk.OptionMenu(self,
                                        self.selected_option,
                                        *extensions)
        self.dropdown_menu.pack()
        self.save_button = Button(self, 
                             text="Сохранить",
                             command = self.click_to_save)
        self.save_button.pack()
        self.mainloop()

    def click_to_save(self):
        file = FilePathSingleton()
        df = pd.read_excel(file.get_file_path())
        dir_to_save = filedialog.askdirectory(mustexist = True)
        file.remove_file_path()
        file.set_file_path(dir_to_save + "/" + self.entry.get() + self.selected_option.get())
        saved_file = pd.DataFrame(df)
        saved_file.to_excel(self.entry.get() + self.selected_option.get(), index = False)
        print(file.get_file_path())
        self.save_label = Label(self, 
                                text = f"Файл {self.entry.get() + self.selected_option.get()} сохранен в {dir_to_save}")
        self.save_label.pack()