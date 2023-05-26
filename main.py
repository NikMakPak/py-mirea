'''
Архитектура приложения:
- Main
- Child
- Update
- Search
- SearchBetween
- DB
'''
import tkinter as tk
import sqlite3
import pytesseract
from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import cv2
import time

pytesseract.pytesseract.tesseract_cmd = \
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class Main(tk.Frame):
	def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    
class Child():
     def __init__(self):   

class Update(Child):
     def __init__(self):
          
class Search():
     def __init__(self):

class SearchBetween():
     def __init__(self):

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('DataBase.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS DataBase (
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , 
            lastName text, Name text, middleName text, both text, city text, 
            serialNumber integer, dateReg text, placeIssue text, 
            divisionCode integer, agresReg text, SNILS text, tax text, 
            birthCertificat text, issueCertificate text, LNMFather text,
            LNMMather text, LinkPhoto text )''')
        self.conn.commit()

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("ReadPass")
    root.geometry("1280x720")
    root.resizable(True, True)
    root.mainloop()