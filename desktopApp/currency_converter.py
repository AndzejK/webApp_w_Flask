# PyQT allaws us to create the Desktop apps

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel,QPushButton,QLineEdit
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
    rate=get_currency_rate() # calling a function that scrapes currant rate from x-rates web
    output=input_text*rate
    output_label.setText(str(output)) # we display this value

# Initial set up
app=QApplication([])
window=QWidget()
window.setWindowTitle('Currency Converter')

# get that field where I can enter a txt
layout=QVBoxLayout() # V - vertical

#before entering value to exchage we want to choose currency value
in_combo=QComboBox()
currencies=['USD','EUR','GBP','AUD','CAD']
in_combo.addItems(currencies)
layout.addWidget(in_combo)

target_combo=QComboBox()
target_combo.addItems(currencies)
layout.addWidget(target_combo)

# Input
text=QLineEdit() # getting value/tx
layout.addWidget(text)

# adding another widget for a button
btn=QPushButton('Convert')
layout.addWidget(btn)
# connecting a button to the txt field with a slot in it in its turn is a fn
btn.clicked.connect(show_currency)

# adding another label/widget/filed to display the outcome
output_label=QLabel('')
layout.addWidget(output_label)


# Display that enetered txt
window.setLayout(layout)
window.show()
app.exec()
