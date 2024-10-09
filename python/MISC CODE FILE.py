import matplotlib.pyplot as plt

# Define the disciplines and their contributions
disciplines = ['Cybersecurity', 'Law', 'Ethics']
contributions = [30, 35, 25]  # Example percentages for contribution to the integrated perspective

# Create a pie chart to represent the integration of disciplines
plt.figure(figsize=(7,7))
plt.pie(contributions, labels=disciplines, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Integration of Disciplines in Privacy Research (Cybersecurity, Law, Ethics)')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.show()
