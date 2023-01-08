import tkinter
from tkinter import ttk, filedialog, messagebox
from tkinter import *
from PIL import Image, ImageTk
from steganocryptopy.steganography import Steganography
import time
# from translit import GetReady, Fix
from test_ready1 import GetReady, Fix
from tkinterdnd2 import TkinterDnD, DND_FILES






def change_for_predpokaz(width, height):
    coordinates = [0, 0]
    box_width = 400
    box_height = 400

    while ((height > box_height) or (width > box_width)):

        if (width > box_width):
            width = width / 2
            height = height / 2

        elif (width < box_width):
            width = width + 50
            height = height + 50

        elif (height > box_height):
            width = width / 2
            height = height / 2

        elif (height < box_height):
            width = width + 50
            height = height + 50

    width = int(round(width))
    height = int(round(height))
    coordinates[0] = width
    coordinates[1] = height
    return coordinates

def ConvertToCode(personal_password): #удлинняет пароль, если он меньше 44 символов

    while len(personal_password) != 43: #берем 43,а не 44 потому что потом еще вконце добавим =
        personal_password = personal_password + "0"
    personal_password = personal_password +"="
    return personal_password

def ValidEntry():
    text = input_your_key_entry.get()
    if len(text) ==44:
        print(len(text))
        print("Все нормально по длине")
        return True
    elif (len(text)<44) & (text[-1] != "="):
        print("Длина меньше 44, но это мы сейчас изменим")
        return True
    elif text[-1] == "=":
        print("Ошибка, текст меньше 44 символов и в конце знак равно")
        return False
    else:
        print("Длина: "+ str(len(text)))
        print("Что-то не так, возможно длина меньше 44 ")
        return False


def openFile(file_):
    if (file_ != None):
        filepath = file_
        print(file_)
        im = Image.open(filepath)
        # im_orig = Image.open(filepath, mode='r')
        # print(im_orig.show())
        im.save('img/original.png')

        # img_pokaz = img_pokaz.resize(img_width / 2, img_height / 2)

        img_for_pokaz = Image.open(
            'img/original.png')  # создаем картинку которую потом будем вставлять в окно предпоказа

        width = img_for_pokaz.width
        height = img_for_pokaz.height

        coord = [0, 0]
        coord = change_for_predpokaz(width, height)

        width = coord[0]
        height = coord[1]

        # width = round(img_for_pokaz.width/2)
        # height = round(img_for_pokaz.height/2)

        rez = img_for_pokaz.resize((width, height))
        rez.save('img/for_pokaz.png')
        rez.close()
        img_for_pokaz.close()

        # img_width = img_pokaz.width()
        # img_height = img_pokaz.height()
        #
        # print(img_width)
        # print(img_height)
        #

        img_pokaz = ImageTk.PhotoImage(Image.open('img/for_pokaz.png'))

        # lb2_tab1.configure(image=img_pokaz)
        # lb2_tab1.image=img_pokaz

        predpokaz_tab1.configure(image=img_pokaz)
        predpokaz_tab1.image = img_pokaz

        print('App get the image and save')

        im.close()

        button1_tab1.config(state=ACTIVE)
        # активируем кнопку для зашифровки текста после того, как выберем картинку в которую будем зашифровывать

        # print(file.read())
        # file.close()

    else:
        filepath = filedialog.askopenfilename(
                                              title="Choose original image",
                                              filetypes=(("JPG", "*.JPG"),
                                                         ("all files", "*.*"))
                                              )
        # file = open(filepath, 'r')
        im = Image.open(filepath)
        # im_orig = Image.open(filepath, mode='r')
        # print(im_orig.show())
        im.save('img/original.png')

        # img_pokaz = img_pokaz.resize(img_width / 2, img_height / 2)

        img_for_pokaz = Image.open('img/original.png')  # создаем картинку которую потом будем вставлять в окно предпоказа

        width = img_for_pokaz.width
        height = img_for_pokaz.height

        coord = [0, 0]
        coord = change_for_predpokaz(width, height)

        width = coord[0]
        height = coord[1]

        # width = round(img_for_pokaz.width/2)
        # height = round(img_for_pokaz.height/2)

        rez = img_for_pokaz.resize((width, height))
        rez.save('img/for_pokaz.png')
        rez.close()
        img_for_pokaz.close()

        # img_width = img_pokaz.width()
        # img_height = img_pokaz.height()
        #
        # print(img_width)
        # print(img_height)
        #

        img_pokaz = ImageTk.PhotoImage(Image.open('img/for_pokaz.png'))

        # lb2_tab1.configure(image=img_pokaz)
        # lb2_tab1.image=img_pokaz

        predpokaz_tab1.configure(image=img_pokaz)
        predpokaz_tab1.image = img_pokaz

        print('App get the image and save')

        im.close()

        button1_tab1.config(state=ACTIVE)
        # активируем кнопку для зашифровки текста после того, как выберем картинку в которую будем зашифровывать

        # print(file.read())
        # file.close()


