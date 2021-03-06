import numpy as np
import scipy 
from create_jh_bscoef import Create_JH_BSCoef

# Evaluates the alpha coefficients 
# - the comment on the original file seemed to be wrong so I will probaly have to expand on this later
def JHAlpha_coef(Density, Te,  create = 0, no_null = 0):
    # these are the variables that will be called from the classes for now I am defining them at the top. 
    # They are not defined as there actual values because the actual values used are defined in other files.
    Dknot = None
    Tknot = None
    LogR_BSCoef=None
    LogS_BSCoef=None
    LogAlpha_BSCoef=None
    A_Lyman=None
    A_Balmer=None
    if create:
        Create_JH_BSCoef()
    if LogR_BSCoef is None:
        # this is where old data is restored I don't entirely know how we want to do this yet or if we are doing this at all 
        pass 

    # Evaluate Alpha coefficients 
    if np.size(Density) != np.size(Te):
        raise Exception('Number of elements of Density and Te are different!')
    result = Density ; result[:] = 1.0e32
    LDensity = np.log(Density)
    LTe = np.log(Te)
    if no_null:
        LDensity = np.maximum(LDensity, min(Dknot))
        LDensity = np.minimum(LDensity, max(Dknot))
        LTe = np.maximum(LTe, min(Tknot))
        LTe = np.minimum(LTe, max(Tknot))
        count = np.size(LDensity)
        ok = np.arange(count)
    else:
        for i in range(0, len(Density)):
            if min(Dknot) < LDensity[i] < max(Dknot) and min(Tknot) < LTe[i] < max(Tknot):
                ok = np.append(ok, i)
    count = np.size(ok)
    ok = ok.astype(int) 
    if count > 0: 
        result[ok] = np.exp( ) # currently missing the python equivalent to bs2dr will come back to this later 
    return result
