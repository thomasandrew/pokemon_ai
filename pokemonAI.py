from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

root = Tk()

root.geometry('400x500')
root.title('Pokemon AI')
#root['bg'] = 'red'
root.maxsize=400
root.minsize=500
root.resizable(False, False)

def btnWork():

    df = pd.read_csv('pokemon.csv')
    print(df.head())

    print(df.isna().any())

    df_new = df.drop(columns='Type 2')

    print(df_new.columns)

    print(df_new.isna().any())

    print(df_new.info())

    print(df_new.head())

    attributes = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
    X = df_new[attributes]

    classes = ['Type 1']
    y = df_new[classes]

    print(X)
    print(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.20 ,random_state= 42)

    print(X_train.shape, y_train.shape)
    print(X_test.shape, y_test.shape)

    model = GaussianNB()
    model.fit(X_train, y_train.values.ravel())
    print(model)

    pred = model.predict(X_test)
    print(pred)

    print(y_test)

    print(accuracy_score(y_test, pred))

    print(classification_report(y_test, pred))
    try: 
        new_pokemon = pd.DataFrame([{
            'HP': int(hpEntry.get()),
            'Attack': int(attackEntry.get()),
            'Defense': int(defenseEntry.get()),
            'Sp. Atk': int(spAtkEntry.get()),
            'Sp. Def': int(spDefEntry.get()),
            'Speed': int(speedEntry.get())
        }])

        prediction = model.predict(new_pokemon)

        messagebox.showinfo('showinfo', f"Pokemon Type: {prediction[0]}")
    except ValueError:
        messagebox.showerror('Erro', 'Preencha todos os campos vazios')


bg_image = Image.open('pokeimg.png').convert('RGBA')

overlay_color = (0, 51, 102, 128)
overlay = Image.new('RGBA', bg_image.size, overlay_color)

final_image = Image.alpha_composite(bg_image, overlay)

bg = ImageTk.PhotoImage(final_image)

#fundo
canvas = Canvas(root, width=400, height=500, highlightthickness=0)
canvas.place(x=0, y=0)

canvas.create_image(0, 0, image=bg, anchor='nw')

original_img = Image.open('tit.png')

resized_img = original_img.resize((250, 80), Image.Resampling.LANCZOS)

titleImg = ImageTk.PhotoImage(resized_img)

pk_titulo = Label(
    root, 
    image=titleImg,  
    bg='gray',
    fg='#fff',
    font='Arial 15 bold',
    relief='raised',
    padx='40',
    pady='30',
    width=250,
    height=80
)
pk_titulo.pack(pady=(10, 20))

hpTxt = canvas.create_text(
    110, 130,
    text='HP: ', 
    fill='#fff',
    font='Arial 15 bold',
    anchor='e'
)

hpEntry = Entry(
    root, 
    width=18, 
    font='Arial 15',
)

canvas.create_window(130, 130, window=hpEntry, anchor='w')

attackTxt = canvas.create_text(
    110,185,
    text='Attack: ',
    fill='#fff',
    font='Arial 15 bold',
    anchor='e'
)

attackEntry = Entry(
    root,
    width=18,
    font='Arial 15'
)

canvas.create_window(130, 185, window=attackEntry, anchor='w')

defenseTxt = canvas.create_text(
    115,240,
    text='Defense: ',
    fill='#fff',
    font='Arial 15 bold',
    anchor='e'
)

defenseEntry = Entry(
    root,
    width=18,
    font='Arial 15'
)

canvas.create_window(130, 240, window=defenseEntry, anchor='w')

spAtkTxt = canvas.create_text(
    115,290,
    text='Sp. Atk: ',
    fill='#fff',
    font='Arial 15 bold',
    anchor='e'
)

spAtkEntry = Entry(
    root,
    width=18,
    font='Arial 15'
)

canvas.create_window(130, 290, window=spAtkEntry, anchor='w')

spDefTxt = canvas.create_text(
    115,340,
    text='Sp. Def: ',
    fill='#fff',
    font='Arial 15 bold',
    anchor='e'
)

spDefEntry = Entry(
    root,
    width=18,
    font='Arial 15'
)

canvas.create_window(130, 340, window=spDefEntry, anchor='w')

speedTxt = canvas.create_text(
    115,390,
    text='Speed: ',
    fill='#fff',
    font='Arial 15 bold',
    anchor='e'
)

speedEntry = Entry(
    root,
    width=18,
    font='Arial 15'
)

canvas.create_window(130, 390, window=speedEntry, anchor='w')

pressBtn = Button(
    root,
    text='Clique Aqui',
    fg='#000',
    width=20,
    font='Arial 11 bold',
    command=btnWork
)

pressBtn.pack(
    pady=25, 
    side='bottom'
)

root.mainloop()