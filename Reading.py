
def read_and_smooth(name):
    import pandas as pd
    import numpy as np
    from scipy.signal import savgol_filter
    
    woof = pd.read_csv(name, sep=",")
    
    time = [i for i in woof["Time"]]
    time.pop(0)
    for i in range(0, len(time)):
        time[i] = float(time[i])
        
    volt1 = [i for i in woof["Channel A"]]
    volt1.pop(0)
    for i in range(0, len(volt1)):
        volt1[i] = float(volt1[i])
        
    volt2= [i for i in woof["Channel B"]]
    volt2.pop(0)
    for i in range(0, len(volt2)):
        volt2[i] = float(volt2[i])
        
    red_smooth = savgol_filter(volt1, 51, 3)
    blue_smooth = savgol_filter(volt2, 51, 3)
    
    red_ready = []
    blue_ready = []

    for i in red_smooth:
        temp = i - np.mean(red_smooth)
        red_ready.append(temp)


    for i in blue_smooth:
        temp = i - np.mean(blue_smooth)
        blue_ready.append(temp)
        
    return time, red_ready, blue_ready
    
    
    
def our_lord_and_saviour_fourier(time, name):
    import numpy as np
    
    fy = np.fft.fft(name)
    dt = time[1] - time[0]
    n = len(time)
    freqs = np.fft.fftfreq(n, d=dt) # Frequencies associated with each samples
    
    return fy, np.fft.fftshift(freqs), np.fft.fftshift(abs(fy))