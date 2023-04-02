from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,QLabel
from PyQt6.QtWidgets import QPushButton, QFileDialog # search for files in OS
from PyQt6.QtCore import Qt
from pathlib import Path # dealing with path on OS

# Initial set up
app=QApplication([])
window=QWidget() # all widget, button will be added in this "window"
window.setWindowTitle('File Destroyer')


# Functions / Slots
    # Open the files and displays file's path - open_btn
def open_files():
    # not good practice but we declare this variably globally, meaning it can be accessed form everywhere
    global filenames 
    print('Searching has started...')
    # we have a list of paths which are strings
    filenames, _ = QFileDialog.getOpenFileNames(window, "Select files")
    # we save the path to message var but it'll be list, once we use .join() it takes a string and adds the value from the list and converts into str
    message.setText('\n'.join(filenames))
    print(message)
    # this button destroy_btn actually deletes fiels
def destroy_files():
    for filename in filenames:
        # we convert path string into Path 
        path=Path(filename)
        # open a file 
        with open(path,'wb') as file:
            # write binary and saves and closes file
            file.write(b'')
        # once it's closed file is deleted
        path.unlink()
    message.setText('Destruction Successful!')
    print(message)
main_layout=QVBoxLayout()
# widget as description of the app
description=QLabel('Choose the files you want to destroy. The files will be <font color="red">permanetly</font> deleted!')
# adding this widget to the main layout
main_layout.addWidget(description)

# Another widget, adding Push button and its parameters
open_btn=QPushButton('Open Files')
# when you hover over this btn u get this msg
open_btn.setToolTip('Find files in the iOS') 
# Changing the size of this btn
open_btn.setFixedWidth(120)
# adding this widget to the main layout
main_layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
# Set the action of the button, what it'll do?
open_btn.clicked.connect(open_files) # once clicked on button .connect method will invoke my fn

# Another widget, adding Destroy button-push and its parameters
destroy_btn=QPushButton('Destroy Files')
# Changing the size of this btn
destroy_btn.setFixedWidth(120)
# adding this widget to the main layout
main_layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files) # once clicked on button .connect method will invoke my fn

# adding widget/Label as msg to inform an user what's going on
message=QLabel('')
main_layout.addWidget(message,alignment=Qt.AlignmentFlag.AlignCenter)

# Display that enetered txt
window.setLayout(main_layout)
window.show()
app.exec()