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

    nome_app = entry.get()
    validacao = src.search_app(nome_aplicativo=nome_app)

    if validacao:
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
    else:
        label = Label(master, text="Aplicativo não encontrado", bg=coll)
        label.place(x=764, y=125)
        time.sleep(2)
        label.destroy()

def display_apps():
    text_display.delete(1.0, END)
    aplicativos = src.list_apps()
    text_display.tag_configure("font_size", font=("Arial", 18))

    for aplicativo in aplicativos:
        text_display.insert(END, f"\t\tNome: {aplicativo['nome_aplicativo']}\n", "font_size")
        text_display.insert(END, f"\t\tSenha: {aplicativo['senha']}\n", "font_size")
        text_display.insert(END, "\n", "font_size")


def app_info():
    nome_aplicativo = entry.get()
    aplicativo = src.search_app(nome_aplicativo)

    if aplicativo:
        text_display.delete(1.0, END)
        text_display.insert(END, f"Nome: {aplicativo['nome_aplicativo']}\n")
        text_display.insert(END, f"Senha: {aplicativo['senha']}\n")
    elif not aplicativo:
        text_display.delete(1.0, END)
        text_display.insert(END, "Aplicativo não encontrado.")

def deleteup():
    nome_aplicativo = entry.get()
    src.delete_app(nome_aplicativo=nome_aplicativo)
    time.sleep(1)
    display_apps()

master = Tk()
master.title("Gerenciador de Senha")
master.geometry("1440x1024")

background = PhotoImage(file="Imagens//background.png")
search = PhotoImage(file="Imagens//search.png")
append = PhotoImage(file="Imagens//add.png")
delete = PhotoImage(file="Imagens//delete.png")
update = PhotoImage(file="Imagens//refresh.png")
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

search_button = Button(master, bd=0, image=search, command=app_info)
append_button = Button(master, bd=0, image=append, command=create_app)
delete_button = Button(master, bd=0, image=delete, command=deleteup)
update_button = Button(master, bd=0, image=update, command=update_app)

search_button.place(x=740, y=14, width=80, height=80)
append_button.place(x=840, y=14, width=80, height=80)
delete_button.place(x=940, y=14, width=80, height=80)
update_button.place(x=1040, y=14, width=80, height=80)

master.mainloop()
