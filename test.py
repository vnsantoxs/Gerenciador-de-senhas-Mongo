from tkinter import *
import src
import time

def on_entry_nome_click(event):
    if entry.get() == 'Nome':
        entry.delete(0, "end")

def on_entry_nome_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Nome')

def create_app():
    def on_entry_nome_click(event):
        if entry.get() == 'Nome':
            entry.delete(0, "end")

    def on_entry_nome_focusout(event):
        if entry.get() == '':
            entry.insert(0, 'Nome')
    def on_entry_password_click(event):
        if password_entry.get() == 'Senha':
            password_entry.delete(0, "end")
            password_entry.config(show="*")

    def on_entry_password_focusout(event):
        if password_entry.get() == '':
            password_entry.config(show="")
            password_entry.insert(0, 'Senha')

    def confirm_create_app():
        nome_aplicativo = entry.get()
        senha = password_entry.get()
        src.create_app(nome_aplicativo, senha)
        time.sleep(1)
        label.destroy()
        confirm_button.destroy()
        entry.destroy()
        password_entry.destroy()
        display_apps()


    fonte = ("Arial", 16)
    label = Label(master, text="Cadastro", bg=coll, bd=4, relief="solid", font=fonte)
    label.place(x=764, y=115)

    entry = Entry(master, bg=coll, bd=2, relief="solid", width=48)
    entry.insert(0, 'Nome')
    entry.bind('<FocusIn>', on_entry_nome_click)
    entry.bind('<FocusOut>', on_entry_nome_focusout)
    entry.place(x=880, y=200, height=50)

    password_entry = Entry(master, bg=coll, bd=2, width=48, show="",relief="solid")
    password_entry.insert(0, 'Senha')
    password_entry.bind('<FocusIn>', on_entry_password_click)
    password_entry.bind('<FocusOut>', on_entry_password_focusout)
    password_entry.place(x=880, y=280, height=50)

    confirm_button = Button(master, text="Confirmar", font=fonte, bd=1, relief="solid", command=confirm_create_app, bg=coll)
    confirm_button.place(x=900, y=360)


def update_app():
    def on_entry_password_click(event):
        if password_entry.get() == 'Senha':
            password_entry.delete(0, "end")
            password_entry.config(show="*")

    def on_entry_password_focusout(event):
        if password_entry.get() == '':
            password_entry.config(show="")
            password_entry.insert(0, 'Senha')

    def confirm_update_app():
        nome_aplicativo = entry.get()
        nova_senha = password_entry.get()
        src.update_app(nome_aplicativo, nova_senha)
        time.sleep(1)
        label.destroy()
        confirm_button.destroy()
        entry.destroy()
        password_entry.destroy()
        display_apps()


    fonte = ("Arial", 16)
    label = Label(master, text="Atualização", bg=coll, bd=4, relief="solid", font=fonte)
    label.place(x=764, y=125)

    password_entry = Entry(master, bg=coll, bd=2, width=48, show="",relief="solid")
    password_entry.insert(0, 'Nova Senha')
    password_entry.bind('<FocusIn>', on_entry_password_click)
    password_entry.bind('<FocusOut>', on_entry_password_focusout)
    password_entry.place(x=880, y=215, height=50)

    confirm_button = Button(master, text="Confirmar", font=fonte, bd=1, relief="solid", command=confirm_update_app, bg=coll)
    confirm_button.place(x=1000, y=300)


def display_apps():
    text_display.delete(1.0, END)
    aplicativos = src.list_apps()
    for aplicativo in aplicativos:
        text_display.insert(END, f"Nome: {aplicativo['nome_aplicativo']}\n")
        text_display.insert(END, f"Senha: {aplicativo['senha']}\n")
        text_display.insert(END, "\n")


def app_info():
    nome_aplicativo = entry.get()
    aplicativo = src.search_app(nome_aplicativo)
    if aplicativo:
        text_display.delete(1.0, END)
        text_display.insert(END, f"Nome: {aplicativo['nome_aplicativo']}\n")
        text_display.insert(END, f"Senha: {aplicativo['senha']}\n")
        time.sleep(2)
        display_apps()
    elif not(aplicativo):
        text_display.delete(1.0, END)
        text_display.insert(END, "Aplicativo não encontrado.")
        display_apps()
        time.sleep(2)



master = Tk()
master.title("Gerenciador de Senha")
master.geometry("1440x1024")

background = PhotoImage(file="Imagens//background.png")
search = PhotoImage(file="Imagens//search.png")
append = PhotoImage(file="Imagens//append.png")
delete = PhotoImage(file="Imagens//delete.png")
update = PhotoImage(file="Imagens//update.png")
positive = PhotoImage(file="Imagens//positive.png")
negative = PhotoImage(file="Imagens//negative.png")
coll = "gray"

label_background = Label(master, image=background)
label_background.pack()

entry = Entry(master, bg=coll, bd=0, width=48)
entry.insert(0, 'Nome')
entry.bind('<FocusIn>', on_entry_nome_click)
entry.bind('<FocusOut>', on_entry_nome_focusout)
entry.place(x=291, y=25, height=50)


text_display = Text(master, bg=coll, bd=0)
text_display.place(x=100, y=160, width=590, height=800)
display_apps()

search_button = Button(master, bd=0, image=search,  command=app_info)
append_button = Button(master, bd=0, image=append, command=create_app)
delete_button = Button(master, bd=0, image=delete, command=lambda: src.delete_app(entry.get()))
update_button = Button(master, bd=0, image=update, command=update_app)

search_button.place(x=747, y=25, width=50, height=50)
append_button.place(x=844, y=18, width=65, height=65)
delete_button.place(x=956, y=25, width=50, height=50)
update_button.place(x=1053, y=25, width=50, height=50)

master.mainloop()