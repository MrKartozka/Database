from tkinter import *
from tkinter import messagebox
import sqlite3

f = ('Times', 14)

con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    имя text, 
                    email text, 
                    контакт number, 
                    пол text, 
                    страна text,
                    пароль text
                )
            ''')
con.commit()

ws = Tk()
ws.title('Регистрация/вход пользователя')
ws.geometry('1000x520')
ws.config(bg='#0BBB81')


def insert_record():
    check_counter = 0
    warn = ""
    if register_name.get() == "":
        warn = "Имя не может быть пустым"
    else:
        check_counter += 1

    if register_email.get() == "":
        warn = "Email не может быть пустым"
    else:
        check_counter += 1

    if register_mobile.get() == "":
        warn = "Контакт не может пустым"
    else:
        check_counter += 1

    if var.get() == "":
        warn = "Укажите пол"
    else:
        check_counter += 1

    if variable.get() == "":
        warn = "Укажите страну"
    else:
        check_counter += 1

    if register_pwd.get() == "":
        warn = "Пароль не может быть пустым"
    else:
        check_counter += 1

    if pwd_again.get() == "":
        warn = "Повторный пароль не может быть пустым"
    else:
        check_counter += 1

    if register_pwd.get() != pwd_again.get():
        warn = "Пароли не совпадают!"
    else:
        check_counter += 1

    if check_counter == 8:
        try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES (:имя, :email, :контакт, :пол, :страна, :пароль)", {
                'имя': register_name.get(),
                'email': register_email.get(),
                'контакт': register_mobile.get(),
                'пол': var.get(),
                'страна': variable.get(),
                'пароль': register_pwd.get()

            })
            con.commit()
            messagebox.showinfo('Статус', 'Данные сохранены')

        except Exception as ep:
            messagebox.showerror('', ep)
    else:
        messagebox.showerror('Ошибка', warn)


def login_response():
    try:
        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        for row in c.execute("Select * from record"):
            username = row[1]
            pwd = row[5]

    except Exception as ep:
        messagebox.showerror('', ep)

    uname = email_tf.get()
    upwd = pwd_tf.get()
    check_counter = 0
    if uname == "":
        warn = "Имя не может быть пустым"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Пароль не может быть пустым"
    else:
        check_counter += 1
    if check_counter == 2:
        if (uname == username and upwd == pwd):
            messagebox.showinfo('Статус входа', 'Вы вошли в систему')

        else:
            messagebox.showerror('Статус входа', 'Неправильное имя или пароль')
    else:
        messagebox.showerror('', warn)


var = StringVar()
var.set('male')

countries = []
variable = StringVar()
world = open('countries.txt', 'r')
for country in world:
    country = country.rstrip('\n')
    countries.append(country)
variable.set(countries[19])

left_frame = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)

Label(
    left_frame,
    text="Введите email",
    bg='#CCCCCC',
    font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(
    left_frame,
    text="Введите пароль",
    bg='#CCCCCC',
    font=f
).grid(row=1, column=0, pady=10)

email_tf = Entry(
    left_frame,
    font=f
)
pwd_tf = Entry(
    left_frame,
    font=f,
    show='*'
)
login_btn = Button(
    left_frame,
    width=15,
    text='Логин',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=login_response
)

right_frame = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=10,
    pady=10
)

Label(
    right_frame,
    text="Введите имя",
    bg='#CCCCCC',
    font=f
).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Введите email",
    bg='#CCCCCC',
    font=f
).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Контактный номер",
    bg='#CCCCCC',
    font=f
).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Выберите пол",
    bg='#CCCCCC',
    font=f
).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Выберите страну",
    bg='#CCCCCC',
    font=f
).grid(row=4, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Введите пароль",
    bg='#CCCCCC',
    font=f
).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame,
    text="Введите повторно пароль",
    bg='#CCCCCC',
    font=f
).grid(row=6, column=0, sticky=W, pady=10)

gender_frame = LabelFrame(
    right_frame,
    bg='#CCCCCC',
    padx=10,
    pady=10,
)

register_name = Entry(
    right_frame,
    font=f
)

register_email = Entry(
    right_frame,
    font=f
)

register_mobile = Entry(
    right_frame,
    font=f
)

male_rb = Radiobutton(
    gender_frame,
    text='Муж.',
    bg='#CCCCCC',
    variable=var,
    value='male',
    font=('Times', 10),

)

female_rb = Radiobutton(
    gender_frame,
    text='Жен.',
    bg='#CCCCCC',
    variable=var,
    value='female',
    font=('Times', 10),

)

register_country = OptionMenu(
    right_frame,
    variable,
    *countries)

register_country.config(
    width=15,
    font=('Times', 12)
)
register_pwd = Entry(
    right_frame,
    font=f,
    show='*'
)
pwd_again = Entry(
    right_frame,
    font=f,
    show='*'
)

register_btn = Button(
    right_frame,
    width=15,
    text='Регистрация',
    font=f,
    relief=SOLID,
    cursor='hand2',
    command=insert_record
)

email_tf.grid(row=0, column=1, pady=10, padx=20)
pwd_tf.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
left_frame.place(x=50, y=50)

register_name.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20)
register_mobile.grid(row=2, column=1, pady=10, padx=20)
register_country.grid(row=4, column=1, pady=10, padx=20)
register_pwd.grid(row=5, column=1, pady=10, padx=20)
pwd_again.grid(row=6, column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.place(x=500, y=50)

gender_frame.grid(row=3, column=1, pady=10, padx=20)
male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)

ws.mainloop()