import hashlib
from tkinter import Tk, Label, Button, filedialog, Entry

def hash_file(file_path):
    h = hashlib.sha1()
    with open(file_path, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()

def browse_file(entry):
    file_path = filedialog.askopenfilename()
    entry.delete(0, 'end')
    entry.insert(0, file_path)

def check_files():
    file_path1 = entry1.get()
    file_path2 = entry2.get()

    if file_path1 and file_path2:
        hash1 = hash_file(file_path1)
        hash2 = hash_file(file_path2)

        if hash1 != hash2:
            result_label.config(text="These files are not identical")
        else:
            result_label.config(text="These files are identical")
    else:
        result_label.config(text="Please select both files")

root = Tk()
root.title("Files Similarity Checker")

label1 = Label(root, text="Select File 1:")
label1.grid(row=0, column=0, padx=5, pady=5)

entry1 = Entry(root, width=50)
entry1.grid(row=0, column=1, padx=5, pady=5)

browse_button1 = Button(root, text="Browse", command=lambda: browse_file(entry1))
browse_button1.grid(row=0, column=2, padx=5, pady=5)

label2 = Label(root, text="Select File 2:")
label2.grid(row=1, column=0, padx=5, pady=5)

entry2 = Entry(root, width=50)
entry2.grid(row=1, column=1, padx=5, pady=5)

browse_button2 = Button(root, text="Browse", command=lambda: browse_file(entry2))
browse_button2.grid(row=1, column=2, padx=5, pady=5)

check_button = Button(root, text="Check", command=check_files)
check_button.grid(row=2, column=1, padx=5, pady=5)

result_label = Label(root, text="")
result_label.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()