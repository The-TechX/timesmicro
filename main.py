import cableloss.plot2D as plt
import cableloss.functions as fnc


att = fnc.cableLoss(frequency=1500, distance=120, rounded=True)
print(att)

plt.cableLoss(distance=120)

plt.cableLossFromCSV(path='measured.csv')

plt.show()