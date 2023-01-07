from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QLabel,
)

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
hlayout.addWidget(convert_button)

output = QLabel('')
vlayout.addWidget(output)

window.setLayout(vlayout)
window.show()
app.exec()
