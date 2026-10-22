import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

BG_COLOR="black"
FG_COLOR="white"
TITLE_FONT=("arial", 20, "bold")
TEXT_FONT=("arial", 15)

window = tk.Tk()
window.title("Планы")
window.geometry("1400x800")
window.resizable(width=False, height=False)
window["bg"] = BG_COLOR



notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)



tab_add = tk.Frame(notebook, bg=BG_COLOR)
notebook.add(tab_add, text="Добавить идею")



tab_plans = tk.Frame(notebook,bg=BG_COLOR)
notebook.add(tab_plans, text="Мои планы")



plans = []



lbl_name = tk.Label(tab_add, text="Название", font=TITLE_FONT,
                    fg=FG_COLOR, bg=BG_COLOR)
lbl_name.place(x=550, y=25)

EnterName = tk.Entry(tab_add, fg=FG_COLOR, width=47, font=TEXT_FONT,insertbackground="white",bg="grey20")
EnterName.place(x=550, y=75)

lbl_idea = tk.Label(tab_add, text="Добавить идею",font=TITLE_FONT,
                    fg=FG_COLOR, bg=BG_COLOR)
lbl_idea.place(x=550, y=150)

EnterIdea = tk.Entry(tab_add, fg=FG_COLOR, width=47, font=TEXT_FONT, insertbackground="white", bg="grey20")
EnterIdea.place(x=550, y=200)



lbl_plans = tk.Label(tab_plans, text="Мои планы", font=TITLE_FONT,
                     fg=FG_COLOR, bg=BG_COLOR)
lbl_plans.pack(pady=20)

list_frame = tk.Frame(tab_plans,bg=BG_COLOR)
list_frame.pack(fill="both", expand=True, padx=50, pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

plans_listbox = tk.Listbox(list_frame, font=TEXT_FONT,
                           bg="grey20", fg=FG_COLOR,
                           yscrollcommand=scrollbar.set,
                           selectbackground="grey40")
plans_listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=plans_listbox.yview)



def refresh_plans():

    plans_listbox.delete(0, tk.END)
    for i, p in enumerate(plans, start=1):
        plans_listbox.insert(tk.END, f"{i}. {p['idea']}  —  {p['name']}")


def save_data():
    idea_text = EnterIdea.get().strip()
    name_text = EnterName.get().strip()

    if not idea_text or not name_text:
        messagebox.showwarning("Ошибка", "Заполни все поля!")
        return

    plans.append({"idea": idea_text, "name": name_text})
    refresh_plans()

    EnterIdea.delete(0, tk.END)
    EnterName.delete(0, tk.END)

    messagebox.showinfo("Готово", "Идея сохранена!")



btn = tk.Button(tab_add, text="Save", font=TITLE_FONT,
                fg=FG_COLOR, bg="grey20", command=save_data)
btn.place(relx=0.5, rely=0.9, anchor="s")


def clear_all():
    if not plans:
        messagebox.showinfo("Пусто", "Список и так пуст.")
        return
    if messagebox.askyesno("Подтверждение", "Удалить все планы?"):
        plans.clear()
        refresh_plans()


btn_clear = tk.Button(tab_plans, text="Очистить всё", font=TEXT_FONT,
                      fg=FG_COLOR, bg="grey20", command=clear_all)
btn_clear.pack(pady=10)


window.mainloop()