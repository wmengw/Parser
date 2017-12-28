import parserUI
import tkFileDialog
from Tkinter import *
import json
import re
import os


class parser():
    keywords = {
        "Project": {
            "GM MY18": {
                "Precheck": {
                    "Build Version": {
                        "search": "Version: GM_Info30_MY18.*?';",
                        "start": "Version: ",
                        "end": "';",
                    },
                    "Navigation Data": {
                        "search": "NavData Version:.*?';",
                        "start": "version_name=",
                        "end": " supported_nat_builds",
                    },
                    "Navidata Path": {
                        "search": "system_navi_data_path.*?' system",
                        "start": "system_navi_data_path='",
                        "end": "' system",
                    },
                    # "J5": {
                    #     "start" : "",
                    #     "end" : "",
                    # },
                    # "J6": {
                    #     "start": "",
                    #     "end": "",
                    # },
                    "Connected Phone Count": {
                        "search": "instance='DCC_PHO_DEV_LIST' event=NUANCE_ASR_DYNAMICCONTENTCONSUMEREVENT_DCC_WITH_N_ENTRIES message='.*?';",
                        "start": "message='",
                        "end": "';",
                    },
                    "Media Song Count": {
                        "search": "instance='DCC_MEDIA_iphone-id' event=NUANCE_ASR_DYNAMICCONTENTCONSUMEREVENT_DCC_WITH_N_ENTRIES message='.*?';",
                        "start": "message='",
                        "end": "';",
                    },
                },
                "System Features": {
                    "search": "system_feature_list={",
                    "list":{
                        "SYSTEM_FEATURE_BT_MUSIC": False,
                        "SYSTEM_FEATURE_BT_PHONE": False,
                        "SYSTEM_FEATURE_DAB": False,
                        "SYSTEM_FEATURE_HD": False,
                        "SYSTEM_FEATURE_INTERNET": False,
                        "SYSTEM_FEATURE_NAVI": False,
                        "SYSTEM_FEATURE_ONSTAR": False,
                        "SYSTEM_FEATURE_USB": False,
                        "SYSTEM_FEATURE_XM": False,
                    },
                },
                "Event": {
                    "PHONE_DEVICE_CHANGED": False,
                    "PHONE_DEVICE_PB_CHANGED": False,
                    "MEDIA_DEVICE_CHANGED": False,
                    "MEDIA_DATA_CHANGED": False,
                    "FM_STATIONS_NEED_UPDATE": False,
                    "DAB_STATIONS_NEED_UPDATE": False,
                    "XM_STATIONS_NEED_UPDATE": False,
                    "NLU_EMBEDDED_ACTIVATE": False,
                    "NAVI_CARD_MOUNT": False,
                },
                "OffboardConnection": "HttpRequest",
            },
            "GM 19": {
                "System Features": {
                    "search": "system_feature_list",
                    "start": "system_feature_list={",
                    "end": "}",
                    # "SYSTEM_FEATURE_APPS"
                    # "SYSTEM_FEATURE_AUDIO"
                    # "SYSTEM_FEATURE_BT_MUSIC"
                    # "SYSTEM_FEATURE_BT_PHONE"
                    # "SYSTEM_FEATURE_HD"
                    # "SYSTEM_FEATURE_INTERNET"
                    # "SYSTEM_FEATURE_NAVI"
                    # "SYSTEM_FEATURE_ONSTAR"
                    # "SYSTEM_FEATURE_PHONE"
                    # "SYSTEM_FEATURE_USB"
                    # "SYSTEM_FEATURE_XM"
                },
            },
            "CIP": {

            },
        },
    }

    MYDATA = []

    def initializejson(self):
        json_string = json.dumps(self.keywords)
        self.keywords = json.loads(json_string)

    def searchInitialInfo(self, project_name):
        # The block below needs more comments...but for now leave it
        for line in self.MYDATA:
            for i in self.keywords["Project"][project_name]["Precheck"]:
                regexp = re.compile(self.keywords["Project"][project_name]["Precheck"][i]['search'])
                if regexp.search(line):
                    start = self.keywords["Project"][project_name]["Precheck"][i]['start']
                    end = self.keywords["Project"][project_name]["Precheck"][i]['end']
                    foo = re.search((start + "(.*)" + end), line)
                    if 'result' not in self.keywords["Project"][project_name]["Precheck"][i]:
                        self.keywords["Project"][project_name]["Precheck"][i]["result"] = foo.group(1)

    def searchSystemFeature(self,project_name):
        for line in self.MYDATA:
            if str(self.keywords["Project"][project_name]["System Features"]["search"]) in line:
                for i in self.keywords["Project"][project_name]["System Features"]["list"]:
                    if i in line:
                        self.keywords["Project"][project_name]["System Features"]["list"][i]=True


    def searchEvent(self,project_name):
        for line in self.MYDATA:
            for event in self.keywords["Project"][project_name]["Event"]:
                if str(event) in line:
                    self.keywords["Project"][project_name]["Event"][event]= True
                    #print event

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
        self.initializejson()

        # Find related project
        project_name = self.searchProject()

        # Log precheck
        self.searchInitialInfo(project_name)

        # Clear previous result
        # self.ui.cleartextbox()

        """Precheck"""
        precheck_result = []

        for i in self.keywords["Project"][project_name]["Precheck"]:
            if 'result' in self.keywords["Project"][project_name]["Precheck"][i]:
                precheck_result.append((i,self.keywords["Project"][project_name]["Precheck"][i]["result"]))
                # self.ui.uploadstringwithformat(i, self.keywords["Project"][project_name]["Precheck"][i]["result"])
        self.ui.updateprecheck(precheck_result)

        """System Features"""
        self.searchSystemFeature(project_name)
        sf_result = []
        for i in self.keywords["Project"][project_name]["System Features"]["list"]:
            sf_result.append((i,str(self.keywords["Project"][project_name]["System Features"]["list"][i])))
        self.ui.updateSF(sf_result)

        """Event"""
        self.searchEvent(project_name)
        event_result = []
        for i in self.keywords["Project"][project_name]["Event"]:
            event_result.append((i, str(self.keywords["Project"][project_name]["Event"][i])))
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
