from PyQt5.QtWidgets import *
import add

class Mywin(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(450)
        self.setStyleSheet("font:20px")
        self.main_layout = QVBoxLayout()
        self.add_recipe = QPushButton("Add recipe",clicked=self.add)
        self.edit_recipe = QPushButton("Edit recipe",clicked=self.edit)
        self.remove_recipe = QPushButton("Remove recipe",clicked=self.remove)
        self.search_topic = QPushButton("Search by topic",clicked=self.search_t)
        self.search_name = QPushButton("Search by name",clicked=self.search_n)
        self.exit = QPushButton("Exit",clicked=exit)
        
        self.main_layout.addWidget(self.add_recipe)
        self.main_layout.addWidget(self.edit_recipe)
        self.main_layout.addWidget(self.remove_recipe)
        self.main_layout.addWidget(self.search_topic)
        self.main_layout.addWidget(self.search_name)
        self.main_layout.addWidget(self.exit)
        
        self.setLayout(self.main_layout)
    
    def add(self):
        self.hide()
        self.add_win = add.win_add(self)
        self.add_win.show()
    
    def edit(self):
        pass
    
    def remove(self):
        pass
    
    def search_t(self):
        pass
    
    def search_n(self):
        pass