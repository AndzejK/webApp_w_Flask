from pathlib import Path
import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,QLabel
from PyQt6.QtWidgets import QPushButton,QLineEdit,QHBoxLayout
from PyQt6.QtCore import Qt

local_api_path=Path('./data.json')

def search_for_a_word():
    wanted_word=word.text()
    print(wanted_word)
# loop through data.json file 
    with open(local_api_path) as json_file:
        data=json.load(json_file)
    wanted_word=wanted_word.strip().lower() # strip whitespaces and make lowercase
    if wanted_word in data:
        definitions=''
        for i,definition in enumerate (data[wanted_word],start=1):
            definitions+=str(i)+". "+definition+"\n"
            message.setText(definitions)
    else:
        message.setText(f"Did not found - {wanted_word}")

# Initial set up
app=QApplication([])
window=QWidget() # all widget, button will be added in this "window"
window.setWindowTitle('Word Definition')

main_layout=QVBoxLayout()
sec_layout=QHBoxLayout()
main_layout.addLayout(sec_layout)

# Input/Enter a word
word=QLineEdit()
sec_layout.addWidget(word)

# adding another widget for a button
btn=QPushButton('Find')
sec_layout.addWidget(btn,alignment=Qt.AlignmentFlag.AlignBottom)
# connecting a button to the txt field with a slot in it in its turn is a fn
btn.clicked.connect(search_for_a_word)

# adding widget/Label as msg to inform an user what's going on
message=QLabel('')
#Givig a fixed size for label when the outcome is displayed
message.setFixedSize(800,100)
main_layout.addWidget(message)#alignment=Qt.AlignmentFlag.AlignCenter

window.setLayout(main_layout)
window.show()
app.exec()