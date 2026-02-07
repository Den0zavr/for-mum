from tkinter import *; from tkinter import filedialog
from singleton_for_path import FilePathSingleton
from singleton import Singleton
from saveWindow import save_file_window
from extractWindow import extract_data_window
from suffixHandler import handleSuffix

class window(Tk, Singleton):
    def init(self):
        super().__init__()
        self.title("Для мамы")
        self.geometry("640x640")
        self.resizable(1, 1)
        self.open_button = Button(self, 
                             text="Открыть файл", 
                             command=self.openfile)
        self.open_button.grid(column=0, row=1)    
        self.extract_button = Button(self, 
                             text="Извлечь данные из файла", 
                             command=self.call_extract_data_window)
        self.extract_button.grid(column=1, row=1)
        self.save_button = Button(self, 
                             text="Сохранить файл", 
                             command=self.call_save_file_window)
        self.save_button.grid(column=2, row=1)        

    def openfile(self):
        file = FilePathSingleton()
        file.set_file_path(filedialog.askopenfilename( 
            title="Выбери файл", 
            initialdir="/home/denozavr/for_mum",
            filetypes=[("Старый формат эксель", "*.xls"), 
                       ("Новый формат эксель", "*.xlsx"), 
                       ("Все типы", "*.*")]))
        print("Открыт этот файл:", file.get_file_path())
        match file.get_file_suffix():
            case ".xlsx":
                handleSuffix().is_xlsx(file)
            case ".xls":
                handleSuffix().is_xls(file)
            case _:
                print(f"Выбран файл с другим расширением - ", file.get_file_suffix())
        print("После открытия работаю с этим файлом:", file.get_file_path())

    def call_extract_data_window(self):
        global ExtractWindow
        ExtractWindow = extract_data_window()

    def call_save_file_window(self):
        global SaveWindow
        SaveWindow = save_file_window()

    def __init__(self):
        ...