import numpy as np
import matplotlib.pyplot as plt

def avopp(vp1, vs1, d1, vp2, vs2, d2, ang, approx):
    # Convert angles from degrees to radians
    t = np.radians(ang)
    #print('t:',t)
    t = t[:, np.newaxis] 
    #print('new t:',t)
    p = np.sin(t) / vp1
    ct = np.cos(t)
    
    # Average and difference values
    da = (d1 + d2) / 2
    Dd = d2 - d1
    vpa = (vp1 + vp2) / 2
    Dvp = vp2 - vp1
    vsa = (vs1 + vs2) / 2
    Dvs = vs2 - vs1
    
    if approx == 1:
        # FULL Zoeppritz (A&K)
        ct2 = np.sqrt(1 - (np.sin(t)**2 * (vp2**2 / vp1**2)))
        cj1 = np.sqrt(1 - (np.sin(t)**2 * (vs1**2 / vp1**2)))
        cj2 = np.sqrt(1 - (np.sin(t)**2 * (vs2**2 / vp1**2)))
        a = (d2 * (1 - (2 * vs2**2 * p**2))) - (d1 * (1 - (2 * vs1**2 * p**2)))
        b = (d2 * (1 - (2 * vs2**2 * p**2))) + (2 * d1 * vs1**2 * p**2)
        c = (d1 * (1 - (2 * vs1**2 * p**2))) + (2 * d2 * vs2**2 * p**2)
        d = 2 * ((d2 * vs2**2) - (d1 * vs1**2))
        E = (b * ct / vp1) + (c * ct2 / vp2)
        F = (b * cj1 / vs1) + (c * cj2 / vs2)
        G = a - (d * ct * cj2 / (vp1 * vs2))
        H = a - (d * ct2 * cj1 / (vp2 * vs1))
        D = (E * F) + (G * H * p**2)
        Rpp = (((b * ct / vp1) - (c * ct2 / vp2)) * F - (a + (d * ct * cj2 / (vp1 * vs2))) * H * p**2) / D
    
    elif approx == 2:
        # Aki & Richard (approx)
        Rpp = (0.5 * (1 - (4 * p**2 * vsa**2)) * Dd / da) + (Dvp / (2 * ct**2 * vpa)) - (4 * p**2 * vsa * Dvs)
    
    elif approx == 3:
        # Shuey
        poi1 = ((0.5 * (vp1 / vs1)**2) - 1) / ((vp1 / vs1)**2 - 1)
        poi2 = ((0.5 * (vp2 / vs2)**2) - 1) / ((vp2 / vs2)**2 - 1)
        poia = (poi1 + poi2) / 2
        Dpoi = poi2 - poi1
        Ro = 0.5 * ((Dvp / vpa) + (Dd / da))
        Bx = (Dvp / vpa) / ((Dvp / vpa) + (Dd / da))
        Ax = Bx - (2 * (1 + Bx) * (1 - 2 * poia) / (1 - poia))
        Rpp = Ro + (((Ax * Ro) + (Dpoi / (1 - poia)**2)) * np.sin(t)**2) + (0.5 * Dvp * (np.tan(t)**2 - np.sin(t)**2) / vpa)
    
    elif approx == 4:
        # Shuey linear
        A = 0.5 * ((Dvp / vpa) + (Dd / da))
        B = (-2 * vsa**2 * Dd / (vpa**2 * da)) + (0.5 * Dvp / vpa) - (4 * vsa * Dvs / (vpa**2))
        Rpp = A + (B * np.sin(t)**2)
    
    else:
        Rpp = None
        
    return Rpp
