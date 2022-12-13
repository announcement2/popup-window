from tkinter import Tk, Label, Button
import announcement_client
import time

class TkPopup:
    def __init__(self):
        self.queue = []
    def window_queue(self):
        while True:
            for window in self.queue:
                root = Tk()
                root.resizable(width=0, height=0)
                root.title('New Announcement')
                root.geometry('800x600')
                name = Label(root, text='New Announcement from {}\n{}'.format(window[0], window[1]))
                name.pack(pady=1)
                root.mainloop()
                self.queue.pop(0)
            time.sleep(1)

tk = TkPopup()

@announcement_client.announcement_callback
def callback(message, name):
    tk.queue.append([name, message])

announcement_client.run_client('Lukes Desktop')
tk.window_queue()
