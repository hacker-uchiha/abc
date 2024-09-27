from mainpage import *


class win_add(QWidget):
    def __init__(self,obj):
        super().__init__()
        self.main_win = obj
        self.setStyleSheet("font:20px")
        
        self.main_lay = QVBoxLayout()
        self.lbl_lay = QVBoxLayout()
        self.edit_lay = QVBoxLayout()
        self.lbl_and_edit_lay = QHBoxLayout()
        self.btn_lay = QHBoxLayout()
        
        self.name_lbl = QLabel("Name: ")
        self.name = QLineEdit()
        self.ingredients_lbl = QLabel("Ingredients: ")
        self.ingredients = QTextEdit()
        self.ingredients.setFixedHeight(70)
        self.ingredients.setStyleSheet("font:16px")
        self.preparation_lbl =  QLabel("Preparation")
        self.preparation = QTextEdit()
        self.preparation.setStyleSheet("font:16px")
        self.preparation.setFixedHeight(70)
        self.back_btn = QPushButton("Back",clicked=self.BACK)
        self.add_btn = QPushButton("Add",clicked=self.ADD)
        self.clear_btn = QPushButton("Clear",clicked=self.CLEAR)
        
        self.lbl_lay.addWidget(self.name_lbl)
        self.lbl_lay.addStretch()
        self.lbl_lay.addWidget(self.ingredients_lbl)
        self.lbl_lay.addStretch()
        self.lbl_lay.addWidget(self.preparation_lbl)
        
        self.edit_lay.addWidget(self.name)
        self.edit_lay.addStretch()
        self.edit_lay.addWidget(self.ingredients)
        self.edit_lay.addStretch()
        self.edit_lay.addWidget(self.preparation)
        
        self.lbl_and_edit_lay.addLayout(self.lbl_lay)
        self.lbl_and_edit_lay.addLayout(self.edit_lay)
        
        self.btn_lay.addWidget(self.clear_btn)
        self.btn_lay.addWidget(self.add_btn)
        
        self.main_lay.addLayout(self.lbl_and_edit_lay)
        self.main_lay.addLayout(self.btn_lay)
        self.main_lay.addWidget(self.back_btn)
        self.setLayout(self.main_lay)
        
    
    def BACK(self):
        self.hide()
        self.main_win.show()
    
    def ADD(self):
        pass
    
    def CLEAR(self):
        for i in range(self.edit_lay.count()):
            x = self.edit_lay.itemAt(i).widget()
            if x is not None:
                x.clear()