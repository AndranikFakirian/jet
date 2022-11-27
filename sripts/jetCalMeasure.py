import spidev
#4.4 cm = 800 steps
import  jetFunctions as jf

try:
    spi = spidev.SpiDev()
    jf.initSpiAdc()
    sample=jf.getMeanAdc(1000)
    jf.save(sample, 1)
finally:
    jf.deinitSpiAdc()