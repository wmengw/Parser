import json

class keywords():
	
	def __init__(self):

		self.TEMPLATE= {
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
	            "GM MY19": {
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

	def get(self):
		json_string = json.dumps(self.TEMPLATE)
		new_keywords = json.loads(json_string)
		return new_keywords
		