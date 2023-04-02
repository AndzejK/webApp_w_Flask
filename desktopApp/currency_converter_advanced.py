# PyQT allaws us to create the Desktop apps

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout #horizontal layout
from PyQt6.QtWidgets import QLabel,QPushButton,QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QComboBox # for dropdown box!
from bs4 import BeautifulSoup
import requests

# Creating a function for a slot
def get_currency_rate(in_cur, out_cur):
    url = f"https://www.x-rates.com/calculator/?from={in_cur}&to={out_cur}&amount=1"
    # if you enter "EUR","AUD" the result would be https://www.x-rates.com/calculator/?from=EUR&to=AUD&amount=1
    get_content=requests.get(url).text # getting SOURCE CODE 
    # At this stage we start using bs4 lib
    soup = BeautifulSoup(get_content,"html.parser")
    # finding class for our rate in HTML format
    soup.find("span", class_="ccOutputRslt")
    # display just text as browser for an user!
    rate=soup.find("span", class_="ccOutputRslt").get_text() # result is 1.598466 AUD and we want to have just numbers
    rate=float(rate[:-4])
    return rate

def show_currency():
    input_text=float(text.text()) # extract the value from text field
    # provide currency nominal like AUD, CAD
    in_cur=in_combo.currentText()
    target_cur=target_combo.currentText()
    print(in_cur,target_cur)
    rate=get_currency_rate(in_cur,target_cur) # calling a function that scrapes currant rate from x-rates web
    output=input_text*rate
    message=f'{input_text} {in_cur} is {output} {target_cur}'
    output_label.setText(str(message)) # we display the final rate plus msg!

# Initial set up
app=QApplication([])
window=QWidget()
window.setWindowTitle('Currency Converter')

# The main layout 
layout=QVBoxLayout() # V - vertical
# Since it has vertical and horizontal layouts we will create them here and add the main layout
layout1=QHBoxLayout() # V - horizontal, for dropdown option (choose currency nominal) and button
# adding child layout to the main/parent layout
layout.addLayout(layout1)

# since label is part of the main layout it'll be here as well
output_label=QLabel('')
layout.addWidget(output_label)

# Going deeper into main layout where in Layout1 we have antoher two layouts 1_1 and 1_2
# layout1_1 will as collumn thus it's vertical layout
layout1_1=QVBoxLayout()
# Now layout1_1 is part of layout1 layout
layout1.addLayout(layout1_1)

# layout1_2 will as collumn thus it's vertical layout
layout1_2=QVBoxLayout()
# Now layout1_2 is part of layout1 layout
layout1.addLayout(layout1_2)

# Again now we're going deeper into hierarchy, where layout1_1 and layout1_2 have in them layouts too

in_combo=QComboBox()
currencies=['USD','EUR','GBP','AUD','CAD']
in_combo.addItems(currencies)
# Here were adding in_combo (dropbox) Widget to layout1_1 (separate layout but the parent is layout1_1)
layout1_1.addWidget(in_combo)

target_combo=QComboBox()
target_combo.addItems(currencies)
# Here were adding target_combo (button/input) Widget to layout1_2 (separate layout but the parent is layout1_2)
layout1_1.addWidget(target_combo)

# Input
text=QLineEdit() # getting value/tx
# based on hierarchy this widget belongs to layout1_2
layout1_2.addWidget(text, alignment=Qt.AlignmentFlag.AlignBottom)

# adding another widget for a button
btn=QPushButton('Convert')
# based on hierarchy this widget belongs to layout1_2
layout1_2.addWidget(btn, alignment=Qt.AlignmentFlag.AlignBottom)
# connecting a button to the txt field with a slot in it in its turn is a fn
btn.clicked.connect(show_currency)


# Display that enetered txt
window.setLayout(layout)
window.show()
app.exec()
