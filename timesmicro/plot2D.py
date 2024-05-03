import matplotlib.pyplot as plt
import numpy as np

from timesmicro.commons import CL


def cableLoss(
        distance: int, 
        start_frequency: int = 1000, 
        stop_frequency: int = 2000,
        color: str = 'blue'
        ) -> None:
    '''
    Plot a graph of the ideal cable loss for a cable run lenght.
    By default uses L-BAND.
    * Distance in ft
    * Satart frequency in MHz
    * Stop frequency in MHz
    '''

    frequencies = np.linspace(start_frequency, stop_frequency, 20)
    attenuations = CL(frequencies, distance)

    plt.plot(frequencies, attenuations, linewidth=1, color=color)
    plt.ylim(30, 0)
    plt.xlim(start_frequency, stop_frequency)
    plt.yticks(np.arange(0, 30, 3))
    plt.xticks(np.arange(start_frequency, stop_frequency + 100, 100))
    plt.grid()


def cableLossFromCSV(
        path: str, 
        start_frequency: int = 1000,
        stop_frequency: int = 2000,
        color: str = 'red'
        ) -> None:
    
    '''
    Plot a graph of a dataset csv file.
    By default uses L-BAND.
    * Distance in ft
    * Satart frequency in MHz
    * Stop frequency in MHz
    '''
    
    # Specify the path to the CSV file
    csv_file_path = 'measured.csv'
    
    # Use genfromtxt to read the CSV file into a NumPy array
    data_array = np.genfromtxt(csv_file_path, delimiter=',')

    feq: np.array = []
    att: np.array = []

    for _ in data_array:
        feq.append(_[0])
        att.append(_[1])

    plt.plot(feq, att, label='measured', linewidth = 1, color=color)
    plt.ylim(30, 0)
    plt.xlim(start_frequency, stop_frequency)
    plt.yticks(np.arange(0, 30, 3))
    plt.xticks(np.arange(start_frequency, stop_frequency + 100, 100))
    plt.grid()


def show() -> None:
    '''
    Show plot or plots using matplotlib.pyplot.show() method.
    '''
    plt.show()
