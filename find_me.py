import sys

import requests

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class FindMeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Find Me")
        self.setGeometry(500, 200, 350, 240)
        self.find_edit: QLineEdit
        self.find_btn: QPushButton
        self.word_box: QTextEdit
        self.find_layout: QHBoxLayout
        self.main_layout: QVBoxLayout
        self.setup_ui()

    def setup_ui(self):
        self.find_edit = QLineEdit()
        self.find_btn = QPushButton("查询单词")
        self.find_btn.clicked.connect(self.find_word)
        self.find_btn.setGeometry(100, 80, 100, 30)
        self.find_layout = QHBoxLayout()
        self.find_layout.addWidget(self.find_edit)
        self.find_layout.addWidget(self.find_btn)

        self.word_box = QTextEdit()
        self.word_box.setGeometry(100, 40, 100, 30)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addLayout(self.find_layout)
        self.main_layout.addWidget(self.word_box)

    def find_word(self):
        words = self.find_edit.text()
        url = "https://open.maimemo.com/open/api/v1/memo/study/query_study_records"
        payload = {
            "next_study_date": {
                "start": "2026-07-09T00:16:00.000Z",
                "end": "2027-07-09T00:16:00.000Z"
            },
            "spellings": [words],
            "tags": "STICKING",
            "as_count": False,
            "limit": 50
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Bearer 4295596d84c27c0028bf788e34d6298af70c3decef597230208aa0c40b8d622e"
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            self.word_box.setText(str(response.json()))
        else:
            self.word_box.setText("查询失败")


if __name__ == "__main__":
    app = QApplication([])
    window = FindMeWindow()
    window.show()
    sys.exit(app.exec())

