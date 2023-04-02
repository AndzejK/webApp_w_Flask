from pathlib import Path
import json
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,QLabel
from PyQt6.QtWidgets import QPushButton,QLineEdit,QHBoxLayout
from PyQt6.QtCore import Qt

local_api_path=Path('./data.json')

def search_for_a_word(word):
    wanted_word=word.text()
# loop through data.json file 
    with open(local_api_path) as json_file:
        data=json.load(json_file)
    wanted_word=wanted_word.strip().lower() # strip whitespaces and make lowercase
    if wanted_word in data:
        print('# '+wanted_word.title())
        for i,definition in enumerate (data[wanted_word],start=1):
            print(f"{i}. {definition}")
            print(message.setText(wanted_word))
    else:
        print(f"Did not found - {wanted_word}")

# Initial set up
app=QApplication([])
window=QWidget() # all widget, button will be added in this "window"
window.setWindowTitle('Word Definition')

main_layout=QHBoxLayout()

# Input/Enter a word
text=QLineEdit()
main_layout.addWidget(text)

# adding another widget for a button
btn=QPushButton('Find')
main_layout.addWidget(btn)
# connecting a button to the txt field with a slot in it in its turn is a fn
btn.clicked.connect(search_for_a_word)

# adding another label/widget/filed to display the outcome
result_as_def=QLabel('')
main_layout.addWidget(result_as_def)


# adding widget/Label as msg to inform an user what's going on
message=QLabel('test')
main_layout.addWidget(message,alignment=Qt.AlignmentFlag.AlignCenter)



window.setLayout(main_layout)
window.show()
app.exec()