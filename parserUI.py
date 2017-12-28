import tkFileDialog
from Tkinter import *


class UI():
    def __init__(self, root):
        self.root = root
        self.root.title("Tentative Name")
        self.root.geometry("600x1000+30+30")

        buttonW = 10
        buttonH = 1
        textFont = ('Calibri', 10)

        self.getfile = Frame(self.root, padx=25, pady=5)
        self.getfile.grid(row=0,column=0,sticky='NS')

        self.getfileButton = Button(self.getfile, text="Open File", width=buttonW, height=buttonH)
        self.fileName = Text(self.getfile, font=textFont, width=50, height=1, padx=5, pady=5)
        self.fileName.config(state=DISABLED)

        self.getfileButton.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.fileName.grid(row=0, column=1, padx=5, pady=5, sticky="e")

        """RESULTS"""
        self.result = Frame(self.root,width=10, height=200)
        self.result.grid(row=1, column=0, sticky="we")

        # self.textbox = Text(self.result, width= 100, height=50)
        # self.textbox.grid()

        """Precheck"""
        self.precheck = Frame(self.result)
        self.precheck.grid(row=0, column=0, padx=5, pady=5, sticky="ns")

        """System Feature"""
        self.system_features = Frame(self.result)
        self.system_features.grid(row=1,column=0,padx=5, pady=5, sticky="nsw")

        """Event"""
        self.event = Frame(self.result)
        self.event.grid(row=2, column=0, padx=5, pady=5, sticky="nsw")

        # self.result_event = Frame(self.result).grid(row=1, column=0, padx=5, pady=5)
        # self.result_systemfeatures = Frame(self.result).grid(row=2, column=0, padx=5, pady=5)
        # self.result_offboard = Frame(self.result).grid(row=3, column=0, padx=5, pady=5)
        #
        #
        # self.resultTextbox = Text(self.result, font=textFont, height=50)
        # self.resultTextbox.config(state=DISABLED)
        # self.resultTextbox.grid()


    def updateEvent(self,result):
        r = 0
        for key, value in result:
            Label(self.event, text=key).grid(row=r, column=0, padx=5, pady=1, sticky="w")
            if value == "True":
                Label(self.event, text=value).grid(row=r, column=1, padx=5, pady=1, sticky="w")
            else:
                Label(self.event, text=value, fg='red').grid(row=r, column=1, padx=5, pady=1, sticky="w")
            r += 1


    def updateSF(self,result):
        r = 0
        for key, value in result:
            Label(self.system_features, text=key).grid(row=r, column=0, padx=5, pady=1, sticky="w")
            if value == "True":
                Label(self.system_features, text=value).grid(row=r, column=1, padx=5, pady=1, sticky="w")
            else:
                Label(self.system_features, text=value,fg='red').grid(row=r, column=1, padx=5, pady=1, sticky="w")
            r += 1

    def updateprecheck(self,result):
        # Take a list of <identifier,var> and and to the precheck accordingly
        r = 0
        for key,value in result:
            Label(self.precheck, text=key).grid(row=r,column=0,padx=5, pady=1,sticky="w")
            Label(self.precheck, text=value).grid(row=r,column=1,padx=5, pady=1, sticky="w")
            r += 1

    def cleartextbox(self):
        self.resultTextbox.config(state=NORMAL)
        self.resultTextbox.delete(1.0, END)
        self.resultTextbox.config(state=DISABLED)


    def uploadfilename(self, my_file):
        self.fileName.config(state=NORMAL)
        self.fileName.delete(1.0,END)
        self.fileName.insert(END, my_file)
        self.fileName.see(END)
        self.fileName.config(state=DISABLED)


    def uploadstring(self, mystring):
        self.resultTextbox.config(state=NORMAL)
        self.resultTextbox.insert(END, mystring + '\n')
        self.resultTextbox.see(END)
        self.resultTextbox.config(state=DISABLED)
