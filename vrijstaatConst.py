import PygameUI as pg

GREY = [200,200,200]
WHITE= [255,255,255]
BLACK = [0, 0, 0]
RED = [255,0,0]

TOPICLIST = ["SIGN", "#"]

# Vars to identify ESPs
ESPlist = []

#Puzzles
puzzleList = []
puzzles = {
		"Holletje"		:	["HolletjesButton", "HolletjesServo"],
		"Kooitjes"		:	["Kooitjes"],
		"Terrarium"		:	["Terrarium"],
		"Poepscanner"	:	["PoepScanner"],
		"Crusher"		: 	["Crusher"],
		"Medicein"		:	["Medicein", "ColorScanner", "MedKast", "CodePanel"],
		"Quiz"			:	["Quiz"]}

TEMPLATE = {
	"SmallButton" : {
		"type"			:	pg.Button,
		"location"		:	(0,0),
		"size"			:	(40,40),
		"color"			:	WHITE,
		"visable"		:	True,
		"fontsize"		:	10,
		"textcolor"		:	BLACK,
		},

	"SmallToggleButton" : {
		"type"			:	pg.ToggleButton,
		"location"		:	(0,0),
		"size"			:	(40,40),
		"color"			:	WHITE,
		"visable"		:	True,
		"fontsize"		:	10,
		"textcolor"		:	BLACK,
		},

	"MiddleButton" : {
		"type"			:	pg.Button,
		"location"		:	(0,0),
		"size"			:	(100,40),
		"color"			:	WHITE,
		"visable"		:	True,
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		},

	"BigText" : {
		"type"			:	pg.Text,
		"location"		:	(0,0),
		"size"			:	(50,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"",
		"fontsize"		:	18,
		},

	"MainContainer" : {
		"type"			:	pg.Container,
		"contname"		:	"MainContainer",
		"location"		:	(5, 100),
		"size"			:	(550, 400),
		"color"			:	BLACK,
		"visable"		:	False,
		"border"		:	2,
		"bordercolor"	:	WHITE,
		"objects"		:	[],
		"title"			:	"Main",
		"showtitle"		:	True,
		},

	"SubContainer" : {
		"type"			:	pg.Container,
		"contname"		:	"SubContainer",
		"location"		:	(570, 80),
		"size"			:	(500, 530),
		"color"			:	BLACK,
		"visable"		:	False,
		"border"		:	2,
		"bordercolor"	:	WHITE,
		"objects"		:	[],
		"title"			:	"Sub",
		"showtitle"		:	True,
		},

	"HeaderButton" : {
		"type"			:	pg.Button,
		"location"		:	(0, 0),
		"size"			:	(100,30),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Header",
		"fontsize"		:	14,
		"textcolor"		:	BLACK,
		},

	"HeaderDropdownButton" : {
		"type"			:	pg.DropDownButton,
		"location"		:	(0, 0),
		"size"			:	(100,30),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Header",
		"fontsize"		:	14,
		"textcolor"		:	BLACK,
		},

	}

DROPDOWNITEM = {
	"type"			:	pg.DropDown,
	"location"		:	(0, 50),
	"size"			:	(100,30),
	"color"			:	WHITE,
	"visable"		:	False,
	"fontsize"		:	14,
	"textcolor"		:	BLACK,
	}

HEADER = {
	"MainContainer"	:	{
		"type"			:	pg.HeaderContainer,
		"contname"		:	"HeaderContainer",
		"location"		:	(0, 0),
		"size"			:	(1080, 10),
		"color"			:	BLACK,
		"visable"		:	True,
		"border"		:	2,
		"bordercolor"	:	WHITE,
		"objects"		:	[],
		"title"			:	"Header",
		"showtitle"		:	False,
		},

	"FakeESPButton" : {
		"fromobject"	:	TEMPLATE["HeaderButton"],
		"text"			:	"Fake",
		},

	"StartGameButton" : {
		"fromobject"	:	TEMPLATE["HeaderButton"],
		"text"			:	"Start",
		},

	"MainWindowButton" : {
		"fromobject"	:	TEMPLATE["HeaderButton"],
		"text"			:	"Main",
		},

	"ResetButton" : {
		"fromobject"	:	TEMPLATE["HeaderButton"],
		"text"			:	"Reset",
		},

	"ESPDropdownButton" : {
		"type"			:	pg.DropDownButton,
		"fromobject"	:	TEMPLATE["HeaderDropdownButton"],
		"text"			:	"ESPS",
		},

	"RoomDropdownButton" : {
		"type"			:	pg.DropDownButton,
		"fromobject"	:	TEMPLATE["HeaderDropdownButton"],
		"text"			:	"Rooms",
		},

	"PuzzelDropdownButton" : {
		"type"			:	pg.DropDownButton,
		"fromobject"	:	TEMPLATE["HeaderDropdownButton"],
		"text"			:	"Puzzles",
		},
	}

MAINWINDOW = {

	"MainContainer" : {
		"fromobject"	:	TEMPLATE["MainContainer"],
		"contname"		:	"MainContainer",
		},

	"NextRoomButton" : {
		"type"			:	pg.Button,
		"location"		:	(320, 5),
		"size"			:	(100,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Next",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		},


	"PlaySoundBUTTON" : {
		"fromobject"	:	TEMPLATE["SmallButton"],
		"location"		:	(200,100),
		"text"			:	"PlaySound",
		"function"		:	"SendMqtt('MusicPlayer','text1.mp3')"
		},

	"MainProgressTextBox" : {
		"type"			:	pg.TextBox,
		"location"		:	(10,20),
		"size"			:	(150,200),
		"color"			:	BLACK,
		"visable"		:	False,
		"border"		:	2,
		"bordercolor"	:	WHITE,
		"title"			:	"Progress",
		"showtitle"		:	True,
		"maxlines"		:	10,
		"textcolor"		:	WHITE,
		},

	"GameTimerText" : {
		"type"			:	pg.Text,
		"location"		:	(200,10),
		"size"			:	(50,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Time: ",
		"fontsize"		:	12,
		},
	}

CONTAINERS = {
	"MainContainer" : {
		"type"			:	pg.Container,
		"contname"		:	"MainContainer",
		"location"		:	(5, 100),
		"size"			:	(550, 400),
		"color"			:	BLACK,
		"visable"		:	True,
		"border"		:	2,
		"bordercolor"	:	WHITE,
		"objects"		:	[],
		"title"			:	"Main",
		"showtitle"		:	True,
		},

	"SubContainer" : {
		"type"			:	pg.Container,
		"contname"		:	"SubContainer",
		"location"		:	(570, 80),
		"size"			:	(500, 530),
		"color"			:	BLACK,
		"visable"		:	False,
		"border"		:	2,
		"bordercolor"	:	WHITE,
		"objects"		:	[],
		"title"			:	"Sub",
		"showtitle"		:	True,
		}
	}

TEXTBOXES = {
	"MainDebugTextBox" : {
		"location"		:	(5, 515),
		"size"			:	(500, 200),
		"color"			:	BLACK,
		"visable"		:	True,
		"border"		:	2,
		"bordercolor"	:	WHITE,
		"title"			:	"Debug Messages",
		"showtitle"		:	True,
		"maxlines"		:	10,
		"textcolor"		:	WHITE,
		},

	"ESPMqttTextBox" : {
		"location"		:	(290, 25),
		"size"			:	(200, 490),
		"color"			:	BLACK,
		"visable"		:	False,
		"border"		:	2,
		"bordercolor"	:	WHITE,
		"title"			:	"Mqtt Messages",
		"showtitle"		:	True,
		"maxlines"		:	16,
		"textcolor"		:	WHITE,
		}
	}

LABUI = {
	"ButtonContainer" : {
		"fromobject"	:	TEMPLATE["MainContainer"],
		"contname"		:	"LabButtonContainer",
		"location"		:	(5, 345),
		"size"			:	(400, 40),
		"objects"		:  ["KAST1BUTTON",
							"KAST2BUTTON",
							"KAST3BUTTON",
							"KAST4BUTTON",
							"KAST5BUTTON",
							"KAST6BUTTON"],
		"border"		:	0,
		"bordercolor"	:	WHITE,
		"title"			:	"Kast",
		"autofit"		: 	True,
		"showtitle"		:	True,
		},	

	"KAST1BUTTON" : {
		"fromobject"	:	TEMPLATE["SmallButton"],
		"text"			:	"Kast 1",
		"function"		:	"SendMqtt('LAB/MEDKAST','1B')"
		},

	"KAST2BUTTON" : {
		"fromobject"	:	TEMPLATE["SmallButton"],
		"text"			:	"Kast 2",
		"function"		:	"SendMqtt('LAB/MEDKAST','2')"
		},

	"KAST3BUTTON" : {
		"fromobject"	:	TEMPLATE["SmallButton"],
		"text"			:	"Kast 3",
		"function"		:	"SendMqtt('LAB/MEDKAST','3')"
		},

	"KAST4BUTTON" : {
		"fromobject"	:	TEMPLATE["SmallButton"],
		"text"			:	"Kast 4",
		"function"		:	"SendMqtt('LAB/MEDKAST','4')"
		},

	"KAST5BUTTON" : {
		"fromobject"	:	TEMPLATE["SmallButton"],
		"text"			:	"Kast 5",
		"function"		:	"SendMqtt('LAB/MEDKAST','5')"
		},

	"KAST6BUTTON" : {
		"fromobject"	:	TEMPLATE["SmallButton"],
		"text"			:	"Kast 6",
		"function"		:	"SendMqtt('LAB/MEDKAST','6')"
		},

	"LabMqttTextBox" : {
		"type"			:	pg.TextBox,
		"location"		:	(345, 25),
		"size"			:	(200, 370),
		"color"			:	BLACK,
		"visable"		:	False,
		"border"		:	2,
		"bordercolor"	:	WHITE,
		"title"			:	"Mqtt Messages",
		"showtitle"		:	True,
		"maxlines"		:	16,
		"textcolor"		:	WHITE,
		},

	"MainContainer" : {
		"fromobject"	:	TEMPLATE["MainContainer"],
		"contname"		:	"LABCONTAINER",
		},

	"LabColorText" : {
		"fromobject"	:	TEMPLATE["BigText"],
		"location"		:	(5,30),
		"text"			:	"ColorScanner: ",
		},

	"LabCrusherStateText" : {
		"fromobject"	:	TEMPLATE["BigText"],
		"location"		:	(5,55),
		"text"			:	"Crusher: ",
		},

	"LabReadyText" : {
		"fromobject"	:	TEMPLATE["BigText"],
		"location"		:	(5,5),
		"text"			:	"Ready: READY",
		},
	}

TUINUI = {
	"ButtonContainer" : {
		"fromobject"	:	TEMPLATE["MainContainer"],
		"contname"		:	"PoepButtonContainer",
		"location"		:	(5, 345),
		"size"			:	(400, 40),
		"objects"		:  ["POEPHOLBUTTON",
							"POEPKOOIBUTTON",
							"POPTERRBUTTON"],
		"border"		:	0,
		"title"			:	"Poepjes",
		"autofit"		: 	True,
		},

	# "PuzzleContainer" : {
	# 	"fromobject"	:	TEMPLATE["MainContainer"],
	# 	"contname"		:	"TuinPuzzleContainer",
	# 	"location"		:	(5, 345),
	# 	"size"			:	(400, 40),
	# 	"objects"		:  ["POEPHOLBUTTON",
	# 						"POEPKOOIBUTTON",
	# 						"POPTERRBUTTON"],
	# 	"border"		:	0,
	# 	"title"			:	"Poepjes",
	# 	"autofit"		: 	True,
	# 	},		

	"POEPHOLBUTTON" : {
		"fromobject"	:	TEMPLATE["SmallButton"],
		"text"			:	"Hol Poep",
		"function"		:	"SendMqtt('poep','1')"
		},

	"POEPKOOIBUTTON" : {
		"fromobject"	:	TEMPLATE["SmallButton"],
		"text"			:	"Kooi Poep",
		"function"		:	"SendMqtt('poep','2')"
		},

	"POPTERRBUTTON" : {
		"fromobject"	:	TEMPLATE["SmallButton"],
		"text"			:	"Terr Poep",
		"function"		:	"SendMqtt('poep','3')"
		},

	"TuinMqttTextBox" : {
		"type"			:	pg.TextBox,
		"location"		:	(345, 25),
		"size"			:	(200, 370),
		"color"			:	BLACK,
		"visable"		:	False,
		"border"		:	2,
		"bordercolor"	:	WHITE,
		"title"			:	"Mqtt Messages",
		"showtitle"		:	True,
		"maxlines"		:	16,
		"textcolor"		:	WHITE,
		},


	"MainContainer" : {
		"fromobject"	:	TEMPLATE["MainContainer"],
		"contname"		:	"TUINCONTAINER",
		# "title"			:	"Tuin",
		},

	"PoepText" : {
		"fromobject"	:	TEMPLATE["BigText"],
		"location"		:	(5,30),
		"text"			:	"Poepjes: ",
		},

	"TuinReadyText" : {
		"fromobject"	:	TEMPLATE["BigText"],
		"location"		:	(5,5),
		"text"			:	"Ready: READY",
		},
	}

ESPUI = {
	"ESPMqttTextBox" : {
		"location"		:	(290, 25),
		"size"			:	(200, 490),
		"color"			:	BLACK,
		"visable"		:	False,
		"border"		:	2,
		"bordercolor"	:	WHITE,
		"title"			:	"Mqtt Messages",
		"showtitle"		:	True,
		"maxlines"		:	16,
		"textcolor"		:	WHITE,
		},

	"MainContainer" : {
		"fromobject"	:	TEMPLATE["SubContainer"],
		"contname"		:	"ESPContainer",
		},

	"SignedText" : {
		"type"			:	pg.Text,
		"location"		:	(5,5),
		"size"			:	(50,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Signed: NO",
		"fontsize"		:	18,
		},

	"ButtonContainer" : {
		"fromobject"	:	TEMPLATE["MainContainer"],
		"contname"		:	"ESPButtonContainer",
		"location"		:	(5, 345),
		"size"			:	(200, 40),
		"objects"		:  	[],
		"border"		:	0,
		"title"			:	"OUTPUT",
		"autofit"		: 	True,
		"showtitle"		:	True,
		},
	}

ESPDict = {
	"HolletjesButtons"	: {
		"topic"	:	"HB",
		"sign"	:	"HolletjesButton",
		"outputs":	{
					"ButtonArray" : {
						"type"			:	pg.ButtonArray,
						"location"		:	(320, 300),
						"size"			:	(150,200),
						"contname"		:	"Buttonarray",
						"varlist"		:	range(1,6),
						"functionlist"	:	["SendMqtt('HB','","')"],
						"buttontemplate":	TEMPLATE["SmallButton"],
						},
					},
		},
	"ColorScanner"		: {
		"topic"	:	"CS",
		"sign"	:	"ColorScanner",
		"outputs":	{
					"CS1" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"RED",
						"function"		:	"SendMqtt('CS','1')"
						},
					"CS2" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"PINK",
						"function"		:	"SendMqtt('CS','2')"
						},
					"CS3" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"PURPLE",
						"function"		:	"SendMqtt('CS','3')"
						},
					"CS4" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"DARKRED",
						"function"		:	"SendMqtt('CS','4')"
						},
					"CS5" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"Blue",
						"function"		:	"SendMqtt('CS','5')"
						},
					},
		},	
	"HolletjesServo"	: {
		"topic"	:	"HB",
		"sign"	:	"HolletjesServo",
		"inputs":	{},
		},
	"MediceinKast"		: {
		"topic"	:	"MED",
		"sign"	:	"MedKast",
		"outputs":	{
					"MED1" : {
						"fromobject"	:	TEMPLATE["SmallToggleButton"],
						"text"			:	"1",
						"function"		:	"SendMqtt('MED','a1B')",
						"offfunction"	:	"SendMqtt('MED','a1A')",
						},
					"MED2" : {
						"fromobject"	:	TEMPLATE["SmallToggleButton"],
						"text"			:	"2",
						"function"		:	"SendMqtt('MED','a2B')",
						"offfunction"	:	"SendMqtt('MED','a2A')",
						},
					"MED3" : {
						"fromobject"	:	TEMPLATE["SmallToggleButton"],
						"text"			:	"3",
						"function"		:	"SendMqtt('MED','a3B')",
						"offfunction"	:	"SendMqtt('MED','a3A')",
						},
					"MED4" : {
						"fromobject"	:	TEMPLATE["SmallToggleButton"],
						"text"			:	"4",
						"function"		:	"SendMqtt('MED','a3B')",
						"offfunction"	:	"SendMqtt('MED','a3A')",
						},
					"MED5" : {
						"fromobject"	:	TEMPLATE["SmallToggleButton"],
						"text"			:	"5",
						"function"		:	"SendMqtt('MED','a4B')",
						"offfunction"	:	"SendMqtt('MED','a4A')",
						},
					"MED6" : {
						"fromobject"	:	TEMPLATE["SmallToggleButton"],
						"text"			:	"6",
						"function"		:	"SendMqtt('MED','a5B')",
						"offfunction"	:	"SendMqtt('MED','a5A')",
						},
					},
		},

	"CodePanel"			: {
		"topic"	:	"Panel",
		"sign"	:	"CodePanel",
		"outputs":	{
					"Panel1" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"1",
						"function"		:	"SendMqtt('MED','1')"
						},
					"Panel2" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"2",
						"function"		:	"SendMqtt('MED','2')"
						},
					"Panel3" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"3",
						"function"		:	"SendMqtt('MED','3')"
						},
					"Panel4" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"4",
						"function"		:	"SendMqtt('MED','4')"
						},
					"Panel5" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"5",
						"function"		:	"SendMqtt('MED','5')"
						},
					"Panel6" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"6",
						"function"		:	"SendMqtt('MED','6')"
						},
					"Panel7" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"4",
						"function"		:	"SendMqtt('MED','4')"
						},
					"Panel8" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"5",
						"function"		:	"SendMqtt('MED','5')"
						},
					"Panel9" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"6",
						"function"		:	"SendMqtt('MED','6')"
						},
					},
		},
	"PoepScanner"		: {
		"topic"	:	"poep",
		"sign"	:	"PoepScanner",
		"outputs":	{
					"POEP1" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"Hol",
						"function"		:	"SendMqtt('poep','1')"
						},
					"POEP2" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"Kooi",
						"function"		:	"SendMqtt('poep','2')"
						},
					"POEP3" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"Ter",
						"function"		:	"SendMqtt('poep','3')"
						},
					},
		},
	}

#Rooms
RoomList = []
Rooms = {
	"LAB": 
		{"puzzles" : ["Quiz","Medicein","Crusher"],
		 "Name": "LAB", 
		 "UI" : LABUI},
	"TUIN": 
		{"puzzles" : ["Holletje"],
		 "Name": "TUIN",
		 "UI" : TUINUI},
		}
	# "A": {"puzzles":["Holletje"], "Name": "Tuin", "UI" : LABUI},
			# "B": {"puzzles":["Quiz","Medicein","Crusher"], "Name": "Lab", "UI" : LABUI}}


# groupA = Group("A")
# groupB = Group("B")

# pTuinA = Room("Tuin", groupA)
# pTuinB = Room("Tuin", groupB)

# kid1 = Kid(1)
# kid1.setGroup(groupA)

