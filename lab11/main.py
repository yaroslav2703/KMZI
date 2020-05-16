from tkinter import *
import hashlib
from datetime import datetime


def todo_hash():
    text = str(message.get()).encode('utf-8')
    start_time = datetime.now()
    sha = hashlib.sha1(text).hexdigest()
    print('время выполнения хэширования: ' + str(datetime.now() - start_time))
    hash_.set(sha)


if __name__ == '__main__':
    root = Tk()
    root.title("GUI на Python")
    root.geometry("500x200+300+200")

    message = StringVar()
    hash_ = StringVar()

    message_label = Label(text="Введите исходное сообщение:")
    hash_label = Label(text="Хэш:")

    message_label.grid(row=0, column=0, sticky="w")
    hash_label.grid(row=1, column=0, sticky="w")

    message_entry = Entry(textvariable=message)
    hash_label_executed = Label(textvariable=hash_)

    message_entry.grid(row=0, column=1, padx=5, pady=5)
    hash_label_executed.grid(row=1, column=1, padx=5, pady=5)

    message_button = Button(text="захэшировать", command=todo_hash)
    message_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

    root.mainloop()
