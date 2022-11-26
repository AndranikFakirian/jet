import spidev
#4.4 cm = 800 steps
#550
import  jetFunctions as jf

try:
    spi = spidev.SpiDev()
    jf.initSpiAdc()
    samples=[]
    jf.initStepMotorGpio()
    for i in range(0, 109):
        samples.append(jf.getAdc())
        jf.stepForward(10)
    jf.save(samples, 109)
finally:
    jf.stepBackward(1090)
    jf.deinitSpiAdc()