''' Link Video Youtube  : https://youtu.be/8JGQStmW3xU 
    Link Github         : https://github.com/bayuwira/AmplitudeModulation
'''


from tkinter import * #GUI
from pygame import mixer #load audio, play audio
import numpy as np
from scipy.io.wavfile import write #membuat wavfile dari signal
import matplotlib.pyplot as plt


def modulated():
    framerate = 44100
    t = np.linspace(0, 1, framerate) #titik sampel

    carrier_Hz = float(entryCarrier.get())
    message_Hz = float(entryMessage.get())
    amplitude_carrier = float(entryCarrierAmp.get())
    amplitude_massage = float(entryMessageAmp.get())

    modulation_index = amplitude_massage / amplitude_carrier

    carrier = amplitude_carrier * np.cos(2 * np.pi * carrier_Hz * t)
    message = amplitude_massage * np.cos(2 * np.pi * message_Hz * t)

    modulated = (amplitude_carrier * (1.0 + modulation_index * message)) * carrier

    carrier_signal = np.int16(carrier * 32767)
    message_signal = np.int16(message * 32767)
    modulated_signal = np.int16(modulated * 32767)

    write('sine.wav', framerate, carrier_signal)
    write('message.wav', framerate, message_signal)
    write('modulated.wav', framerate, modulated_signal)

    plt.subplot(3, 1, 1)
    plt.plot(carrier, 'g')
    plt.xlim(0, int(entryxlimit.get()))
    plt.ylabel('Amplitude')
    plt.xlabel('Carrier signal ' + entryCarrier.get() + 'Hz, Amp : ' + entryCarrierAmp.get())

    plt.subplot(3, 1, 2)
    plt.plot(message, 'b')
    plt.ylabel('Amplitude')
    plt.xlabel('message signal ' + entryMessage.get() + 'Hz, Amp : ' + entryMessageAmp.get())
    plt.xlim(0, int(entryxlimit.get()))

    plt.subplot(3, 1, 3)
    plt.plot(modulated, 'r')
    plt.ylabel('Amplitude')
    plt.xlabel('Modulated signal')
    plt.xlim(0, int(entryxlimit.get()))

    plt.subplots_adjust(hspace=2)
    plt.rc('font', size=15)
    plt.show()

def playCarrier():
    mixer.music.load('sine.wav')
    mixer.music.play()

def playmessage():
    mixer.music.load('message.wav')
    mixer.music.play()

def playModulated():
    mixer.music.load('modulated.wav')
    mixer.music.play()

def stopWav():
    mixer.music.stop()

root = Tk()
root.title('AM Modulation')
root.geometry('300x350')
mixer.init()

entryCarrier = Entry(root, width=5, border=5)
labelCarrier = Label(root, text='F Carrier (Hz)')
labelCarrier.grid(row=0, sticky='W')
entryCarrier.grid(row=0, column=1)

entryMessage = Entry(root, width=5, border=5)
labelMessage = Label(root, text='F message (Hz)')
labelMessage.grid(row=1, sticky='W')
entryMessage.grid(row=1, column=1)

entryCarrierAmp = Entry(root, width=5, border=5)
labelCarrierAmp = Label(root, text='Carrier Amplitude')
labelCarrierAmp.grid(row=2, sticky='W')
entryCarrierAmp.grid(row=2, column=1)

entryMessageAmp = Entry(root, width=5, border=5)
labelMessageAmp = Label(root, text='message Amplitude')
labelMessageAmp.grid(row=3, sticky='W')
entryMessageAmp.grid(row=3, column=1)

entryxlimit = Entry(root, width=5, border=5)
labelxlimit = Label(root, text='xlimit')
labelxlimit.grid(row=4, sticky='W')
entryxlimit.grid(row=4, column=1)


plotButton = Button(root, text='Plot & Calculate', command=modulated).grid(row=5, sticky='W', padx=5, pady=5)
playCarrier = Button(root, text='play Carrier', command=playCarrier).grid(row=6, sticky='W', padx=5, pady=5)
playmessage = Button(root, text='play message', command=playmessage).grid(row=7, sticky='W', padx=5, pady=5)
playModulated = Button(root, text='play Modulated', command=playModulated).grid(row=8, sticky='W', padx=5, pady=5)
stopButton = Button(root, text='stop', command=stopWav).grid(row=9, sticky='W', padx=5, pady=5)


root.mainloop()
