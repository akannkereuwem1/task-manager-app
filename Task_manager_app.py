import sys
import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg

class TaskManagerApp(qtw.QWidget):
    def __init__(self):
        super().__init__()
        
        self.task_label = qtw.QLabel("Task Manager", self)
        self.add_button = qtw.QPushButton('Add Task', self)
        self.add_button.clicked.connect(self.add_task)
        
        self.task_list = qtw.QListWidget()

      
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Task Manager App')
        self.setGeometry(100, 100, 800, 600)

        # Input field
        self.task_input = qtw.QLineEdit(placeholderText='Enter a task here')

        # Layout
        h_box = qtw.QHBoxLayout()
        v_box = qtw.QVBoxLayout()

        # Vertical layout
        v_box.addWidget(self.task_label)
        v_box.addWidget(self.task_list)
        v_box.setAlignment(qtc.Qt.AlignmentFlag.AlignTop)

        # Horizontal layout
        self.setLayout(v_box)
        v_box.addLayout(h_box)
        h_box.addWidget(self.task_input)
        h_box.addWidget(self.add_button)
        h_box.setAlignment(qtc.Qt.AlignmentFlag.AlignCenter)
        
        # Complete task
        self.complete_button = qtw.QPushButton('Complete Task', self)
        self.complete_button.clicked.connect(self.complete_task)
        h_box.addWidget(self.complete_button)

        # Delete task
        self.delete_button = qtw.QPushButton('Delete Task', self)
        self.delete_button.clicked.connect(self.delete_completed_tasks)
        h_box.addWidget(self.delete_button)

    def add_task(self):
        task_text = self.task_input.text()
        if task_text:
            num = self.task_list.count() + 1
            self.task_list.addItem(f"{num}. {task_text}")  # Add task to list
            self.task_input.clear()  # Clear input field
        else:
            qtw.QMessageBox.warning(self, "Warning", "Task Cannot be empty!")
  

    def complete_task(self):
        # Marks the selected Item as completed (strikethrough effect)
        selected_item = self.task_list.currentItem()
        if selected_item:
            font = selected_item.font()
            font.setStrikeOut(True)
            selected_item.setFont(font)
            selected_item.setForeground(qtg.QColor('green'))
        else:
            qtw.QMessageBox.warning(self, "Warning", "No Task Selected")

    def delete_completed_tasks(self):
        """Removes completed tasks (tasks with strikethrough)."""
        for index in range(self.task_list.count() - 1, -1, -1):  # Loop in reverse to avoid shifting issues
            item = self.task_list.item(index)
            if item.font().strikeOut():  # Check if task is completed
                self.task_list.takeItem(index)  # Remove item from list

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    taskmanager = TaskManagerApp()
    taskmanager.show()

    sys.exit(app.exec())



