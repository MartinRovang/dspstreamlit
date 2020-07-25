import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as dsp
plt.style.use('seaborn-deep')


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Original', 'Lowpass', 'Highpass')
)

fs = 100
t = np.arange(0, 10, 1/fs)
chrp = dsp.chirp(t, 10, 10, 45)

# @st.cache(suppress_st_warning=True)
def main():

    if add_selectbox == 'Lowpass':
        N = int(st.slider('Select butterfilter order', min_value = 0, max_value = 10))
        system = dsp.butter(N, 25, fs = fs)
        lp_filtered = dsp.lfilter(*system, chrp)
        ww, gd = dsp.group_delay(system, fs = fs)
        fig, ax = plt.subplots(2, 1, figsize = [12, 9])
        ax[0].plot(t, lp_filtered)
        ax[0].set_title('Lowpass filtered')
        ax[0].set_xlabel('Time')
        ax[0].set_ylabel('Amplitude')
        ax[1].plot(ww, gd)
        ax[1].set_title('Filter group delay')
        ax[1].set_xlabel('Frequency')
        ax[1].set_ylabel('Delay samples')
        plt.tight_layout()
        st.pyplot()

    if add_selectbox == 'Highpass':
        N = int(st.slider('Select butterfilter order', min_value = 0, max_value = 10))
        system = dsp.butter(N, 25, btype = 'high', fs = fs)
        hp_filtered = dsp.lfilter(*system, chrp)
        ww, gd = dsp.group_delay(system, fs = fs)
        fig, ax = plt.subplots(2, 1, figsize = [12, 9])
        ax[0].plot(t, hp_filtered)
        ax[0].set_title('Lowpass filtered')
        ax[0].set_xlabel('Time')
        ax[0].set_ylabel('Amplitude')
        ax[1].plot(ww, gd)
        ax[1].set_title('Filter group delay')
        ax[1].set_xlabel('Frequency')
        ax[1].set_ylabel('Delay samples')
        plt.tight_layout()
        st.pyplot()

    if add_selectbox == 'Original':
        plt.plot(t, chrp)
        plt.title('Chirp')
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        st.pyplot()

if __name__ == "__main__":
    main()