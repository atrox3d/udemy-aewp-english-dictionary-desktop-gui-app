from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
)

import dictionary


def get_definition():
    term = word_input.text()
    definition = dictionary.get_definition(term)
    print(f'{definition=}')
    if definition:
        text = '\n'.join(definition)
    else:
        text = f'term {term} not found, please check'
    print(f'{text=}')
    output.setText(f'{text}')


app = QApplication([])
window = QWidget()
window.setWindowTitle('Word Definition')

vlayout = QVBoxLayout()
hlayout = QHBoxLayout()
vlayout.addLayout(hlayout)

word_input = QLineEdit('')
word_input.setFixedWidth(200)
hlayout.addWidget(word_input)

convert_button = QPushButton('Convert')
convert_button.clicked.connect(get_definition)
hlayout.addWidget(convert_button)

output = QLabel('')
vlayout.addWidget(output)

window.setLayout(vlayout)
window.show()
app.exec()
