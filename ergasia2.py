import numpy as np
import matplotlib.pyplot as plt
import commlib as cl

val = input("Enter your value: ")
res = ''.join(format(ord(i), '08b') for i in val)


bitlist = [res[i:i+1] for i in range(0, len(res), 1)]


plt.close('all')
mdictionary2 = cl.pam_gray_forward_map(2)
TS = 1*1e-9

bits = np.array(bitlist)
symbolarray = cl.bits_to_symbols(bits, mdictionary2)
t, x = cl.pam_waveform2(symbolarray, TS)

cl.plot_signal(t, x, plot_type='--',figure_no=1)

mdictionary4= cl.pam_gray_forward_map(4)
TS =2*1e-9

bits = np.array(bitlist)
symbolarray = cl.bits_to_symbols(bits, mdictionary4)
t, x = cl.pam_waveform2(symbolarray, TS)

cl.plot_signal(t, x, plot_type='--',figure_no=2)

mdictionary16= cl.pam_gray_forward_map(16)
TS = 4*1e-9

bits = np.array(bitlist)
symbolarray = cl.bits_to_symbols(bits, mdictionary16)
t, x = cl.pam_waveform2(symbolarray, TS)

cl.plot_signal(t, x, plot_type='--',figure_no=3)

