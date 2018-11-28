import PygameUI as pg


soundlist={}
soundlist["radiokapot"] ='RadioRepareerVerbindingProf.wav'
soundlist["wezen1"] ='WezensLoop-01.wav'
soundlist["wezen2"] ='WezensLoop-02.wav'
soundlist["wezen3"] ='WezensLoop-03.wav'
soundlist["alarm"] ='alarm.wav'
soundlist["error1"] ='error1.wav'
# soundlist["error2"] ='error2.wav'
soundlist["winsound"] ='Win.wav'
soundlist["succes"] ='succes.wav'
soundlist["error3"] ='error3.wav'
soundlist["dooropen"] ='dooropen.wav'
# soundlist["doorlock1"] ='doorloc'
soundlist["doorlock2"] ='doorlock2.wav'
# soundlist["rats"] ='rats.mp3'
soundlist["soundcreatures"] ='soundscreatures.wav'
soundlist["intube"] ='soundsintube.wav'
soundlist["intro1"] ='intro.wav'
soundlist["intro2"] ='intro2.wav'
soundlist["inniti"] ='inniti.wav'
soundlist["lockdown1"] ='lockdown1.wav'
soundlist["zaklamp"] ='benedenzaklamp.wav'
soundlist["eindelab"] ='eindlab.wav'
soundlist["tiplab"] ='tiplab.wav'
soundlist["verbindinggerepareerd"] ='verbindingfixed.wav'
soundlist["verbindingverbreekt"] ='verbindingverbreekt.wav'
soundlist["kijkgerustrond"] ='kijkrond.wav'
soundlist["koffiehalen"] ='koffiehalen.wav'
soundlist["lokmachine"] ='lokmachine.wav'


GREY = [200,200,200]
WHITE= [255,255,255]
BLACK = [0, 0, 0]
RED = [255,0,0]


#Puzzles
puzzleList = []
puzzles = {
			"Holletje"		:	["HolletjesButtons", "HolletjesServo"],
			"Kooitjes"		:	["Kooitjes"],
			"Terrarium"		:	["Terrarium"],
			"PoepScanner"	:	["Poep"],
			"Crusher"		: 	["Crusher"],
			"Medicein"		:	["Medicein", "ColorScanner", "Kastje", "Panel"],
			"Quiz"			:	["Quiz"]}




