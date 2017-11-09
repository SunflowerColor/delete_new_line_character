#delete newline
import tkinter
    
def delbutton ():
    str=inputtext.get('0.0','end')
    str2=str.replace('\n',' ')
    outputtext.delete('0.0','end')
    outputtext.insert('0.0',str2)

root=tkinter.Tk()
inputtext=tkinter.Text(root)
inputtext.pack()
outputtext=tkinter.Text(root)
outputtext.pack()
outputbutton=tkinter.Button(root,text="go",command=delbutton)
outputbutton.pack()

root.mainloop()