def openPhotoWithSecret(file_):
    if (file_ != None):
        filepath = file_
        print(file_)

        # file = open(filepath, 'r')
        im = Image.open(filepath)
        # im_orig = Image.open(filepath, mode='r')
        # print(im_orig.show())
        im.save('img/secret_to_decode.png')

        # img_pokaz = img_pokaz.resize(img_width / 2, img_height / 2)

        img_for_pokaz_tab2 = Image.open(
            'img/secret_to_decode.png')  # создаем картинку которую потом будем вставлять в окно предпоказа

        width = img_for_pokaz_tab2.width
        height = img_for_pokaz_tab2.height

        coord = [0, 0]
        coord = change_for_predpokaz(width, height)

        width = coord[0]
        height = coord[1]

        # width = round(img_for_pokaz.width/2)
        # height = round(img_for_pokaz.height/2)

        rez = img_for_pokaz_tab2.resize((width, height))
        rez.save('img/for_pokaz_tab2.png')
        rez.close()
        img_for_pokaz_tab2.close()

        # img_width = img_pokaz.width()
        # img_height = img_pokaz.height()
        #
        # print(img_width)
        # print(img_height)
        #

        img_pokaz = ImageTk.PhotoImage(Image.open('img/for_pokaz_tab2.png'))

        # lb2_tab1.configure(image=img_pokaz)
        # lb2_tab1.image=img_pokaz

        predpokaz_tab2.configure(image=img_pokaz)
        predpokaz_tab2.image = img_pokaz

        print('App get the image with secret and save')

        im.close()

        button1_tab2.config(state=ACTIVE)

    else:
        filepath = filedialog.askopenfilename(
            title="Choose original image",
            filetypes=(("PNG", "*.png"),
                       ("all files", "*.*"))
        )

        # file = open(filepath, 'r')
        im = Image.open(filepath)
        # im_orig = Image.open(filepath, mode='r')
        # print(im_orig.show())
        im.save('img/secret_to_decode.png')

        # img_pokaz = img_pokaz.resize(img_width / 2, img_height / 2)

        img_for_pokaz_tab2 = Image.open(
            'img/secret_to_decode.png')  # создаем картинку которую потом будем вставлять в окно предпоказа

        width = img_for_pokaz_tab2.width
        height = img_for_pokaz_tab2.height

        coord = [0, 0]
        coord = change_for_predpokaz(width, height)

        width = coord[0]
        height = coord[1]

        # width = round(img_for_pokaz.width/2)
        # height = round(img_for_pokaz.height/2)

        rez = img_for_pokaz_tab2.resize((width, height))
        rez.save('img/for_pokaz_tab2.png')
        rez.close()
        img_for_pokaz_tab2.close()

        # img_width = img_pokaz.width()
        # img_height = img_pokaz.height()
        #
        # print(img_width)
        # print(img_height)
        #

        img_pokaz = ImageTk.PhotoImage(Image.open('img/for_pokaz_tab2.png'))

        # lb2_tab1.configure(image=img_pokaz)
        # lb2_tab1.image=img_pokaz

        predpokaz_tab2.configure(image=img_pokaz)
        predpokaz_tab2.image = img_pokaz

        print('App get the image with secret and save')

        im.close()

        button1_tab2.config(state=ACTIVE)









def decode_Secret():
    ResultArea.delete("1.0", END)
    key_for_decode = str(key_entry.get())
    message = open('text/key_for_decode.key', 'w', encoding='UTF-8')
    message = message.write(key_for_decode)

    before_translit = Steganography.decrypt("text/key_for_decode.key", "img/secret_to_decode.png")

    print("Result: " + before_translit)

    print("On Rus: ")
    # text_ru = translit(english, language_code='rus')
    text = Fix(before_translit)
    print(text)

    # result = "Текст кириллицей:\n"+ text_ru + "\nText on Eng:\n"+ english

    ResultArea.insert("1.0",text)




