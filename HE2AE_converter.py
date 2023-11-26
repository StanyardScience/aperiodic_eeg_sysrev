import neurodsp #aperiodic.conversions.convert_hurst_exponent
from neurodsp.aperiodic import conversions
def HE2AE(array):
    hurst = array[0] 
    array[1] = 'unknown'
    aperiodic_exponent = conversions.convert_hurst_exponent(hurst,'gaussian')
    aperiodic_exponent = abs(aperiodic_exponent)
    return aperiodic_exponent
