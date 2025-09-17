from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(15))
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

tones = {
"B0": 31,
"C1": 33,
"CS1": 35,
"D1": 37,
"DS1": 39,
"E1": 41,
"F1": 44,
"FS1": 46,
"G1": 49,
"GS1": 52,
"A1": 55,
"AS1": 58,
"B1": 62,
"C2": 65,
"CS2": 69,
"D2": 73,
"DS2": 78,
"E2": 82,
"F2": 87,
"FS2": 93,
"G2": 98,
"GS2": 104,
"A2": 110,
"AS2": 117,
"B2": 123,
"C3": 131,
"CS3": 139,
"D3": 147,
"DS3": 156,
"E3": 165,
"F3": 175,
"FS3": 185,
"G3": 196,
"GS3": 208,
"A3": 220,
"AS3": 233,
"B3": 247,
"C4": 262,
"CS4": 277,
"D4": 294,
"DS4": 311,
"E4": 330,
"F4": 349,
"FS4": 370,
"G4": 392,
"GS4": 415,
"A4": 440,
"AS4": 466,
"B4": 494,
"C5": 523,
"CS5": 554,
"D5": 587,
"DS5": 622,
"E5": 659,
"F5": 698,
"FS5": 740,
"G5": 784,
"GS5": 831,
"A5": 880,
"AS5": 932,
"B5": 988,
"C6": 1047,
"CS6": 1109,
"D6": 1175,
"DS6": 1245,
"E6": 1319,
"F6": 1397,
"FS6": 1480,
"G6": 1568,
"GS6": 1661,
"A6": 1760,
"AS6": 1865,
"B6": 1976,
"C7": 2093,
"CS7": 2217,
"D7": 2349,
"DS7": 2489,
"E7": 2637,
"F7": 2794,
"FS7": 2960,
"G7": 3136,
"GS7": 3322,
"A7": 3520,
"AS7": 3729,
"B7": 3951,
"C8": 4186,
"CS8": 4435,
"D8": 4699,
"DS8": 4978
}

bpms = {
    "GF": 145,
    "RR": 112
    }

bpm = bpms["GF"]

wn = 240/bpm
hn = 120/bpm
qn = 60/bpm
en = 30/bpm
sxn = 15/bpm

tqn = (qn/3) * 2
ten = (en/3) * 2
tsxn = (sxn/3) * 2

hnd = (hn/2) + hn
qnd = (qn/2) + qn
end = (en/2) + en
sxnd = (sxn/2) + sxn

wr = wn
hr = hn
qr = qn
er = en
stop = 0.01

song = ["E5","G5","A5","P","E5","G5","B5","A5","P","E5","G5","A5","P","G5","E5"]

gravity_falls = ["F5", "D5", "A4",
                 "D5", "F5", "D5", "A4",
                 "D5", "F5", "C5", "A4",
                 "C5", "F5", "C5", "A4",
                 "C5", "E5", "CS5", "A4",
                 "CS5", "E5", "CS5", "A4",
                 "CS5", "E5", "CS5", "A4",
                 "CS5", "E5", "CS5", "A5",
                 "D5", "E5", "F5", "A5", "G5", "A5", "C5",
                 "D5", "E5", "F5", "E5", "G5", "A5", "G5", "F5", "S",
                 "F5", "S", "F5", "S", "F5", "A5", "S", "A5", "G5", "F5", "S",
                 "A5", "S", "A5", "S", "A5", "G5", "A5", "G5", "F5", "S",
                 "F5", "S", "F5", "S", "F5", "A5", "S", "A5", "G5", "F5",
                 "A5", "S", "A5", "S", "A5", "CS6", "S", "CS6", "S", "CS6",
                 "F5", "S", "F5", "S", "F5", "A5", "S", "A5", "G5", "F5",
                 "AS5", "S", "AS5", "S", "AS5", "G5", "C6", "A5", "CS6",
                 "D4", "A4", "F4","C5", "C4", "C5", "E5", "C5", "D5", "CS4", "D6"]

gravity_falls_time = [en, en, en,
                      en, en, en, en,
                      en, en, en, en,
                      en, en, en, en,
                      en, en, en, en,
                      en, en, en, en,
                      en, en, en, en,
                      en, en, en, qn,
                      hn, qn, hn, qnd, qnd, qn, hnd,
                      hn, qn, qnd, qnd, qnd, qnd, qnd, qnd, stop,
                      end, stop, end, stop, end, end, stop, end, end, qnd, stop,
                      end, stop, end, stop, end, end, end, end, qnd, stop,
                      end, stop, end, stop, end, end, stop, end, end, qnd,
                      end, stop, end, stop, qn, end, stop, end, stop, qn,
                      end, stop, end, stop, end, end, stop, end, end, qnd,
                      end, stop, end, stop, end, qnd, qnd, qnd, qnd,
                      en, en, en, en, en, en, en, en, end, end, en
                      ]

megalovania = ["D4", "P", "D4", "D5", "A4", "GS4", "G4", "F4", "D4", "F4", "G4"]

rick_roll = ["F5", "G5", "C5", "G5", "A5",
             "C6", "AS5", "A5", "F5", "G5", "C5", "S",
             "D5", "E5", "F5", "S", "F5", "G5", "E5", "D5", "C5", "S",
             "D5", "S", "D5", "E5", "F5", "D5","C5", "C6", "S", "C6", "G5"
             ]
rick_roll_time = [qnd, qnd, qn, qnd, qnd,
                  sxn, sxn, sxn, qnd, qnd, wn, stop,
                  en, en, en, stop, en, en, end, en, wn, stop,
                  en, stop, en, en, en, end, sxnd, end, stop, sxn,wn
                  ]

def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)

def playsong(mysong, timesig):
    for i in range(len(mysong)):
        if mysong[i] == "P":
            bequiet()
        elif mysong[i] == "S":
            bequiet()
            sleep(timesig[i])              
        else:
            playtone(tones[mysong[i]])
            sleep(timesig[i])
    bequiet()

while True:
    if button.value():      
        playsong(gravity_falls, gravity_falls_time)
