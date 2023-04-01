# PyQT allaws us to create the Desktop apps

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel,QPushButton,QLineEdit

# Creating a function for a slot
def make_sentence():
    input_text=text.text()
    output_label.setText(input_text.capitalize())

app=QApplication([]) # we need to have some argument and default one empty list
window=QWidget()
window.setWindowTitle("Sentence Maker"+'!')

# get that field where I can enter a txt
layout=QVBoxLayout() # V - vertical

# Input
text=QLineEdit()
layout.addWidget(text)

# adding another widget for a button
btn=QPushButton('Do magic!')
layout.addWidget(btn)
# connecting a button to the txt field with a slot in it in its turn is a fn
btn.clicked.connect(make_sentence)

# adding another label/widget/filed to display the outcome
output_label=QLabel('')
layout.addWidget(output_label)


# Display that enetered txt
window.setLayout(layout)
window.show()
app.exec()