def createSecret():
#надо сделать так, чтобы если галочка нажата и текст в поле для ввода собственного пароля проходит проверку,
# то пароль НЕ генерировать, а брать с окна для ввода, в ином случае (если галочка не нажата, то генерировать пароль)
    if x.get():
        if ValidEntry():
            print("Ты молодец")
            your_personal_password = str(input_your_key_entry.get())
            print(your_personal_password)
            if (len(your_personal_password)<44) & (your_personal_password[-1] != "="):
                your_personal_password = ConvertToCode(your_personal_password)
                print("После применения функции удлиннения пароля мы получили:")
                print(your_personal_password)


            personal_password = open('text/personal.key', 'w', encoding='UTF-8')
            personal_password = personal_password.write(your_personal_password)

            text_secret = textArea.get("1.0", END)

            text = GetReady(text_secret)

            message = open('text/message.txt', 'w', encoding='UTF-8')
            message = message.write(text)
            print(text_secret)
            print(text)

            secret = Steganography.encrypt("text/personal.key", "img/original.png", "text/message.txt")
            secret.save("img/secret.png")
            # secret.close()

            file = filedialog.asksaveasfile(mode='w', defaultextension=".png")

            print(file.name)

            secret.save(file.name)
            secret.close()

            key = open('text/personal.key', 'r', encoding='UTF-8')
            key_read = key.read()
            print(key_read)

            get_key_entry.delete(0, END)
            get_key_entry.insert(0, key_read)
            key.close()

        elif not ValidEntry():
            text_fromArea = textArea.get("1.0",END)
            # textArea.delete("1.0", END)
            # textArea.insert(float(len(text_fromArea)), "\nError01")
            messagebox.showerror(title='Ошибка!',
                                 message='ERROR_01\nВозможное возникновение ошибки -'
                                         '\nВы ввели персональный пароль, что по длинне меньше 44 символов'
                                         ' и в конце стоит знак равно. '
                                         'Попробуйте ввести еще раз пароль, но без знака равно в конце')
            #Error01 - ошибка по полю, где пользователь вводит свой кастомный пароль. Возможное возникновение ошибки -
            # если человек ввел пароль меньше 44 символов и в конце знак = стоит

            # textArea.delete("1.0", END)
            # textArea.insert("1.0",text_fromArea)
            input_your_key_entry.delete(0,END)



    # elif x.get() & (ValidEntry()):
    #     print("Ты молодец")

    elif (not x.get()):

        Steganography.generate_key("text/key.key")  # 43 symbols + "="

        # secret = open('text.txt', 'r', encoding='UTF-8')
        text_secret = textArea.get("1.0", END)

        # text = translit(text_secret, language_code='rus', reversed=True)
        text = GetReady(text_secret)

        message = open('text/message.txt', 'w', encoding='UTF-8')
        message = message.write(text)
        print(text_secret)
        print(text)

        secret = Steganography.encrypt("text/key.key", "img/original.png", "text/message.txt")
        secret.save("img/secret.png")
        # secret.close()

        file = filedialog.asksaveasfile(mode='w', defaultextension=".png")

        print(file.name)

        secret.save(file.name)
        secret.close()

        key = open('text/key.key', 'r', encoding='UTF-8')
        key_read = key.read()
        print(key_read)

        get_key_entry.delete(0,END)
        get_key_entry.insert(0, key_read)
        key.close()

def InputYourOwnPassword():
    if (x.get()):
       input_your_key_entry.config(state=NORMAL)
    else:
        input_your_key_entry.config(state=DISABLED)

def AboutApp():
    print("About program ")
    about_window = Toplevel()
    about_window.geometry("400x300")
    about_window.title("About app")

    title = Label(about_window,text="MyApp")
# Stegamage? Stemage? Stegic?
    title.pack()

def drop_to_encrypt(event):

    jpg = '.jpg'
    JPG = '.JPG'
    png = '.png'
    PNG = '.PNG'


    entry_file.set(event.data)
    data = event.data

    data = data.replace('{','')
    data = data.replace('}','')
    # data = data[1:] #обрезаем { и }
    # data = data[:-1]
    print(data)

    if jpg in data:
        print("Cool, it's jpg))")
        openFile(data)
    elif JPG in data:
        print("Cool, it's JPG))")
        openFile(data)
    # elif png in data:
    #     print("Cool, it's png))")
    #     openFile(data)
    # elif PNG in data:
    #     print("Cool, it's PNG))")
    #     openFile(data)

    else:
        print("Unknown type of file")
        # openFile(data)

def drop_to_decrypt(event):

    png = '.png'
    PNG = '.PNG'


    entry_file_to_decrypt.set(event.data)
    data = event.data

    data = data.replace('{','')
    data = data.replace('}','')
    # data = data[1:] #обрезаем { и }
    # data = data[:-1]
    print(data)

    if png in data:
        print("Cool, it's png ))")
        openPhotoWithSecret(data)
    elif PNG in data:
        print("Cool, it's PNG ))")
        openPhotoWithSecret(data)

    # elif png in data:
    #     print("Cool, it's png))")
    #     openFile(data)
    # elif PNG in data:
    #     print("Cool, it's PNG))")
    #     openFile(data)

    else:
        print("Unknown type of file")
        # openFile(data)

window = TkinterDnD.Tk()
window.title("Stegic")

