import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
import os

root = ttk.Window(themename='vapor')
root.title('notepad')
base_dir = os.path.dirname(__file__)
image_path = os.path.join(base_dir, "notepad_logo.png")
icon = tk.PhotoImage(file=image_path)
root.iconphoto(True, icon)

try:
    root.wm_attributes("-zoomed", True)
except tk.TclError:
    root.state('zoomed')

def import_file(): 
    file_path = filedialog.askopenfilename(initialdir='/home/', title='pick text file to import',filetypes=(("Text files", "*.txt"),))
    
    if file_path:
        note.delete('1.0','end')
        file = open(file_path, 'r')
        file_data = file.read()
        note.insert(tk.END, file_data)
        file.close()

def saveas_filename():

    def create_file():
        name_window.destroy()
        file_path = filedialog.askdirectory(initialdir='/home/', title='save file to where?')
        

        if file_path:
            file = open(f'{file_path}/{filename.get()}', 'x')
            file.write('')
            file.close
    
    name_window = tk.Toplevel(root)
    name_window.title('file name')
    name_window.geometry('300x300')

    filename = tk.StringVar()

    filename_input = ttk.Entry(name_window, textvariable=filename)
    filename_select = ttk.Button(name_window, text='select', command=create_file)

    filename_input.pack(pady=5)
    filename_select.pack()

def saveto():
    file_path = filedialog.askopenfilename(initialdir='/home/', title='save file to where?',filetypes=(("Text files", "*.txt"),))

    if file_path:
        file = open(file_path,'w')
        file.write(note.get('1.0','end'))
        file.close()

root.grid_propagate(False)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

notepad_frame = ttk.Frame(root)

toolbar_frame = ttk.Frame(root)

notepad_frame.grid_rowconfigure(0, weight=1)
notepad_frame.grid_columnconfigure(0, weight=1)

note = ttk.Text(notepad_frame, undo=True)

scroll_bar = ttk.Scrollbar(notepad_frame, command=note.yview)

import_button = ttk.Button(toolbar_frame, text='import', command= import_file)
saveas_button = ttk.Button(toolbar_frame , text= 'save as', command=saveas_filename)
saveto_button = ttk.Button(toolbar_frame, text='save to', command=saveto)


toolbar_frame.grid(row=0, column=0, sticky='ew')
saveas_button.pack(side='left', padx=5)
saveto_button.pack(side='left')
import_button.pack(side='left', padx=5)
notepad_frame.grid(row=1, column=0, sticky= 'nsew')
note.grid(row=0,column=0, sticky='nsew')
scroll_bar.grid(row=0, column=1, sticky='ns')
note['yscrollcommand'] = scroll_bar.set


tk.mainloop()