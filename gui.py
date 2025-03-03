import sys
import os
import subprocess
import threading
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QTabWidget, QStatusBar
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

class SystemOptimizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("System Maintenance Optimizer")
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("""
            background-color: #2E2E2E; 
            color: white;
            QPushButton {
                background-color: #1E90FF; 
                color: white; 
                padding: 8px; 
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #00BFFF;
            }
            QTextEdit {
                background-color: #1E1E1E;
                color: white;
                border: 1px solid gray;
            }
            QTabWidget::pane {
                border: 1px solid gray;
            }
        """)

        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()
        self.status_bar = QStatusBar()
        self.status_bar.setStyleSheet("color: white;")

        self.setup_cleanup_tab()
        self.setup_performance_tab()

        self.layout.addWidget(self.tabs)
        self.layout.addWidget(self.status_bar)
        self.setLayout(self.layout)

    def setup_cleanup_tab(self):
        self.cleanup_tab = QWidget()
        self.cleanup_tab_layout = QVBoxLayout()

        self.cleanup_button = QPushButton("Run Cleanup")
        self.cleanup_button.setIcon(QIcon.fromTheme("edit-clear"))
        self.cleanup_button.clicked.connect(self.run_cleanup)

        self.cleanup_log = QTextEdit()
        self.cleanup_log.setReadOnly(True)

        self.cleanup_tab_layout.addWidget(self.cleanup_button)
        self.cleanup_tab_layout.addWidget(self.cleanup_log)
        self.cleanup_tab.setLayout(self.cleanup_tab_layout)
        self.tabs.addTab(self.cleanup_tab, "Cleanup")

    def setup_performance_tab(self):
        self.performance_tab = QWidget()
        self.performance_tab_layout = QVBoxLayout()

        self.monitor_button = QPushButton("Monitor Performance")
        self.monitor_button.setIcon(QIcon.fromTheme("view-refresh"))
        self.monitor_button.clicked.connect(self.monitor_performance)

        self.performance_log = QTextEdit()
        self.performance_log.setReadOnly(True)

        self.performance_tab_layout.addWidget(self.monitor_button)
        self.performance_tab_layout.addWidget(self.performance_log)
        self.performance_tab.setLayout(self.performance_tab_layout)
        self.tabs.addTab(self.performance_tab, "Performance")

    def log_message(self, log_widget, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_widget.append(f"[{timestamp}] {message}")

    def run_script(self, script_name, log_widget, success_message):
        project_root = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(project_root, "scripts", "windows" if os.name == "nt" else "linux", script_name)
        
        try:
            if os.name == "nt":
                result = subprocess.run([script_path], check=True, capture_output=True, text=True, shell=True)
            else:
                result = subprocess.run(["bash", script_path], check=True, capture_output=True, text=True)
            
            self.log_message(log_widget, f"{success_message}: {result.stdout}")
            self.status_bar.showMessage("Operation completed successfully.", 3000)
        except subprocess.CalledProcessError as e:
            self.log_message(log_widget, f"Error: {e.stderr}")
            self.status_bar.showMessage("Operation failed.", 3000)

    def run_cleanup(self):
        self.log_message(self.cleanup_log, "Running cleanup...")
        threading.Thread(target=self.run_script, args=("auto_cleanup.bat" if os.name == "nt" else "auto_cleanup.sh", self.cleanup_log, "Cleanup completed successfully")).start()

    def monitor_performance(self):
        self.log_message(self.performance_log, "Monitoring system performance...")
        threading.Thread(target=self.run_script, args=("performance_monitor.bat" if os.name == "nt" else "performance_monitor.sh", self.performance_log, "Performance monitoring completed")).start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemOptimizer()
    window.show()
    sys.exit(app.exec())