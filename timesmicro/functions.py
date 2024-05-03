from timesmicro.commons import CL

def cableLoss(distance: int, frequency: int, rounded: bool = False) -> float | int:
    '''
    * Frequency in MHz
    * Distance in ft
    '''

    if not rounded:
        return CL(frequency, distance)
    
    return round(CL(frequency, distance),1)
    