menubar = Menu(window)
window.config(menu= menubar)

programMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Program", menu = programMenu)
programMenu.add_cascade(label="About App", command=AboutApp)



notebook = ttk.Notebook(window, )  # widget that manages a collection of window/displays

tab1 = Frame(notebook)  # new frame for tab 1
tab2 = Frame(notebook)  # new frame for tab 2

notebook.add(tab1, text="Tab 1, зашифровка")
notebook.add(tab2, text="Tab 2, декодирование ")
notebook.pack(expand=True, fill="both")  # expand = expand to fill any space not otherwise used
# fill = fill space on X and y axis

original_photo = PhotoImage(file='img/Skype100.png',
                            height=100,
                            width=100,
                            )
# frame_left = Frame(tab1)
# frame_left.grid(row=0,column=0)

lb1_tab1 = Label(tab1, text="Insert your original image: ", height=3, width=20)
lb1_tab1.grid(row=0,column=0)

entry_file = tkinter.StringVar()

# drag_and_drop = tkinter.Entry(frame_left, textvariable=entry_file,width=50 )
# drag_and_drop.pack(fill=tkinter.X)
#
# drag_and_drop.drop_target_register(DND_FILES)
# drag_and_drop.dnd_bind('<<Drop>>', drop)

# lb1_tab1 = Label(tab1, text="Insert your original image: ", height=3, width=20).grid(row=0, column=0)

choose_im_tab1 = Button(tab1, text="Choose an image", height=3, width=20, command=openFile).grid(row=1, column=0)

# Сделать так, чтобы после выбора изображения, оно отображалось в окошке

predpokaz_tab1 = Label(tab1, image=original_photo, height=400, width=400,textvariable=entry_file)
predpokaz_tab1.grid(row=2, column=0)
predpokaz_tab1.drop_target_register(DND_FILES)
predpokaz_tab1.dnd_bind('<<Drop>>', drop_to_encrypt)


#### button_tab1 = Button(tab1, text="Under",height=3,width=20).grid(row=1,column=0)

textArea = Text(tab1, height=10, width=30, font=("Arial", 15))
textArea.grid(row=0, column=1)


frame = Frame(tab1)
frame.grid(row=1,column=1)

# button1_tab1.grid(row=1, column=1)

x = BooleanVar()



check_button = Checkbutton(frame,
                          text="Я хочу ввести свой пароль",
                          variable=x,
                          onvalue=True,
                          offvalue=False,
                           command=InputYourOwnPassword,
                        font=("Arial",15))
check_button.pack()
# check_button.grid(row=2,column=1)
input_your_key_entry = Entry(frame, width=50, font=("Arial", 15),state=DISABLED)
input_your_key_entry.pack()

button1_tab1 = Button(frame, text="Create secret image", height=3, width=20, command=createSecret, state=DISABLED)
button1_tab1.pack()

# get_key_entry = Entry(tab1, width=50, font=("Arial", 15))
# get_key_entry.grid(row=3, column=1)

get_key_entry = Entry(tab1, width=50, font=("Arial", 15))
get_key_entry.grid(row=2, column=1)



# save_button = Button(tab1,text="Save as",height=3,width=20, command=saveSecret)
# save_button.grid(row=2, column = 1)


######################################################################## TAB 2

entry_file_to_decrypt = tkinter.StringVar()

original_photo_decode = PhotoImage(file='img/Skype100.png',
                                   height=100,
                                   width=100,
                                   )

lb1_tab2 = Label(tab2, text="Insert image to decode: ", height=3, width=20).grid(row=0, column=0)
choose_im_tab2 = Button(tab2, text="Choose an image", height=3, width=20, command=openPhotoWithSecret).grid(row=1,
                                                                                                            column=0)

predpokaz_tab2 = Label(tab2, image=original_photo_decode, height=400, width=400,textvariable=entry_file_to_decrypt)
predpokaz_tab2.grid(row=2, column=0)
predpokaz_tab2.drop_target_register(DND_FILES)
predpokaz_tab2.dnd_bind('<<Drop>>', drop_to_decrypt)
#### button_tab1 = Button(tab1, text="Under",height=3,width=20).grid(row=1,column=0)


key_entry = Entry(tab2, width=50, font=("Arial", 15))
key_entry.grid(row=0, column=1)

ResultArea = Text(tab2, height=10, width=30, font=("Arial", 15))
ResultArea.grid(row=2, column=1)

button1_tab2 = Button(tab2, text="Decode the message", height=3, width=20, command=decode_Secret, state=DISABLED)
button1_tab2.grid(row=1, column=1)

# Label(tab2, text="Hello, this is tab #2!!!", width=50, height=25).pack()


window.bind("<Return>", openFile)
window.mainloop()
