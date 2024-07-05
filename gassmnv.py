import numpy as np

def gassmnv(vp1, vs1, ro1, rofl1, kfl1, rofl2, kfl2, k0, phi):
    """
    Gassmann fluid substitution with velocities as input/outputs.
    
    Parameters:
    vp1, vs1, ro1: rock Vp, Vs, and density with fluid 1
    rofl1, kfl1:   density and bulk modulus of initial fluid
    rofl2, kfl2:   density and bulk modulus of new fluid
    k0, phi:       mineral bulk modulus, and rock porosity
    
    Returns:
    vp2, vs2, ro2, k2: Vp, Vs, density, and bulk modulus of rock with new fluid
    
    Note: Giving vs1=0, and mineral P-wave modulus in place of k0 does approximate 
    Gassmann calculation.
    """
    
    ro2 = ro1 - phi * rofl1 + phi * rofl2
    mu1 = ro1 * vs1**2
    k1 = ro1 * vp1**2 - (4/3) * mu1
    a = k1 / (k0 - k1) - kfl1 / (phi * (k0 - kfl1)) + kfl2 / (phi * (k0 - kfl2))
    k2 = k0 * a / (1 + a)
    mu2 = mu1
    vp2 = np.sqrt((k2 + (4/3) * mu2) / ro2)
    vs2 = np.sqrt(mu2 / ro2)
    
    return vp2, vs2, ro2, k2

# Example usage:
# vp2, vs2, ro2, k2 = gassmnv(vp1, vs1, ro1, rofl1, kfl1, rofl2, kfl2, k0, phi)
