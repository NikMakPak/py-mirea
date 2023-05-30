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
        
    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='add.gif')
        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию',
                                    command=self.open_dialog, bg='#d7d8e0',
                                    bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='update.gif')
        btn_edit_dialog = tk.Button(toolbar, text='Редактировать',
                                    bg='#d7d8e0', bd=0, image=self.update_img,
                                    compound=tk.TOP,
                                    command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.RIGHT)

        self.delete_img = tk.PhotoImage(file='delete.gif')
        btn_delete = tk.Button(toolbar, text='Удалить позицию', bg='#d7d8e0',
                               bd=0, image=self.delete_img,
                               compound=tk.TOP, command=self.delete_records)
        btn_delete.pack(side=tk.RIGHT)

        self.search_img = tk.PhotoImage(file='search.gif')
        btn_search = tk.Button(toolbar, text='Поиск', bg='#d7d8e0', bd=0,
                               image=self.search_img,
                               compound=tk.TOP,
                               command=self.open_search_dialog)
        btn_search.pack(side=tk.RIGHT)

        self.refresh_img = tk.PhotoImage(file='refresh.gif')
        btn_refresh = tk.Button(toolbar, text='Обновить', bg='#d7d8e0', bd=0,
                                image=self.refresh_img,
                                compound=tk.TOP, command=self.view_records)
        btn_refresh.pack(side=tk.RIGHT)

        # self.aboutImage = Image.open('about.png')
        # self.aboutImage = self.aboutImage.resize((45, 45))
        # self.aboutImage = ImageTk.PhotoImage(self.aboutImage)
        # btn_about = tk.Button(toolbar, text='Об авторах', bg='#d7d8e0', bd=0,
        #                       compound=tk.TOP, image=self.aboutImage,
        #                       command=AboutUs)
        # btn_about.place(relx=0.45, rely=0.1)

        pasInfo = tk.Frame(bg='#d7d8e0', bd=2)
        pasInfo.pack(side=tk.TOP)

        self.label_f = tk.Label(pasInfo,
                                text='                                                                                                                                          ')
        self.label_f.pack(side=tk.LEFT)
        self.label_f = tk.Label(pasInfo,
                                text='                                                                                                                                        ')
        self.label_f.pack(side=tk.RIGHT)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)
        self.label_f = tk.Label(pasInfo, text='')
        self.label_f.pack(side=tk.TOP)

        self.canvas = Canvas(pasInfo, width=190, height=285)
        self.canvas.place(x=1, y=10)

        # self.img1 = ImageTk.PhotoImage(file="images/pas2.png")
        #
        # self.image_container = self.canvas.create_image(0, 0, anchor="nw",
        #                                                 image=self.img1)
        # self.canvas.itemconfig(self.image_container, image=self.img1)

        X1 = 200
        X2 = 330
        X3 = 450
        Y = 20

        self.label_f = tk.Label(pasInfo, text='Фамилия:')
        self.label_f.place(x=X1, y=0)
        self.value_lastName = tk.Label(pasInfo, text='ФАМИЛИЯ')
        self.value_lastName.place(x=X2, y=Y * 0)

        self.label_f2 = tk.Label(pasInfo, text='Имя:')
        self.label_f2.place(x=X1, y=Y * 1)
        self.value_name = tk.Label(pasInfo, text='ИМЯ')
        self.value_name.place(x=X2, y=Y * 1)

        self.label_f3 = tk.Label(pasInfo, text='Отчество:')
        self.label_f3.place(x=X1, y=Y * 2)
        self.value_midleName = tk.Label(pasInfo, text='Отчество')
        self.value_midleName.place(x=X2, y=Y * 2)

        self.label_f4 = tk.Label(pasInfo, text='Дата рождения:')
        self.label_f4.place(x=X1, y=Y * 3)
        self.value_birth = tk.Label(pasInfo, text='00.00.0000')
        self.value_birth.place(x=X2, y=Y * 3)

        self.label_f5 = tk.Label(pasInfo, text='Место рождения:')
        self.label_f5.place(x=X1, y=Y * 4)
        self.value_placeBirth = tk.Label(pasInfo, text='МЕСТО РОЖДЕНИЯ')
        self.value_placeBirth.place(x=X2, y=Y * 4)

        self.label_f6 = tk.Label(pasInfo, text='Серийный номер:')
        self.label_f6.place(x=X1, y=Y * 6)
        self.value_Namber = tk.Label(pasInfo, text='00 00 000000')
        self.value_Namber.place(x=X2, y=Y * 6)

        self.label_f7 = tk.Label(pasInfo, text='Дата выдачи:')
        self.label_f7.place(x=X1, y=Y * 7)
        self.value_dateGet = tk.Label(pasInfo, text='00.00.0000')
        self.value_dateGet.place(x=X2, y=Y * 7)

        self.label_f3 = tk.Label(pasInfo, text='Паспорт выдан:')
        self.label_f3.place(x=X1, y=Y * 8)
        self.value_whoGet = tk.Label(pasInfo, text='ПАСПОРТ ВЫДАН')
        self.value_whoGet.place(x=X2, y=Y * 8)

        self.label_f4 = tk.Label(pasInfo, text='Код подразделения:')
        self.label_f4.place(x=X1, y=Y * 10)
        self.value_codeWho = tk.Label(pasInfo, text='000-000')
        self.value_codeWho.place(x=X2, y=Y * 10)

        self.label_f5 = tk.Label(pasInfo, text='Адрес регистрации:')
        self.label_f5.place(x=X3, y=0)
        self.value_adresReg = tk.Label(pasInfo, text='Адрес регистрации')
        self.value_adresReg.place(x=X3 + 200, y=20 * 0)

        self.label_f6 = tk.Label(pasInfo, text='СНИЛС:')
        self.label_f6.place(x=X3, y=20 * 3)
        self.value_snils = tk.Label(pasInfo, text='Свидетельство выдано')
        self.value_snils.place(x=X3 + 200, y=20 * 3)

        self.label_f7 = tk.Label(pasInfo, text='ИНН:')
        self.label_f7.place(x=X3, y=20 * 4)
        self.value_tax = tk.Label(pasInfo, text='Свидетельство выдано')
        self.value_tax.place(x=X3 + 200, y=20 * 4)

        self.label_f3 = tk.Label(pasInfo, text='Номер свидетельства:')
        self.label_f3.place(x=X3, y=20 * 5)
        self.value_certNum = tk.Label(pasInfo, text='Номер свидетельства')
        self.value_certNum.place(x=X3 + 200, y=20 * 5)

        self.label_f = tk.Label(pasInfo, text='Свидетельство выдано')
        self.label_f.place(x=X3, y=20 * 6)
        self.value_certPlace = tk.Label(pasInfo, text='Свидетельство выдано:')
        self.value_certPlace.place(x=X3 + 200, y=20 * 6)

        self.label_f5 = tk.Label(pasInfo, text='ФИО отца:')
        self.label_f5.place(x=X3, y=20 * 11)
        self.value_LNMFather = tk.Label(pasInfo, text='ФИО отца')
        self.value_LNMFather.place(x=X3 + 200, y=20 * 11)

        self.label_f6 = tk.Label(pasInfo, text='ФИО матери:')
        self.label_f6.place(x=X3, y=20 * 13)
        self.value_LNMMather = tk.Label(pasInfo, text='ФИО матери')
        self.value_LNMMather.place(x=X3 + 200, y=20 * 13)

        self.tree = ttk.Treeview(self, columns=(
            'ID', 'lastName', 'Name', 'middleName', 'both', 'city',
            'serialNumber',
            'dateReg', 'placeIssue', 'divisionCode', 'agresReg', 'SNILS',
            'tax',
            'birthCertificat', 'issueCertificate', 'LNMFather', 'LNMMather'),
                                 height=15, show='headings')
        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('lastName', width=75, anchor=tk.CENTER)
        self.tree.column('Name', width=90, anchor=tk.CENTER)
        self.tree.column('middleName', width=140, anchor=tk.CENTER)
        self.tree.column('both', width=100, anchor=tk.CENTER)
        self.tree.column('city', width=100, anchor=tk.CENTER)
        self.tree.column('serialNumber', width=120, anchor=tk.CENTER)
        self.tree.column('dateReg', width=100, anchor=tk.CENTER)
        self.tree.column('placeIssue', width=100, anchor=tk.CENTER)
        self.tree.column('divisionCode', width=80, anchor=tk.CENTER)
        self.tree.column('agresReg', width=100, anchor=tk.CENTER)
        self.tree.column('SNILS', width=100, anchor=tk.CENTER)
        self.tree.column('tax', width=100, anchor=tk.CENTER)
        self.tree.column('birthCertificat', width=100, anchor=tk.CENTER)
        self.tree.column('issueCertificate', width=100, anchor=tk.CENTER)
        self.tree.column('LNMFather', width=100, anchor=tk.CENTER)
        self.tree.column('LNMMather', width=100, anchor=tk.CENTER)

        vsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(xscrollcommand=vsb.set)
        vsb.place(rely=0.97, relwidth=1, anchor=W, height=15)
        
        def select_item(a):
            curItem = self.tree.focus()
            if curItem != '':
                self.value_lastName.config(
                    text=self.tree.item(curItem)['values'][1])
                self.value_name.config(
                    text=self.tree.item(curItem)['values'][2])
                self.value_midleName.config(
                    text=self.tree.item(curItem)['values'][3])
                self.value_birth.config(
                    text=self.tree.item(curItem)['values'][4])
                self.value_placeBirth.config(
                    text=self.tree.item(curItem)['values'][5])
                self.value_Namber.config(
                    text=self.tree.item(curItem)['values'][6])
                self.value_dateGet.config(
                    text=self.tree.item(curItem)['values'][7])
                self.value_whoGet.config(
                    text=self.tree.item(curItem)['values'][8])
                self.value_codeWho.config(
                    text=self.tree.item(curItem)['values'][9])
                self.value_adresReg.config(
                    text=self.tree.item(curItem)['values'][10])
                self.value_snils.config(
                    text=self.tree.item(curItem)['values'][11])
                self.value_tax.config(
                    text=self.tree.item(curItem)['values'][12])
                self.value_certNum.config(
                    text=self.tree.item(curItem)['values'][13])
                self.value_certPlace.config(
                    text=self.tree.item(curItem)['values'][14])
                self.value_LNMFather.config(
                    text=self.tree.item(curItem)['values'][15])
                self.value_LNMMather.config(
                    text=self.tree.item(curItem)['values'][16])

                try:
                    tempImg = Image.open(self.tree.item(curItem)['values'][17])
                    tempImg = tempImg.resize((195, 285), Image.LANCZOS)
                    self.img1 = ImageTk.PhotoImage(tempImg)
                    self.image_container = self.canvas.create_image(0, 0,
                                                                    anchor="nw",
                                                                    image=self.img1)
                    self.canvas.itemconfig(self.image_container,
                                           image=self.img1)
                except:
                    print("Фото не найдено")

        self.tree.heading('ID', text='ID')
        self.tree.heading('lastName', text='Фамилия')
        self.tree.heading('Name', text='Имя')
        self.tree.heading('middleName', text='Отчество')
        self.tree.heading('both', text='Дата рождения')
        self.tree.heading('city', text='Место рождения')
        self.tree.heading('serialNumber', text='Серийный номер')
        self.tree.heading('dateReg', text='Дата выдачи')
        self.tree.heading('placeIssue', text='Паспорт выдан')
        self.tree.heading('divisionCode', text='Код подразделения')
        self.tree.heading('agresReg', text='Адрес регистрации')
        self.tree.heading('SNILS', text='СНИЛС')
        self.tree.heading('tax', text='ИНН')
        self.tree.heading('birthCertificat',
                          text='Номер сведетельства о рождении')
        self.tree.heading('issueCertificate',
                          text='Орган выдачи сведетельства')
        self.tree.heading('LNMFather', text='ФИО отца')
        self.tree.heading('LNMMather', text='ФИО матери')
        self.tree.bind('<ButtonRelease-1>', select_item)

        self.tree.pack(side=tk.LEFT)
        curItem = self.tree.focus()
        print(self.tree.item(curItem))

        scroll = tk.Scrollbar(self, command=self.tree.yview)
        scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scroll.set)

    def records(self, lastName, Name, middleName, both, city, serialNumber,
                dateReg, placeIssue, divisionCode, agresReg, SNILS, tax,
                birthCertificat, issueCertificate, LNMFather, LNMMather,
                LinkPhoto):
        self.db.insert_data(lastName, Name, middleName, both, city,
                            serialNumber, dateReg, placeIssue, divisionCode,
                            agresReg, SNILS, tax, birthCertificat,
                            issueCertificate, LNMFather, LNMMather, LinkPhoto)
        self.view_records()

    def update_record(self, lastName, Name, middleName, both, city,
                      serialNumber, dateReg, placeIssue, divisionCode,
                      agresReg, SNILS, tax, birthCertificat, issueCertificate,
                      LNMFather, LNMMather, LinkPhoto):
        self.db.c.execute('''UPDATE DataBase SET lastName=?, Name=?, 
                          middleName=?, both=?, city=?, serialNumber=?, 
                          dateReg=?, placeIssue=?, divisionCode=?, agresReg=?,
                          SNILS=?, tax=?, birthCertificat=?, 
                          issueCertificate=?, LNMFather=?, LNMMather=?,
                          LinkPhoto=?  WHERE ID=?''',
                          (
                              lastName, Name, middleName, both, city,
                              serialNumber,
                              dateReg, placeIssue, divisionCode, agresReg,
                              SNILS,
                              tax, birthCertificat, issueCertificate,
                              LNMFather,
                              LNMMather, LinkPhoto,
                              self.tree.set(self.tree.selection()[0], '#1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM DataBase''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in
         self.db.c.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.c.execute('''DELETE FROM DataBase WHERE id=?''',
                              [self.tree.set(selection_item, '#1')])
        self.db.conn.commit()
        self.view_records()
	
    def search_records(self, description):
        description = '%' + description + '%'
        sqlString = f"""SELECT * FROM DataBase  
        WHERE lastName LIKE '{description}'  OR Name LIKE '{description}' 
        OR middleName LIKE '{description}'  OR both LIKE '{description}' 
        OR city LIKE '{description}'  OR serialNumber LIKE '{description}' 
        OR dateReg LIKE '{description}'  OR placeIssue LIKE '{description}' 
        OR divisionCode LIKE '{description}'  OR agresReg LIKE '{description}' 
        OR SNILS LIKE '{description}' OR tax LIKE '{description}' 
        OR birthCertificat LIKE '{description}' 
        OR issueCertificate LIKE '{description}' 
        OR LNMFather LIKE '{description}' OR LNMMather LIKE '{description}' 
        OR LinkPhoto LIKE '{description}' OR ID LIKE '{description}'"""
        self.db.c.execute(sqlString)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in
         self.db.c.fetchall()]

    def search_between(self, firstValue, secondValue):
        sqlString = f"""SELECT * FROM DataBase WHERE both 
        BETWEEN {firstValue} and {secondValue} 
        OR serialNumber BETWEEN {firstValue} and {secondValue} 
        OR dateReg BETWEEN {firstValue} and {secondValue} 
        OR divisionCode BETWEEN {firstValue} and {secondValue} 
        OR SNILS BETWEEN {firstValue} and {secondValue}
        OR tax BETWEEN {firstValue} and {secondValue} 
        OR birthCertificat BETWEEN {firstValue} and {secondValue}
        OR ID BETWEEN {firstValue} and {secondValue}"""
        self.db.c.execute(sqlString)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in
         self.db.c.fetchall()]

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.croppedImg = None
        self.init_child()
        self.view = app

        self.SecondX = None
        self.SecondY = None
        self.FirstX = None
        self.FirstY = None
        self.img = None
        self.image_container = None
        self.linkPhoto = None

    def init_child(self):
        self.title('Добавить данные')
        self.geometry('1200x900')
        self.resizable(False, False)

        def monochrome(file, tresh):
            img_grey = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

            img_binary = \
                cv2.threshold(img_grey, tresh, 600, cv2.THRESH_BINARY)[1]
            cv2.imwrite(file, img_binary)

        def load_photo():
            try:
                canvas.delete("all")
                self.img = tk.filedialog.askopenfilename()
                self.img = Image.open(self.img)
                self.img = resize_image(self.img, 600)
                image = ImageTk.PhotoImage(self.img)
                self.image_container = canvas.create_image(0, 0, anchor='nw',
                                                      image=image)
                canvas.place(x=400, y=0)
                canvas.config(width=self.img.width, height=self.img.height)
                root.mainloop()
            except:
                print("Что то сломалось")

        def reload_photo():
            try:
                canvas.delete("all")
                image = ImageTk.PhotoImage(self.img)
                self.image_container = canvas.create_image(0, 0, anchor='nw',
                                                      image=image)
                canvas.place(x=400, y=0)
                root.mainloop()
            except:
                print("Что-то сломалось")

        def resize_image(image, fixed_w):
            fixed_width = fixed_w
            width_percent = (fixed_width / float(image.size[0]))
            height_size = int((float(image.size[0]) * float(width_percent)))
            new_image = image.resize((fixed_width, height_size))
            return new_image

        def first_point_crop(event):
            print(event.x, event.y)

            self.FirstX = event.x
            self.FirstY = event.y
            reload_photo()

        def second_point_crop(event):
            print(event.x, event.y)

            self.SecondX = event.x
            self.SecondY = event.y

            if (self.SecondX < 0):
                self.SecondX = 0
            if (self.SecondY < 0):
                self.SecondY = 0
            if (self.SecondX > self.img.width):
                self.SecondX = self.img.width
            if (self.SecondY > self.img.height):
                self.SecondY = self.img.height

            canvas.create_rectangle(self.FirstX, self.FirstY, self.SecondX, self.SecondY,
                                    outline="red")

        def crop_image():
            if self.FirstX == self.SecondX and self.FirstY == self.SecondY:
                return 0

            if self.img != None:
                if self.FirstX < self.SecondX and self.FirstY < self.SecondY:
                    croppedImg = self.img.crop((self.FirstX, self.FirstY, self.SecondX, self.SecondY))
                elif self.FirstX < self.SecondX and self.FirstY > self.SecondY:
                    croppedImg = self.img.crop((self.FirstX, self.SecondY, self.SecondX, self.FirstY))
                elif self.FirstX > self.SecondX and self.FirstY < self.SecondY:
                    croppedImg = self.img.crop((self.SecondX, self.FirstY, self.FirstX, self.SecondY))
                elif self.FirstX > self.SecondX and self.FirstY > self.SecondY:
                    croppedImg = self.img.crop((self.SecondX, self.SecondY, self.FirstX, self.FirstY))

            return croppedImg

        def scan_photo(velue, arg="none"):
            croppedImg = crop_image()

            if arg == "serial":
                croppedImg = croppedImg.rotate(90, expand=True)

            croppedImg.save('temp.png', quality=95)
            testPhoto = cv2.imread('temp.png')

            config = r'--oem 3 --psm 6'

            tempResult = pytesseract.image_to_string(testPhoto, lang="rus",
                                                     config=config)

            result = ""

            for i in tempResult:
                if i != '[' and i != ']' and i != '|' and i != '{' and i != '}':
                    result += i

            velue.delete(0, 'end')
            velue.insert(0, result)

            print(result)
            print("Success")

        def cut_photo():
            self.img = crop_image(self.img)
            self.img = resize_image(self.img, 600)
            canvas.delete("all")
            image = ImageTk.PhotoImage(self.img)
            self.image_container = canvas.create_image(0, 0, anchor='nw',
                                                  image=image)
            canvas.place(x=400, y=0)
            root.mainloop()

        def load_pass_photo(X2, Y):

            try:
                photo = crop_image(self.img)
                photo = resize_image(photo, 80)
                new_canvas.delete("all")
                image = ImageTk.PhotoImage(photo)
                self.image_container = new_canvas.create_image(0, 0, anchor='nw',
                                                          image=image)
                new_canvas.place(x=X2, y=Y + 30 * 16)
                self.linkPhoto = "images/" + repr(time.time()) + ".png"
                photo.save(self.linkPhoto, quality=95)
            except:
                print("Ошибка загрузки фото")
            root.mainloop()

        canvas = Canvas(self, width=800, height=800)
        canvas.place(x=400, y=50)

        canvas.bind("<ButtonPress-1>", first_point_crop)
        canvas.bind("<ButtonRelease-1>", second_point_crop)



        self.SecondX = 0
        self.SecondY = 0
        self.FirstX = 0
        self.FirstY = 0
        self.img = None
        self.linkPhoto = ''

        X1 = 50
        Y = 50
        X2 = 260

        new_canvas = Canvas(self, width=80, height=120)
        new_canvas.place(x=X2, y=Y + 30 * 16)

        self.velue_LastName = ttk.Entry(self)
        self.velue_LastName.place(x=X2, y=Y)
        label_description = tk.Button(self, text='Фамилия:',
                                      command=lambda: scan_photo(
                                          self.velue_LastName))
        label_description.place(x=X1, y=Y)

        self.velue_Name = ttk.Entry(self)
        self.velue_Name.place(x=X2, y=Y + 30)
        label_description = tk.Button(self, text='Имя:',
                                      command=lambda: scan_photo(
                                          self.velue_Name))
        label_description.place(x=X1, y=Y + 30)

        self.velue_MiddleName = ttk.Entry(self)
        self.velue_MiddleName.place(x=X2, y=Y + 30 * 2)
        label_description = tk.Button(self, text='Отчество:',
                                      command=lambda: scan_photo(
                                          self.velue_MiddleName))
        label_description.place(x=X1, y=Y + 30 * 2)

        self.velue_Both = ttk.Entry(self)
        self.velue_Both.place(x=X2, y=Y + 30 * 3)
        label_description = tk.Button(self, text='Дата рождения:',
                                      command=lambda: scan_photo(
                                          self.velue_Both))
        label_description.place(x=X1, y=Y + 30 * 3)

        self.velue_City = ttk.Entry(self)
        self.velue_City.place(x=X2, y=Y + 30 * 4)
        label_description = tk.Button(self, text='Место рождения:',
                                      command=lambda: scan_photo(
                                          self.velue_City))
        label_description.place(x=X1, y=Y + 30 * 4)

        self.velue_SerialNumber = ttk.Entry(self)
        self.velue_SerialNumber.place(x=X2, y=Y + 30 * 5)
        serial_description = tk.Button(self, text='Серия и номер:',
                                       command=lambda: scan_photo(
                                           self.velue_SerialNumber, "serial"))
        serial_description.place(x=X1, y=Y + 30 * 5)

        self.velue_dateReg = ttk.Entry(self)
        self.velue_dateReg.place(x=X2, y=Y + 30 * 6)
        label_description = tk.Button(self, text='Дата выдачи:',
                                      command=lambda: scan_photo(
                                          self.velue_dateReg))
        label_description.place(x=X1, y=Y + 30 * 6)

        self.velue_placeIssue = ttk.Entry(self)
        self.velue_placeIssue.place(x=X2, y=Y + 30 * 7)
        label_description = tk.Button(self, text='Паспорт выдан:',
                                      command=lambda: scan_photo(
                                          self.velue_placeIssue))
        label_description.place(x=X1, y=Y + 30 * 7)

        self.velue_divisionCode = ttk.Entry(self)
        self.velue_divisionCode.place(x=X2, y=Y + 30 * 8)
        label_description = tk.Button(self, text='Код подразделения:',
                                      command=lambda: scan_photo(
                                          self.velue_divisionCode))
        label_description.place(x=X1, y=Y + 30 * 8)

        self.velue_agresReg = ttk.Entry(self)
        self.velue_agresReg.place(x=X2, y=Y + 30 * 9)
        label_description = tk.Button(self, text='Адрес регистрации:',
                                      command=lambda: scan_photo(
                                          self.velue_agresReg))
        label_description.place(x=X1, y=Y + 30 * 9)

        self.velue_SNILS = ttk.Entry(self)
        self.velue_SNILS.place(x=X2, y=Y + 30 * 10)
        label_description = tk.Button(self, text='СНИЛС:',
                                      command=lambda: scan_photo(
                                          self.velue_SNILS))
        label_description.place(x=X1, y=Y + 30 * 10)

        self.velue_tax = ttk.Entry(self)
        self.velue_tax.place(x=X2, y=Y + 30 * 11)
        label_description = tk.Button(self, text='ИНН:',
                                      command=lambda: scan_photo(
                                          self.velue_tax))
        label_description.place(x=X1, y=Y + 30 * 11)

        self.velue_birthCertificat = ttk.Entry(self)
        self.velue_birthCertificat.place(x=X2, y=Y + 30 * 12)
        label_description = tk.Button(self,
                                      text='Номер сведетельства о рождении:',
                                      command=lambda: scan_photo(
                                          self.velue_birthCertificat))
        label_description.place(x=X1, y=Y + 30 * 12)

        self.velue_issueCertificate = ttk.Entry(self)
        self.velue_issueCertificate.place(x=X2, y=Y + 30 * 13)
        label_description = tk.Button(self, text='Орган выдачи сведетельства:',
                                      command=lambda: scan_photo(
                                          self.velue_issueCertificate))
        label_description.place(x=X1, y=Y + 30 * 13)

        self.velue_LNMFather = ttk.Entry(self)
        self.velue_LNMFather.place(x=X2, y=Y + 30 * 14)
        label_description = tk.Button(self, text='ФИО отца:',
                                      command=lambda: scan_photo(
                                          self.velue_LNMFather))
        label_description.place(x=X1, y=Y + 30 * 14)

        self.velue_LNMMather = ttk.Entry(self)
        self.velue_LNMMather.place(x=X2, y=Y + 30 * 15)
        label_description = tk.Button(self, text='ФИО матери:',
                                      command=lambda: scan_photo(
                                          self.velue_LNMMather))
        label_description.place(x=X1, y=Y + 30 * 15)

        self.velue_LinkPhoto = ttk.Entry(self)
        # self.velue_LinkPhoto.place(x=X2, y=Y + 30*16)
        label_description = tk.Button(self, text='Фото:',
                                      command=lambda: load_pass_photo(X2, Y))
        label_description.place(x=X1, y=Y + 30 * 16)

        self.btn_ok = ttk.Button(self, text="Сканировать фото",
                                 command=lambda: load_photo())
        self.btn_ok.place(x=60, y=Y + 30 * 20)

        self.btn_cut = ttk.Button(self, text="Обрезать",
                                  command=lambda: cut_photo())
        self.btn_cut.place(x=200, y=Y + 30 * 20)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=Y + 30 * 21 + 50)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(
            self.velue_LastName.get(),
            self.velue_Name.get(),
            self.velue_MiddleName.get(),
            self.velue_Both.get(),
            self.velue_City.get(),
            self.velue_SerialNumber.get(),
            self.velue_dateReg.get(),
            self.velue_placeIssue.get(),
            self.velue_divisionCode.get(),
            self.velue_agresReg.get(),
            self.velue_SNILS.get(),
            self.velue_tax.get(),
            self.velue_birthCertificat.get(),
            self.velue_issueCertificate.get(),
            self.velue_LNMFather.get(),
            self.velue_LNMMather.get(),
            self.linkPhoto
        ))

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=Y + 30 * 21 + 50)

        self.grab_set()
        self.focus_set()   

