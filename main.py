import matplotlib.pyplot as plt

x_array = ['USC', 'UCLA', 'UCI', 'Caltech', 'Stanford', 'UCSD']
y_array = [17, 18, 41, 8, 5, 36]

plt.bar(x_array, y_array, align='center', alpha=0.5)
plt.ylabel('Acceptance Rate')
plt.xlabel('University')

plt.show()