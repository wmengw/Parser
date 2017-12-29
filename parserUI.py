import tkFileDialog
from Tkinter import *


class UI():
    def __init__(self, root):
        self.root = root
        self.root.title("Tentative Name")
        self.root.geometry("700x700+30+30")

        buttonW = 10
        buttonH = 1
        textFont = ('Calibri', 10)

        self.getfile = Frame(self.root, padx=25, pady=10)
        self.getfile.grid(row=0, column=0, sticky='nsw')

        self.getfileButton = Button(self.getfile, text="Open File", width=buttonW, height=buttonH)
        self.fileName = Text(self.getfile, font=textFont, width=50, height=1, padx=5, pady=1)
        self.fileName.config(state=DISABLED)

        self.getfileButton.grid(row=0, column=0, padx=5, pady=1, sticky="nsw")
        self.fileName.grid(row=0, column=1, padx=5, pady=1, sticky="nse")

        """RESULTS"""
        self.result = Frame(self.root)
        self.result.grid(row=1, column=0, sticky="we")
        # self.result.pack()

        # self.textbox = Text(self.result, width= 100, height=50)
        # self.textbox.grid()

        """Precheck"""
        self.precheck = Frame(self.result)
        self.precheck.grid(row=0, column=0, padx=5, pady=1, sticky="nswe")

        """"Subresults"""
        self.subresults = Frame(self.result)
        self.subresults.grid(row=1, column=0, sticky="nswe")

        """System Feature"""
        self.system_features = Frame(self.subresults)
        self.system_features.grid(row=0, column=0, padx=5, pady=1, sticky="nswe")

        """Event"""
        self.event = Frame(self.subresults)
        self.event.grid(row=0, column=1, padx=5, pady=1, sticky="e")

        """Offboard"""
        self.offboard = Frame(self.result)
        self.offboard.grid(row=2, column=0, padx=5, pady=1, sticky="nswe")

        """PTT"""
        self.PTT = Frame(self.result)
        self.PTT.grid(row=3, column=0, padx=5, pady=1, sticky="nswe")

    def updatePTT(self,result):
        self.PTT.grid_forget()
        self.PTT = Frame(self.result)
        self.PTT.grid(row=3, column=0, padx=5, pady=1, sticky="nswe")
        Label(self.PTT, text="PTT SESSIONS", font="Calibri 10 bold", width=30, bd=2, relief=GROOVE).grid(row=0, column=0, padx=5, pady=1, sticky="w")
        Label(self.PTT, text=result, font="Calibri 10 italic").grid(row=1, column=0, padx=5, pady=1, sticky="w")

    def updateOffboard(self, result, offboardEnabled):
        self.offboard.grid_forget()
        self.offboard = Frame(self.result)
        self.offboard.grid(row=2, column=0, padx=5, pady=1, sticky="nswe")
        Label(self.offboard, text="OFFBOARD", font="Calibri 10 bold", width=30, bd=2, relief=GROOVE).grid(row=0,
                                                                                                          column=0,
                                                                                                          padx=5,
                                                                                                          pady=1,
                                                                                                          sticky="w")
        r = 1
        for key, value in result:
            if value == "False":
                Label(self.offboard, text=key).grid(row=r, column=0, padx=5, pady=1, sticky="w")
                Label(self.offboard, text=value, fg='red').grid(row=r, column=1, padx=5, pady=1, sticky="w")
                r += 1
        color = 'dark green'
        mystring = "OFFBOARD CONNECTED"
        if not offboardEnabled:
            mystring = "OFFBOARD CONNECTION FAILED"
            color = 'red'
        Label(self.offboard, text=mystring, fg=color).grid(row=r, column=0, padx=5, pady=1, sticky="nsw")

    def updateEvent(self, result):
        self.event.grid_forget()
        self.event = Frame(self.subresults)
        self.event.grid(row=0, column=1, padx=5, pady=1, sticky="e")
        Label(self.event, text="EVENTS", font="Calibri 10 bold", width=30, bd=2, relief=GROOVE).grid(row=0, column=0,
                                                                                                     padx=7, pady=1,
                                                                                                     sticky="w")
        Label(self.event, text="", width=10).grid(row=0, column=1, padx=5, pady=1, sticky="w")
        r = 1
        for key, value in result:
            Label(self.event, text=key).grid(row=r, column=0, padx=5, pady=1, sticky="w")
            if value == "True":
                Label(self.event, text=value).grid(row=r, column=1, padx=5, pady=1, sticky="w")
            else:
                Label(self.event, text=value, fg='red').grid(row=r, column=1, padx=5, pady=1, sticky="w")
            r += 1

    def updateSF(self, result):
        self.system_features.grid_forget()
        self.system_features = Frame(self.subresults)
        self.system_features.grid(row=0, column=0, padx=5, pady=1, sticky="nswe")
        Label(self.system_features, text="SYSTEM FEATURES", font="Calibri 10 bold", width=30, bd=2, relief=GROOVE).grid(
            row=0, column=0, padx=7, pady=1, sticky="w")
        Label(self.system_features, text="", width=10).grid(row=0, column=1, padx=5, pady=1, sticky="w")
        r = 1
        for key, value in result:
            Label(self.system_features, text=key).grid(row=r, column=0, padx=5, pady=1, sticky="w")
            if value == "True":
                Label(self.system_features, text=value).grid(row=r, column=1, padx=5, pady=1, sticky="w")
            else:
                Label(self.system_features, text=value, fg='red').grid(row=r, column=1, padx=5, pady=1, sticky="w")
            r += 1

    def updateprecheck(self, result):
        # Take a list of <identifier,var> and and to the precheck accordingly
        self.offboard.grid_forget()
        self.precheck = Frame(self.result)
        self.precheck.grid(row=0, column=0, padx=5, pady=1, sticky="nswe")
        Label(self.precheck, text="PRECHECKS", font="Calibri 10 bold", width=30, bd=2, relief=GROOVE).grid(row=0,
                                                                                                           column=0,
                                                                                                           padx=5,
                                                                                                           pady=1,
                                                                                                           sticky="ns")
        r = 4
        for key, value in result:
            if key == "Build Version":
                Label(self.precheck, text=key).grid(row=1, column=0, padx=5, pady=1, sticky="w")
                Label(self.precheck, text=value).grid(row=1, column=1, padx=5, pady=1, sticky="w")
            elif key == "Navidata Path":
                Label(self.precheck, text=key).grid(row=2, column=0, padx=5, pady=1, sticky="w")
                Label(self.precheck, text=value).grid(row=2, column=1, padx=5, pady=1, sticky="w")
            elif key == "Navigation Data":
                Label(self.precheck, text=key).grid(row=3, column=0, padx=5, pady=1, sticky="w")
                Label(self.precheck, text=value).grid(row=3, column=1, padx=5, pady=1, sticky="w")
            else:
                Label(self.precheck, text=key).grid(row=r, column=0, padx=5, pady=1, sticky="w")
                Label(self.precheck, text=value).grid(row=r, column=1, padx=5, pady=1, sticky="w")
            r += 1

    def uploadfilename(self, my_file):
        self.fileName.config(state=NORMAL)
        self.fileName.delete(1.0, END)
        self.fileName.insert(END, my_file)
        self.fileName.see(END)
        self.fileName.config(state=DISABLED)

    def uploadprojectname(self, project_name):
        mystring = "This is " + project_name
        Label(self.getfile, text=mystring, font="Calibri 10 italic").grid(row=1, column=0, sticky="ns")