class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app
        self.db = db
        self.default_data()

    def init_edit(self):
        self.title('Редактировать позицию')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=200, y=50 + 30 * 21 + 50)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(
            self.velue_LastName.get(),
            self.velue_Name.get(),
            self.velue_MiddleName.get(),
            self.velue_Both.get(),
            self.velue_City.get(),
            self.velue_SerialNumber.get(),
            self.velue_dateReg.get(),
            self.velue_placeIssue.get(),
            self.velue_divisionCode.get(),
            self.velue_agresReg.get(),
            self.velue_SNILS.get(),
            self.velue_tax.get(),
            self.velue_birthCertificat.get(),
            self.velue_issueCertificate.get(),
            self.velue_LNMFather.get(),
            self.velue_LNMMather.get(),
            self.velue_LinkPhoto.get()
        ))
        self.btn_ok.destroy()

    def default_data(self):
        self.db.c.execute('''SELECT * FROM DataBase WHERE id=?''',
                          (self.view.tree.set(self.view.tree.selection()[0],
                                              '#1'),))
        row = self.db.c.fetchone()
        self.velue_LastName.insert(0, row[1])
        self.velue_Name.insert(0, row[2])
        self.velue_MiddleName.insert(0, row[3])
        self.velue_Both.insert(0, row[4])
        self.velue_City.insert(0, row[5])
        self.velue_SerialNumber.insert(0, row[6]),
        self.velue_dateReg.insert(0, row[7])
        self.velue_placeIssue.insert(0, row[8])
        self.velue_divisionCode.insert(0, row[9])
        self.velue_agresReg.insert(0, row[10])
        self.velue_SNILS.insert(0, row[11])
        self.velue_tax.insert(0, row[12])
        self.velue_birthCertificat.insert(0, row[13])
        self.velue_issueCertificate.insert(0, row[14])
        self.velue_LNMFather.insert(0, row[15])
        self.velue_LNMMather.insert(0, row[16])
        self.velue_LinkPhoto.insert(0, row[17])
          
