import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSpinBox, QComboBox, QDateEdit, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QScrollArea, QCalendarWidget
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore


class PupPlateGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PupPlate")
        self.setGeometry(100, 100, 800, 600)

        # Set app logo
        logo = QLabel(self)
        pixmap = QPixmap('pupplate_logo.png')
        logo.setPixmap(pixmap)
        logo.setAlignment(QtCore.Qt.AlignCenter)

        # Set menu options
        schedule_button = QPushButton(QIcon('schedule_icon.png'), "Feeding Schedule", self)
        intake_button = QPushButton(QIcon('intake_icon.png'), "Food Intake Tracker", self)
        nutrition_button = QPushButton(QIcon('nutrition_icon.png'), "Nutritional Information", self)

        # Set button styles
        button_style = "QPushButton {background-color: #90caf9; color: white; border-radius: 10px; font-size: 18px; font-weight: bold;}"
        schedule_button.setStyleSheet(button_style)
        intake_button.setStyleSheet(button_style)
        nutrition_button.setStyleSheet(button_style)

        # Set button layouts
        button_layout1 = QVBoxLayout()
        button_layout1.addWidget(schedule_button)
        button_layout2 = QVBoxLayout()
        button_layout2.addWidget(intake_button)
        button_layout3 = QVBoxLayout()
        button_layout3.addWidget(nutrition_button)
        buttons_layout = QHBoxLayout()
        buttons_layout.addLayout(button_layout1)
        buttons_layout.addLayout(button_layout2)
        buttons_layout.addLayout(button_layout3)

        # Set main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(logo)
        main_layout.addLayout(buttons_layout)

        # Set the central widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Connect the button signals to the slots
        schedule_button.clicked.connect(self.show_feeding_schedule)
        intake_button.clicked.connect(self.show_food_intake_tracker)
        nutrition_button.clicked.connect(self.show_nutritional_information)

    def show_feeding_schedule(self):
        # Create a new widget for the feeding schedule
        feeding_schedule_widget = QWidget()

        # Create the feeding schedule layout
        feeding_schedule_layout = QVBoxLayout()

        # Add the initial feedings
        self.add_feeding(feeding_schedule_layout)
        self.add_feeding(feeding_schedule_layout)

        # Create the add feeding button
        add_feeding_button = QPushButton("Add Feeding")

        # Connect the button signal to the slot
        add_feeding_button.clicked.connect(lambda: self.add_feeding(feeding_schedule_layout))

        # Add the add feeding button to the layout
        feeding_schedule_layout.addWidget(add_feeding_button)

        # Create the back button
        back_button = QPushButton("Back")

        # Connect the button signal to the slot
        back_button.clicked.connect(lambda: self.setCentralWidget(self.central_widget()))

        # Add the back button to the layout
        feeding_schedule_layout.addWidget(back_button)

        # Set the layout for the feeding schedule widget
        feeding_schedule_widget.setLayout(feeding_schedule_layout)

        # Create a scroll area for the feeding schedule widget
        feeding_schedule_scroll_area = QScrollArea()
        feeding_schedule_scroll_area.setWidget(feeding_schedule_widget)

        # Set the central widget to the feeding schedule scroll area
        self.setCentralWidget(feeding_schedule_scroll_area)




    def show_food_intake_tracker(self):
        # Create a new widget for the food intake tracker
        food_intake_tracker_widget = QWidget()

        # Create the food intake tracker layout
        food_intake_tracker_layout = QVBoxLayout()

        # Create the calendar widget
        calendar = QCalendarWidget()

        # Add the calendar widget to the layout
        food_intake_tracker_layout.addWidget(calendar)

        # Set the layout for the food intake tracker widget
        food_intake_tracker_widget.setLayout(food_intake_tracker_layout)

        # Create a scroll area for the food intake tracker widget
        food_intake_tracker_scroll_area = QScrollArea()
        food_intake_tracker_scroll_area.setWidget(food_intake_tracker_widget)

        # Set the central widget to the food intake tracker scroll area
        self.setCentralWidget(food_intake_tracker_scroll_area)

        
    def show_nutritional_information(self):
        # Create a new widget for the nutritional information
        nutritional_information_widget = QWidget()

        # Create the nutritional information layout
        nutritional_information_layout = QVBoxLayout()

        # Add the nutritional information labels
        food_name_label = QLabel("Food Name:")
        food_name_value_label = QLabel("Acme Dog Food")
        serving_size_label = QLabel("Serving Size:")
        serving_size_value_label = QLabel("1 cup (100g)")
        calories_label = QLabel("Calories:")
        calories_value_label = QLabel("350")
        protein_label = QLabel("Protein:")
        protein_value_label = QLabel("20g")
        fat_label = QLabel("Fat:")
        fat_value_label = QLabel("10g")
        carbs_label = QLabel("Carbs:")
        carbs_value_label = QLabel("35g")

        # Add the labels to the nutritional information layout
        nutritional_information_layout.addWidget(food_name_label)
        nutritional_information_layout.addWidget(food_name_value_label)
        nutritional_information_layout.addWidget(serving_size_label)
        nutritional_information_layout.addWidget(serving_size_value_label)
        nutritional_information_layout.addWidget(calories_label)
        nutritional_information_layout.addWidget(calories_value_label)
        nutritional_information_layout.addWidget(protein_label)
        nutritional_information_layout.addWidget(protein_value_label)
        nutritional_information_layout.addWidget(fat_label)
        nutritional_information_layout.addWidget(fat_value_label)
        nutritional_information_layout.addWidget(carbs_label)
        nutritional_information_layout.addWidget(carbs_value_label)

        # Set the layout for the nutritional information widget
        nutritional_information_widget.setLayout(nutritional_information_layout)

        # Create a scroll area for the nutritional information widget
        nutritional_information_scroll_area = QScrollArea()
        nutritional_information_scroll_area.setWidget(nutritional_information_widget)

        # Set the central widget to the nutritional information scroll area
        self.setCentralWidget(nutritional_information_scroll_area)
            
    def add_feeding(self, feeding_schedule_layout):
        # Create a new horizontal layout for the feeding
        feeding_layout = QHBoxLayout()

        # Create the feeding time spin box
        feeding_time_spin_box = QSpinBox()
        feeding_time_spin_box.setRange(0, 23)

        # Create the feeding amount line edit
        feeding_amount_line_edit = QLineEdit()

        # Add the widgets to the feeding layout
        feeding_layout.addWidget(feeding_time_spin_box)
        feeding_layout.addWidget(feeding_amount_line_edit)

        # Add the feeding layout to the feeding schedule layout
        feeding_schedule_layout.addLayout(feeding_layout)        

def main():
    # Create the application
    app = QApplication([])

    # Create the main window
    window = PupPlateGUI()

    # Show the main window
    window.show()

    # Run the event loop
    app.exec_()


if __name__ == '__main__':
    main()
