import PygameUI as pg
from vrijstaatConst import *
GREY = [200,200,200]
WHITE= [255,255,255]
BLACK = [0, 0, 0]
RED = [255,0,0]

ESPDict = {
	"HolletjesButtons"	: {
		"topic"		:	"TUIN/HOL/BUTTONS",
		"sign"		:	"HolletjesButton",
		"outputs"	:	{
							"HOLB1": {
								"fromobject"	:	TEMPLATE["SmallButton"],
								"text"			:	"1",
								"function"		:	"SendMqtt('TUIN/HOL/BUTTONS','a1')",
							},
							"HOLB2" : {
								"fromobject"	:	TEMPLATE["SmallToggleButton"],
								"text"			:	"2",
								"function"		:	"SendMqtt('TUIN/HOL/BUTTONS','a3')",
								"offfunction"	:	"SendMqtt('TUIN/HOL/BUTTONS','a4')",
							},
							"HOLB3" : {
								"fromobject"	:	TEMPLATE["SmallToggleButton"],
								"text"			:	"3",
								"function"		:	"SendMqtt('TUIN/HOL/BUTTONS','a5')",
								"offfunction"	:	"SendMqtt('TUIN/HOL/BUTTONS','a6')",
							},
							"HOLB4" : {
								"fromobject"	:	TEMPLATE["SmallToggleButton"],
								"text"			:	"4",
								"function"		:	"SendMqtt('TUIN/HOL/BUTTONS','a7')",
								"offfunction"	:	"SendMqtt('TUIN/HOL/BUTTONS','a8')",
							},
							"HOLB5" : {
								"fromobject"	:	TEMPLATE["SmallToggleButton"],
								"text"			:	"5",
								"function"		:	"SendMqtt('TUIN/HOL/BUTTONS','a9')",
								"offfunction"	:	"SendMqtt('TUIN/HOL/BUTTONS','a0')",
							},


						},
		},

	"HolletjesServo"	: {
		"topic"	:	"TUIN/HOL/#",
		"sign"	:	"HolletjesServo",
		"inputs":	{},
		},

	"MusicPlayer"		: {
		"topic"	:	"MusicPlayer",
		"sign"	:	"MusicPlayer1",
		"outputs":	{
					"M1" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"1",
						"function"		:	"SendMqtt('IntroVideo','text1.mp3')"
						},
					"M2" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"2",
						"function"		:	"SendMqtt('MusicPlayer','2')"
						},
					"M3" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"3",
						"function"		:	"SendMqtt('MusicPlayer','3')"
						},
					"M4" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"4",
						"function"		:	"SendMqtt('MusicPlayer','4')"
						},
					"M5" : {
						"fromobject"	:	TEMPLATE["SmallButton"],
						"text"			:	"5",
						"function"		:	"SendMqtt('MusicPlayer','5')"
						},
					},
		},	

	"MediceinKast"		: {
		"topic"	:	"LAB/MEDKAST",
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
	"LabBerry"			: {
		"topic"	:	"LAB/LABBERRY/#",
		"sign"	:	"LabBerry",
		"outputs":	{
					"Panel1" : {
						"fromobject"	:	TEMPLATE["SmallToggleButton"],
						"text"			:	"Next State",
						"function"		:	"SendMqtt('MED','1')",
						"offfunction"	:	"SendMqtt('MED','1')",
						},
					},
		},

	"LampLabTL"			: {
		"topic"	:	"LAB/RELAIS/TL",
		"sign"	:	"LampLabTL",
		"outputs":	{
					"LabTLRelais" : {
						"fromobject"	:	TEMPLATE["SmallToggleButton"],
						"text"			:	"TL",
						"function"		:	"SendMqtt('LAB/RELAIS/TL','1')",
						"offfunction"	:	"SendMqtt('LAB/RELAIS/TL','0')",
						},
					},
		},

	"LampLabPuzzel"			: {
		"topic"	:	"LAB/RELAIS/PUZZEL",
		"sign"	:	"LampLabPuzzels",
		"outputs":	{
					"LabTLPuz" : {
						"fromobject"	:	TEMPLATE["SmallToggleButton"],
						"text"			:	"PuzLight",
						"function"		:	"SendMqtt('LAB/RELAIS/PUZZEL','1')",
						"offfunction"	:	"SendMqtt('LAB/RELAIS/PUZZEL','0')",
						},
					},
		},

	"LabKey"			: {
		"topic"	:	"LAB/labkey",
		"sign"	:	"LABKEY",
		"outputs":	{
					"LabTLPuz" : {
						"fromobject"	:	TEMPLATE["SmallToggleButton"],
						"text"			:	"Open",
						"function"		:	"SendMqtt('LAB/labkey','a1')",
						"offfunction"	:	"SendMqtt('LAB/labkey','a2')",
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
	"Crusher"		: {
		"topic"	:	"LAB/CRUSHER/#",
		"sign"	:	"Crusher",
		"outputs":	{
					"B1" : {
						"fromobject"	:	TEMPLATE["SmallToggleButton"],
						"type"			:	pg.ToggleButton,
						"text"			:	"B1",
						"function"		:	"SendMqtt('LAB/CRUSHER/b1','1')",
						"offfunction"	:	"SendMqtt('LAB/CRUSHER/b1','0')",
						},
					"B2" : {
						"fromobject"	:	TEMPLATE["SmallToggleButton"],
						"type"			:	pg.ToggleButton,
						"text"			:	"B2",
						"function"		:	"SendMqtt('LAB/CRUSHER/b2','1')",
						"offfunction"	:	"SendMqtt('LAB/CRUSHER/b2','0')",
						},
					"T1" : {
						"fromobject"	:	TEMPLATE["SmallToggleButton"],
						"type"			:	pg.ToggleButton,
						"text"			:	"T1",
						"function"		:	"SendMqtt('LAB/CRUSHER/t1','1')",
						"offfunction"	:	"SendMqtt('LAB/CRUSHER/t1','0')",						},
					"T2" : {
						"fromobject"	:	TEMPLATE["SmallToggleButton"],
						"type"			:	pg.ToggleButton,
						"text"			:	"T2",
						"function"		:	"SendMqtt('LAB/CRUSHER/t2','1')",
						"offfunction"	:	"SendMqtt('LAB/CRUSHER/t2','0')",
						},
					"kr" : {
						"fromobject"	:	TEMPLATE["SmallToggleButton"],
						"type"			:	pg.ToggleButton,
						"text"			:	"kr",
						"function"		:	"SendMqtt('LAB/CRUSHER/kr','1')",
						"offfunction"	:	"SendMqtt('LAB/CRUSHER/kr','0')",
						},
					"kl" : {
						"fromobject"	:	TEMPLATE["SmallToggleButton"],
						"type"			:	pg.ToggleButton,
						"text"			:	"kl",
						"function"		:	"SendMqtt('LAB/CRUSHER/kl','1')",
						"offfunction"	:	"SendMqtt('LAB/CRUSHER/kl','0')",
						},	
					},
		},
	}