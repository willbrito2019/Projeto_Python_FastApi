import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QComboBox

API_URL = "http://127.0.0.1:8000"

class FinanceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema Financeiro")
        self.setGeometry(100, 100, 400, 300)
        self.layout = QVBoxLayout()

        self.desc_input = QLineEdit(self)
        self.desc_input.setPlaceholderText("Descrição")
        self.layout.addWidget(self.desc_input)

        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText("Valor")
        self.layout.addWidget(self.amount_input)

        self.type_input = QComboBox(self)
        self.type_input.addItems(["receita", "despesa"])
        self.layout.addWidget(self.type_input)

        self.add_button = QPushButton("Adicionar", self)
        self.add_button.clicked.connect(self.add_transaction)
        self.layout.addWidget(self.add_button)

        self.balance_label = QLabel("Saldo: R$ 0,00", self)
        self.layout.addWidget(self.balance_label)

        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Descrição", "Valor", "Tipo"])
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)
        self.load_transactions()
        self.update_balance()

    def add_transaction(self):
        desc = self.desc_input.text()
        amount = float(self.amount_input.text())
        type_ = self.type_input.currentText()
        requests.post(f"{API_URL}/transactions/", json={"description": desc, "amount": amount, "type": type_})
        self.load_transactions()
        self.update_balance()

    def load_transactions(self):
        response = requests.get(f"{API_URL}/transactions/").json()
        self.table.setRowCount(len(response))
        for i, trans in enumerate(response):
            self.table.setItem(i, 0, QTableWidgetItem(trans["description"]))
            self.table.setItem(i, 1, QTableWidgetItem(f"R$ {trans['amount']:.2f}"))
            self.table.setItem(i, 2, QTableWidgetItem(trans["type"]))

    def update_balance(self):
        balance = requests.get(f"{API_URL}/balance/").json()["balance"]
        self.balance_label.setText(f"Saldo: R$ {balance:.2f}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FinanceApp()
    window.show()
    sys.exit(app.exec())