class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск')
        self.geometry('300x120')
        self.resizable(False, False)

        label_search = tk.Label(self, text='Поиск')
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(x=105, y=50)

        btn_search_between = ttk.Button(self, text='Поиск между')
        btn_search_between.place(x=20, y=50)

        btn_search.bind('<Button-1>', lambda event: self.view.search_records(
            self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

        btn_search_between.bind('<Button-1>', lambda event: SearchBetween())
        btn_search_between.bind('<Button-1>', lambda event: self.destroy(),
                                add='+')

class SearchBetween(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title('Поиск между значениями')
        self.geometry('300x100')
        self.resizable(False, False)

        label1_search = tk.Label(self, text='От:')
        label1_search.place(relx=0.1, rely=0.15)

        label2_search = tk.Label(self, text='До:')
        label2_search.place(relx=0.5, rely=0.15)

        self.first_value = ttk.Entry(self)
        self.first_value.place(relx=0.1, rely=0.45)

        self.second_value = ttk.Entry(self)
        self.second_value.place(relx=0.5, rely=0.45)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(relx=0.5, rely=0.7)

        btn_search = ttk.Button(self, text='Поиск')
        btn_search.place(relx=0.1, rely=0.7)

        btn_search.bind('<Button-1>', lambda event: self.view.search_between(
            self.first_value.get(), self.second_value.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

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
    
    def insert_data(self, lastName, Name, middleName, both, city, serialNumber,
                    dateReg, placeIssue, divisionCode, agresReg, SNILS, tax,
                    birthCertificat, issueCertificate, LNMFather, LNMMather,
                    LinkPhoto):
        self.c.execute(
            '''INSERT INTO DataBase( lastName, Name, middleName, both, city, 
            serialNumber, dateReg, placeIssue, divisionCode, agresReg, SNILS, 
            tax, birthCertificat, issueCertificate, LNMFather, LNMMather, 
            LinkPhoto ) VALUES (?, ?, ?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?,?)''',
            (
                lastName, Name, middleName, both, city, serialNumber, dateReg,
                placeIssue, divisionCode, agresReg, SNILS, tax,
                birthCertificat, issueCertificate, LNMFather, LNMMather,
                LinkPhoto))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("DocScan")
    root.geometry("1280x720")
    root.resizable(True, True)
    root.mainloop()
