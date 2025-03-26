import tkinter as tk
from typing import List

def fazer_janela() -> tk.Tk:
    janela = tk.Tk()
    janela.title('Calculadora')
    janela.config(padx=10, pady=10, background='#002817')
    janela.resizable(False, False)
    return janela

def fazer_label(janela, **grid_options) -> tk.Label:
    label = tk.Label(
        janela, text='Bem-vindo',
        anchor='e', justify='right', background='#026842', font=("Courier", 10, "italic"))
    label.grid(**grid_options)
    return label

def fazer_display(janela, **grid_options) -> tk.Entry:
    display = tk.Entry(janela)
    display.grid(**grid_options)
    display.config(
        font=('Arial', 40, 'bold'),
        justify='right', bd=1, relief='flat',
        highlightthickness=1, highlightcolor='#ccc'
    )
    display.bind('<Control-a>', _display_control_a)
    return display

def _display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'

def fazer_button(janela, text, **grid_options) -> tk.Button:
    btn = tk.Button(janela, text=text)
    btn.grid(**grid_options)
    btn.config(
        font=('courier', 15, 'normal'),
        pady=25, width=12,height=1, background='#026842', bd=0, 
        cursor='hand2', highlightthickness=0,
        highlightcolor='#ccc', activebackground='#ccc',
        highlightbackground='#ccc')
    return btn

def fazer_buttons(janela, starting_row) -> List[List[tk.Button]]:
    button_texts: List[List[str]] = [
        ['(', ')', 'C', '/'],
        ['7', '8', '9', '*'],
        ['4', '5', '6', '-'],
        ['1', '2', '3', '+'],
        ['^', '0', '.', '='],
        
    ]

    buttons: List[List[tk.Button]] = []

    for row, row_value in enumerate(button_texts, start=starting_row):
        button_row = []
        for col_index, col_value in enumerate(row_value):
            btn = fazer_button(
                janela, text=col_value,
                row=row, column=col_index, sticky='news', padx=5, pady=5
            )
            button_row.append(btn)
        buttons.append(button_row)
    return buttons
