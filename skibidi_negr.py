from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  *

skibidi_negr = QApplication([])
negrrrrrrrrrrrrr = QWidget()
negrrrrrrrrrrrrr.setWindowTitle("Adolf")
negrrrrrrrrrrrrr.move(350,0)
negrrrrrrrrrrrrr.setFixedSize(500,600)

negrrrrrrrrrrrrr_layoutV=QVBoxLayout()
negrrrrrrrrrrrrr_layoutH1=QHBoxLayout()
negrrrrrrrrrrrrr_layoutH2=QHBoxLayout()
negrrrrrrrrrrrrr_layoutH3=QHBoxLayout()

sw_button = QPushButton("pidor")
sw_button.setFixedSize(300,100)
sl_button = QPushButton("no pidop")
sl_button.setFixedSize(300,100)

radbut_1 = QRadioButton("я")
radbut_2 = QRadioButton("н")
radbut_3 = QRadioButton("е")
radbut_4 = QRadioButton("г")
radbut_5 = QRadioButton("р")
radbut_6 = QRadioButton("е")
radbut_7 = QRadioButton("т")
radbut_8 = QRadioButton("о")
radbut_9 = QRadioButton("с")

negrrrrrrrrrrrrr_layoutH1.addWidget(radbut_1,alignment=Qt.AlignCenter)
negrrrrrrrrrrrrr_layoutH1.addWidget(radbut_2,alignment=Qt.AlignCenter)
negrrrrrrrrrrrrr_layoutH1.addWidget(radbut_7,alignment=Qt.AlignCenter)
negrrrrrrrrrrrrr_layoutH2.addWidget(radbut_3,alignment=Qt.AlignCenter)
negrrrrrrrrrrrrr_layoutH2.addWidget(radbut_4,alignment=Qt.AlignCenter)
negrrrrrrrrrrrrr_layoutH2.addWidget(radbut_8,alignment=Qt.AlignCenter)
negrrrrrrrrrrrrr_layoutH3.addWidget(radbut_5,alignment=Qt.AlignCenter)
negrrrrrrrrrrrrr_layoutH3.addWidget(radbut_6,alignment=Qt.AlignCenter)
negrrrrrrrrrrrrr_layoutH3.addWidget(radbut_9,alignment=Qt.AlignCenter)

negrrrrrrrrrrrrr_layoutV.addWidget(sw_button,alignment=Qt.AlignCenter)
negrrrrrrrrrrrrr_layoutV.addLayout(negrrrrrrrrrrrrr_layoutH1)
negrrrrrrrrrrrrr_layoutV.addLayout(negrrrrrrrrrrrrr_layoutH2)
negrrrrrrrrrrrrr_layoutV.addLayout(negrrrrrrrrrrrrr_layoutH3)


negrrrrrrrrrrrrr_layoutV.addWidget(sl_button,alignment=Qt.AlignCenter)



negrrrrrrrrrrrrr.setLayout(negrrrrrrrrrrrrr_layoutV)

negrrrrrrrrrrrrr.show()
skibidi_negr.exec_()

