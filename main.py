import tkinter as tk
from tkinter import ttk

def on_button_click(text_entry):
    text = text_entry.get()
    print("Wpisany tekst:", text)

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Nowe Okno")
    label = tk.Label(new_window, text="To jest nowe okno!")
    label.pack(pady=10)

# Tworzymy główne okno aplikacji
root = tk.Tk()
root.title("Proste Okienko tkinter z Navbar i Polem Input")

# Tworzymy pasek nawigacyjny (navbar) jako ttk.Notebook
navbar = ttk.Notebook(root)

# Funkcja pomocnicza do tworzenia kart z polem input i przyciskiem
def create_view_with_input(parent, label_text):
    view = tk.Frame(parent)

    label = tk.Label(view, text=label_text)
    label.pack(pady=10)

    text_entry = tk.Entry(view)
    text_entry.pack(pady=5)

    button = tk.Button(view, text="Wyświetl", command=lambda: on_button_click(text_entry))
    button.pack()

    return view

# Widok 1 z polem input, przyciskiem "Wyświetl" i przyciskiem "Dodaj"
view1 = create_view_with_input(navbar, "To jest widok 1")

# Przycisk "Dodaj" do otwierania nowego okna
add_button = tk.Button(view1, text="Dodaj", command=open_new_window)
add_button.pack(pady=10)

navbar.add(view1, text="Widok 1")

# Widok 2 z polem input, przyciskiem "Wyświetl" i przyciskiem "Dodaj"
view2 = create_view_with_input(navbar, "To jest widok 2")

# Przycisk "Dodaj" do otwierania nowego okna
add_button = tk.Button(view2, text="Dodaj", command=open_new_window)
add_button.pack(pady=10)

navbar.add(view2, text="Widok 2")

# Wyśrodkowanie paska nawigacyjnego i umieszczenie go na górze okna
navbar.pack(fill='both', expand=True)

# Uruchamiamy główną pętlę aplikacji
root.mainloop()
