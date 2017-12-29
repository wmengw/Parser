import parserUI
import keywordsJson
import tkFileDialog
from Tkinter import *
import json
import re
import os


class parser():

    MYDATA = []

    def searchInitialInfo(self, project_name, my_json):
        # The block below needs more comments...but for now leave it
        for line in self.MYDATA:
            for i in my_json["Project"][project_name]["Precheck"]:
                regexp = re.compile(my_json["Project"][project_name]["Precheck"][i]['search'])
                if regexp.search(line):
                    start = my_json["Project"][project_name]["Precheck"][i]['start']
                    end = my_json["Project"][project_name]["Precheck"][i]['end']
                    foo = re.search((start + "(.*)" + end), line)
                    if 'result' not in my_json["Project"][project_name]["Precheck"][i]:
                        my_json["Project"][project_name]["Precheck"][i]["result"] = foo.group(1)
        return my_json

    def searchSystemFeature(self,project_name, my_json):
        for line in self.MYDATA:
            if str(my_json["Project"][project_name]["System Features"]["search"]) in line:
                for i in my_json["Project"][project_name]["System Features"]["list"]:
                    if i in line:
                        my_json["Project"][project_name]["System Features"]["list"][i]=True
        return my_json


    def searchEvent(self,project_name,my_json):
        for line in self.MYDATA:
            for event in my_json["Project"][project_name]["Event"]:
                if str(event) in line:
                    my_json["Project"][project_name]["Event"][event]= True
                    #print event
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
        foo = "GM MY18"
        return foo

    def processing(self):
        # Initialize Json
        my_json_temp = keywordsJson.keywords().get()

        # Find related project
        project_name = self.searchProject()

        # Log precheck
        json_modified = self.searchInitialInfo(project_name, my_json_temp)

        # Clear previous result
        # self.ui.cleartextbox()

        """Precheck"""
        precheck_result = []

        for i in json_modified["Project"][project_name]["Precheck"]:
            if 'result' in json_modified["Project"][project_name]["Precheck"][i]:
                precheck_result.append((i,json_modified["Project"][project_name]["Precheck"][i]["result"]))
                # self.ui.uploadstringwithformat(i, self.keywords["Project"][project_name]["Precheck"][i]["result"])
        self.ui.updateprecheck(precheck_result)

        """System Features"""
        json_modified = self.searchSystemFeature(project_name,json_modified)
        sf_result = []
        for i in json_modified["Project"][project_name]["System Features"]["list"]:
            sf_result.append((i,str(json_modified["Project"][project_name]["System Features"]["list"][i])))
        self.ui.updateSF(sf_result)

        """Event"""
        json_modified = self.searchEvent(project_name, json_modified)
        event_result = []
        for i in json_modified["Project"][project_name]["Event"]:
            event_result.append((i, str(json_modified["Project"][project_name]["Event"][i])))
        self.ui.updateEvent(event_result)

        #
        # PTT_session = "There are(is) " + str(len(self.split(self.MYDATA))) + " PTT session(s)."
        # self.ui.uploadstring(PTT_session)

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
