import parserUI
import keywordsJson
import tkFileDialog
from Tkinter import *
import json
import re
import os


class parser():

    MYDATA = []

    def searchInitialInfo(self, my_json):
        # The block below needs more comments...but for now leave it
        for line in self.MYDATA:
            for i in my_json["Precheck"]:
                regexp = re.compile(my_json["Precheck"][i]['search'])
                if regexp.search(line):
                    start = my_json["Precheck"][i]['start']
                    end = my_json["Precheck"][i]['end']
                    foo = re.search((start + "(.*)" + end), line)
                    if 'result' not in my_json["Precheck"][i]:
                        my_json["Precheck"][i]["result"] = foo.group(1)
        return my_json

    def searchSystemFeature(self, my_json):
        for line in self.MYDATA:
            if str(my_json["System Features"]["search"]) in line:
                for i in my_json["System Features"]["list"]:
                    if i in line:
                        my_json["System Features"]["list"][i]=True
        return my_json


    def searchEvent(self,my_json):
        for line in self.MYDATA:
            for event in my_json["Event"]:
                if str(event) in line:
                    my_json["Event"][event]= True
                    #print event
        return my_json

    def searchOffboard(self,my_json):
        for line in self.MYDATA:
            for i in my_json["Offboard Connection"]:
                if (i and str(my_json["Offboard Connection"][i]["search"])) in line:
                    my_json["Offboard Connection"][i]["result"] = not my_json["Offboard Connection"][i]["result"]
        return my_json

    def split(self, mylist):
        # start with the first PTT
        start_point = []
        segment = []
        for i in range(len(mylist)):
            if "NAME=PTT" in mylist[i]:
                start_point.append(i)
        for i in range(len(start_point)):
            if i != len(start_point) - 1:
                segment.append(mylist[start_point[i]:start_point[i + 1]])
            else:
                segment.append(mylist[start_point[i]:])
        return segment

    def searchProject(self):
        # Return string: project name
        foo = "GM_MY18"
        return foo

    def processing(self):
        # Find related project
        project_name = self.searchProject()
        self.ui.uploadprojectname(project_name)

        # Initialize Json
        if project_name == "GM_MY18":
            my_json_temp = keywordsJson.keywords().getGM_MY18()
        else:
            my_json_temp = keywordsJson.keywords().getGM_MY18() # NEED TO CHANGE!!! LEAVE IT FOR NOW

        # Log precheck
        json_modified = self.searchInitialInfo(my_json_temp)

        # Clear previous result
        # self.ui.cleartextbox()

        """Precheck"""
        precheck_result = []

        for i in json_modified["Precheck"]:
            if 'result' in json_modified["Precheck"][i]:
                precheck_result.append((i,json_modified["Precheck"][i]["result"]))
        self.ui.updateprecheck(precheck_result)

        """System Features"""
        json_modified = self.searchSystemFeature(json_modified)
        sf_result = []
        for i in json_modified["System Features"]["list"]:
            sf_result.append((i,str(json_modified["System Features"]["list"][i])))
        self.ui.updateSF(sf_result)

        """Event"""
        json_modified = self.searchEvent(json_modified)
        event_result = []
        for i in json_modified["Event"]:
            event_result.append((i, str(json_modified["Event"][i])))
        self.ui.updateEvent(event_result)

        """Offboard"""
        json_modified = self.searchOffboard(json_modified)
        offboard_result = []
        OffboardEnable = True
        for i in json_modified["Offboard Connection"]:
            if not json_modified["Offboard Connection"][i]["result"]:
                OffboardEnable = False
            offboard_result.append((i, str(json_modified["Offboard Connection"][i]["result"])))
        self.ui.updateOffboard(offboard_result, OffboardEnable)

        PTT_session = "There are(is) " + str(len(self.split(self.MYDATA))) + " PTT session(s)."
        self.ui.updatePTT(PTT_session)

        # Clear MYDATA array for the next file
        self.MYDATA = []

    def openwindows(self, event):
        # Open file
        my_file = tkFileDialog.askopenfile('r')

        # Print name of the current opened file
        file_name = os.path.split(my_file.name)[1]
        self.ui.uploadfilename(file_name)

        # Copy log to array
        for line in my_file:
            self.MYDATA.append(line.replace('\n', ''))

        # Close file
        my_file.close()

        # Start to analyze
        self.processing()

    def __init__(self):
        self.root = Tk()

        self.ui = parserUI.UI(self.root)
        self.ui.getfileButton.bind('<ButtonRelease>', self.openwindows)

        # Display UI
        self.root.mainloop()


if __name__ == '__main__':
    main = parser()