BUTTONS = {
	"FakeESPButton" : {
		"type"			:	pg.Button,
		"location"		:	(320, 5),
		"size"			:	(100,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Fake",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		},

	"StartGameButton" : {
		"type"			:	pg.Button,
		"location"		:	(320, 5),
		"size"			:	(100,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Start",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		},

	"NextPhaseButton" : {
		"type"			:	pg.Button,
		"location"		:	(320, 5),
		"size"			:	(100,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Next",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		},

	"MainWindowButton" : {
		"type"			:	pg.Button,
		"location"		:	(320, 5),
		"size"			:	(100,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Main",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		},

	"ResetButton" : {
		"type"			:	pg.Button,
		"location"		:	(320, 5),
		"size"			:	(100,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Reset",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		},


}

DROPDOWNBUTTONS = {
	"ESPDropdownButton" : {
		"location"		:	(320, 5),
		"size"			:	(100,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"ESPS",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		},

	"PhaseDropdownButton" : {
		"location"		:	(320, 5),
		"size"			:	(100,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Phases",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		},

	"PuzzelDropdownButton" : {
		"location"		:	(320, 5),
		"size"			:	(100,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Puzzles",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		},
}

DROPDOWNITEM = {
	"location"		:	(0, 50),
	"size"			:	(80,30),
	"color"			:	WHITE,
	"visable"		:	False,
	"fontsize"		:	12,
	"textcolor"		:	BLACK,
	}

HEADER = {
	"location"		:	(0, 0),
	"size"			:	(1080, 10),
	"color"			:	BLACK,
	"visable"		:	True,
	"border"		:	2,
	"bordercolor"	:	WHITE,
	"objects"		:	["StartGameButton", 
						"MainWindowButton", 
						"ResetButton", 
						"PhaseDropdownButton", 
						"PuzzelDropdownButton",
						"ESPDropdownButton",
						"FakeESPButton"],
	"title"			:	"Header",
	"showtitle"		:	False,
}

CONTAINERS = {
	"MainContainer" : {
		"location"		:	(5, 100),
		"size"			:	(550, 400),
		"color"			:	BLACK,
		"visable"		:	True,
		"border"		:	2,
		"bordercolor"	:	WHITE,
		"objects"		:	["MainProgressTextBox", "NextPhaseButton", "GameTimerText"],
		"title"			:	"Main",
		"showtitle"		:	True,
		},

	"SubContainer" : {
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
	"MainProgressTextBox" : {
		"location"		:	(10,10),
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

TEXTOBJECTS = {
	"GameTimerText" : {
			"location"		:	(200,10),
			"size"			:	(50,50),
			"color"			:	WHITE,
			"visable"		:	True,
			"text"			:	"Time: ",
			"fontsize"		:	12,
			},
}

LABUI = {
	"KAST1BUTTON" : {
		"type"			:	pg.Button,
		"location"		:	(10, 5),
		"size"			:	(50,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Kast 1",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		"function"		:	"SendMqtt('MED','1')"
		},

	"KAST2BUTTON" : {
		"type"			:	pg.Button,
		"location"		:	(10, 70),
		"size"			:	(50, 50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Kast 2",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		"function"		:	"SendMqtt('MED','2')"
		},

	"KAST3BUTTON" : {
		"type"			:	pg.Button,
		"location"		:	(10, 130),
		"size"			:	(50,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Kast 3",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		"function"		:	"SendMqtt('MED','3')"
		},

	"KAST4BUTTON" : {
		"type"			:	pg.Button,
		"location"		:	(10, 190),
		"size"			:	(50,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Kast 4",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		"function"		:	"SendMqtt('MED','4')"
		},

	"KAST5BUTTON" : {
		"type"			:	pg.Button,
		"location"		:	(10, 260),
		"size"			:	(50,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Kast 5",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		"function"		:	"SendMqtt('MED','5')"
		},

	"KAST6BUTTON" : {
		"type"			:	pg.Button,
		"location"		:	(10, 320),
		"size"			:	(50,50),
		"color"			:	WHITE,
		"visable"		:	True,
		"text"			:	"Kast 6",
		"fontsize"		:	12,
		"textcolor"		:	BLACK,
		"function"		:	"SendMqtt('MED','6')"
		},

	"PhaseMqttTextBox" : {
		"type"			:	pg.TextBox,
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
		"type"			:	pg.Container,
		"contname"			:	"LabContainer",
		"location"		:	(5, 100),
		"size"			:	(550, 400),
		"color"			:	BLACK,
		"visable"		:	True,
		"border"		:	2,
		"bordercolor"	:	WHITE,
		"objects"		:	[
							"KAST1BUTTON",
							"KAST2BUTTON",
							"KAST3BUTTON",
							"KAST4BUTTON",
							"KAST5BUTTON",
							"KAST6BUTTON",
							"PhaseMqttTextBox",
							],
		"title"			:	"LAB",
		"showtitle"		:	True,
		},

}

#Phases
phaseList = []
phases = {	"GETIN": {"puzzles" : [], "Name": "Get in", "UI" : LABUI},
			"INTRO": {"puzzles" : [], "Name": "Intro", "UI" : LABUI},
			"A": {"puzzles":["Holletje"], "Name": "Tuin", "UI" : LABUI},
			"B": {"puzzles":["Quiz","Medicein","Crusher"], "Name": "Lab", "UI" : LABUI}}

# playButtonList = []
# def play(file):
#     winsound.PlaySound(
#         soundlist[file], winsound.SND_FILENAME | winsound.SND_ASYNC)
# def playlamb(z):
#     return lambda: play(z)


# groupA = Group("A")
# groupB = Group("B")

# pTuinA = Phase("Tuin", groupA)
# pTuinB = Phase("Tuin", groupB)

# kid1 = Kid(1)
# kid1.setGroup(groupA)

