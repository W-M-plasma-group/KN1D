# Make_dVr_dVx
#   Constructs velocity space differentials for distrobution functions 
# used by Kinetic_Neutrals, Kinetic_H2, Kinetic_H, and other related
# procedures 
#
# Gwendolyn Galleher 

import numpy as np

def Make_dVr_dVx(Vr, Vx): # For this to work inputs must be np arrays so I might need to ammend this later to make sure all inputs are arrays

    # Determine velocity space differentials 
    nVr = np.size(Vr)
    nVx = np.size(Vx)

    # for Vr first 
    _Vr = [Vr, 2 * Vr[nVr-1] - Vr[nVr-2]]  # this is an array and Vr(nVr-1) is calling the last cell of Vr
    Vr_mid = [0.0, 0.5 * (_Vr + np.roll(_Vr, -1))]
    
    VrR = np.roll(Vr_mid, -1)
    VrL = Vr_mid

    Vr2pidVr = np.pi * ((VrR ** 2) - (VrL ** 2))
    Vr2pidVr = Vr2pidVr[0 : nVr - 1]  # makes it the same length as Vr 

    VrVr4pidVr = (4/3) * np.pi * ((VrR ** 3) - (VrL ** 3))
    VrVr4pidVr = VrVr4pidVr[0 : nVr - 1]
    VrR = VrR[0 : nVr - 1]
    VrL = VrL[0 : nVr - 1]

    # now for Vx
    _Vx = [2 * Vx[0] - Vx[1], Vx, 2 * Vx[nVx - 1] - Vx[nVx - 2]]
    VxR = 0.5 * (np.roll(_Vx, -1) + _Vx)
    VxL = 0.5 * (np.roll(_Vx, 1) + _Vx)
    dVx = VxR[1: nVx] - VxL[1:nVx]
    VxR = VxR[1: nVx]
    VxL = VxL[1 : nVx]

    # compute volume elements 
    vol = np.zeros((nVr, nVx), float)
    for i in range(0, nVr - 1):
        vol[i, np.size(vol) - 1] = Vr2pidVr * dVx

    #compute DeltaVx, DeltaVr
    DeltaVx = VxR - VxL
    DeltaVr = VrR - VrL

    # compute vth_Deltavx, vx_Deltavx, vr_Deltavr, padded with zeros
    Vth_DeltaVx = np.array((nVr + 2, nVr + 2), float)
    Vx_DeltaVx = np.array((nVx + 2, nVx + 2), float)
    Vr_DeltaVr = np.array((nVr + 2, nVr + 2), float)
    for i in range(1, nVr):
        Vth_DeltaVx[i, 1 : nVx] = 1.0/DeltaVx
        Vx_DeltaVx[i, 1 : nVx] = Vx/DeltaVx
    for j in range(1, nVx):
        Vr_DeltaVr[1 : nVr, j] = Vr/DeltaVr
    
    #compute v^2
    Vr2Vx2 = np.zeros((nVr, nVx), float)
    for i in range(0, nVr - 1):
        Vr2Vx2[i : np.size(Vr2Vx2)] = (Vr[i] ** 2) + (Vx ** 2)

    # Determine indice range of positive and negative Vx 
    jp = np.argwhere(Vx > 0)
    jpa = jp[0]; jpb = jp[np.size(jp) - 1]
    jn = np.argwhere(Vx < 0)
    jna = jn[0]; jnb = jn[np.size(jn) - 1]

    return
