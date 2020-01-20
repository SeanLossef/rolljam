#!/usr/bin/env python

import sys
from rflib import *
from struct import *
import bitstring
import operator
import argparse
import time
import pickle

baseFreq = 313.85e6
deviation = 30e3
jamOffset = deviation * 2
baudRate = 2.99e3


print "Configuring Jammer on Frequency: " + str(baseFreq + jamOffset) + " Hz"
c = RfCat(idx=0)
c.setMdmModulation(MOD_ASK_OOK) #on of key
c.setFreq(baseFreq + jamOffset) # frequency
c.setMdmDRate(baudRate)# how long each bit is transmited for
# c.setMdmChanBW(results.chanBW)# how wide channel is
# c.setMdmChanSpc(results.chanWidth)
c.setChannel(0)
c.setMaxPower() # max power
c.lowball(1) # need inorder to read data

time.sleep(0.2) #warm up

print "Jamming...."
c.setModeTX() # start transmitting 

time.sleep(5)

c.setModeIDLE()