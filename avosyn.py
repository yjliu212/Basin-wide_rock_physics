import numpy as np
from avopp import avopp
import matplotlib.pyplot as plt

def avosyn(Z,vp,vs,d,x,ang,approx):
    """
    %Calculates synthetic AVO gather as a function of depth and angle
    %
    %input parameters:
    %  Z: depth function, with constant depth interval
    %  vp: P-wave velocity function (m/s)
    %  vs: S-wave velocity function (m/s)
    %  d: density function (g/c)
    %  vp, vs, d and Z must be same size, and have no NaN values
    %
    %  x: wavelet with 2 ms as time interval, zero phase at middle point
    %
    %  ang: vector with angles(DEG)
    %  approx: 1)Full Zoeppritz(A&R)
    %	       2)Aki&Richards
    %         3)Shuey's paper
    %         4)Castagna's paper->Shuey (slightly different formulation of Shuey)
    %Output:
    %  sd: synthetic AVO gathers in depth domain
    %  Z1: the depth function
    %
    % With no output arguments, plots figures.
    %
    % See also AVOPP, AVOPS, AVO_ABE
    %
    % written by Kevin Liu (March,2021)
    """

    dZ = Z[1]-Z[0]
    
    # The center of wavelet length
    n = np.floor(len(x) / 2).astype(int)
    
    # Calculate reflection coefficient series
    
    vp1 = vp[:-1]
    vp2 = vp[1:]
    vs1 = vs[:-1]
    vs2 = vs[1:]
    d1 = d[:-1]
    d2 = d[1:]

    R1 = avopp(vp1, vs1, d1, vp2, vs2, d2, ang, approx)
    
    print('R1 shape:',R1.shape)
    print('Z shape:',Z.shape)
    
    # Define the variables
    dt = 2  # dt = 2 ms
    T = np.arange(0, 3000, dt)  # TWT, Travel time table, dt=2 ms, same as wavelet
    
    # Calculate average velocity of each layer
    vp_avg = (vp[:-1] + vp[1:]) / 2
    
    # Calculate TWT (Two-Way Travel time) in ms
    T1 = 2 * np.cumsum(1000 * dZ / vp_avg)
    
    # Interpolate R1 to regular T axis
    
    R1T=np.zeros((len(T),len(ang)))
    for i in range(len(ang)):
        R1T[:,i]=np.interp(T, T1, R1[i,:])
    print('R1T shape:',R1T.shape)
    print('T shape:',T.shape)
    
    # Convolve R1T with wavelet
    
    s=np.zeros((len(T)+len(x)-1,len(ang)))
    for i in range(len(ang)):
        s[:,i]=np.convolve(x,R1T[:,i]) # Convolve in time, TWT
    
    st = s[n:n+len(T), :] # time domain, start from the center of wavelet length, n+1
  
    '''
    scalor=20
    
    plt.figure()
    for i in range(len(ang)):
        plt.plot(st[:,i]*scalor+5*i,T,'k')
    plt.xlabel('Angle')
    plt.ylabel('TWT (ms)')
    plt.axis([-30,40,0,2500])
    plt.gca().invert_yaxis()
    '''
    
    # Depth domain interpolation using NumPy's interpolation
    sd = np.zeros((len(T1), st.shape[1]))
    for i in range(st.shape[1]):
        sd[:, i] = np.interp(T1, T, st[:, i])
    
    # Depth axis, start from half of dZ, center of the first layer
    Z1 = Z[1:] - dZ / 2
    
    '''
    plt.figure()
    for i in range(len(ang)):
        plt.plot(sd[:,i]*scalor+5*i,Z1,'k')
    plt.xlabel('Angle')
    plt.ylabel('Depth (m)')
    plt.axis([-30,40,0,2500])
    plt.gca().invert_yaxis()
    '''
    
    return sd, Z1
