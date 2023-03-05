from tkinter import *
def processOK():
    print("OK button is clicked")
def processCancel():
    print("Cancel button is clicked")
def main():
    tk=Tk()
    btnok=Button(tk,text="OK",fg="red",command=processOK)
    btncancel=Button(tk,text="Cancel",bg="yellow",command=processCancel)
    btnok.pack()
    btncancel.pack()
    tk.mainloop()
if __name__ == '__main__':
    main()