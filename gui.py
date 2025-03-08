import sys
import os
import subprocess
import threading
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QTabWidget, QStatusBar, QProgressBar
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt


class SystemOptimizer(QWidget):
    def __init__(self):
        """
        Initialize the SystemOptimizer GUI.
        """
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

        # Layout and widgets
        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()
        self.status_bar = QStatusBar()
        self.status_bar.setStyleSheet("color: white;")

        # Progress bar for long-running tasks
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setRange(0, 0)  # Indeterminate mode

        # Initialize tabs and layout
        self.setup_cleanup_tab()
        self.setup_performance_tab()

        # Add widgets to the main layout
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(self.status_bar)
        self.setLayout(self.layout)

        # Store subprocess for stopping tasks
        self.process = None

    def setup_cleanup_tab(self):
        """
        Set up the "Cleanup" tab with a button to run cleanup tasks and a log area.
        """
        self.cleanup_tab = QWidget()
        self.cleanup_tab_layout = QVBoxLayout()

        # Run Cleanup button
        self.cleanup_button = QPushButton("Run Cleanup")
        self.cleanup_button.setIcon(QIcon.fromTheme("edit-clear"))
        self.cleanup_button.setToolTip("Run system cleanup tasks.")
        self.cleanup_button.clicked.connect(self.run_cleanup)

        # Clear Log button
        self.clear_cleanup_log_button = QPushButton("Clear Log")
        self.clear_cleanup_log_button.setToolTip("Clear the cleanup log.")
        self.clear_cleanup_log_button.clicked.connect(lambda: self.cleanup_log.clear())

        # Log area
        self.cleanup_log = QTextEdit()
        self.cleanup_log.setReadOnly(True)

        # Add widgets to the cleanup tab
        self.cleanup_tab_layout.addWidget(self.cleanup_button)
        self.cleanup_tab_layout.addWidget(self.clear_cleanup_log_button)
        self.cleanup_tab_layout.addWidget(self.cleanup_log)
        self.cleanup_tab.setLayout(self.cleanup_tab_layout)
        self.tabs.addTab(self.cleanup_tab, "Cleanup")

    def setup_performance_tab(self):
        """
        Set up the "Performance" tab with a button to monitor performance and a log area.
        """
        self.performance_tab = QWidget()
        self.performance_tab_layout = QVBoxLayout()

        # Monitor Performance button
        self.monitor_button = QPushButton("Monitor Performance")
        self.monitor_button.setIcon(QIcon.fromTheme("view-refresh"))
        self.monitor_button.setToolTip("Monitor system performance.")
        self.monitor_button.clicked.connect(self.monitor_performance)

        # Stop Monitoring button
        self.stop_monitor_button = QPushButton("Stop Monitoring")
        self.stop_monitor_button.setToolTip("Stop the performance monitoring task.")
        self.stop_monitor_button.clicked.connect(self.stop_process)
        self.stop_monitor_button.setEnabled(False)  # Disabled by default

        # Log area
        self.performance_log = QTextEdit()
        self.performance_log.setReadOnly(True)

        # Add widgets to the performance tab
        self.performance_tab_layout.addWidget(self.monitor_button)
        self.performance_tab_layout.addWidget(self.stop_monitor_button)
        self.performance_tab_layout.addWidget(self.performance_log)
        self.performance_tab.setLayout(self.performance_tab_layout)
        self.tabs.addTab(self.performance_tab, "Performance")

    def log_message(self, log_widget, message, is_error=False):
        """
        Log a message to the specified log widget with a timestamp.

        Args:
            log_widget (QTextEdit): The log widget to append the message to.
            message (str): The message to log.
            is_error (bool): Whether the message is an error (default: False).
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if is_error:
            log_widget.append(f'<span style="color: red;">[{timestamp}] {message}</span>')
        else:
            log_widget.append(f"[{timestamp}] {message}")

    def run_script(self, script_name, log_widget, success_message):
        """
        Run a script and log its output.

        Args:
            script_name (str): The name of the script to run.
            log_widget (QTextEdit): The log widget to display output.
            success_message (str): The message to log on successful completion.
        """
        project_root = os.path.dirname(os.path.abspath(__file__))
        script_path = os.path.join(project_root, "scripts", "windows" if os.name == "nt" else "linux", script_name)

        if not os.path.exists(script_path):
            self.log_message(log_widget, f"Error: Script '{script_name}' not found.", is_error=True)
            self.status_bar.showMessage(f"Script '{script_name}' not found.", 3000)
            return

        try:
            self.progress_bar.setVisible(True)
            if os.name == "nt":
                self.process = subprocess.Popen([script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
            else:
                self.process = subprocess.Popen(["bash", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            stdout, stderr = self.process.communicate()  # Wait for process to complete
            if stdout:
                self.log_message(log_widget, f"{success_message}: {stdout}")
            if stderr:
                self.log_message(log_widget, f"Error: {stderr}", is_error=True)
            self.status_bar.showMessage("Operation completed successfully.", 3000)
        except Exception as e:
            self.log_message(log_widget, f"Error: {str(e)}", is_error=True)
            self.status_bar.showMessage("Operation failed.", 3000)
        finally:
            self.progress_bar.setVisible(False)
            self.process = None
            self.stop_monitor_button.setEnabled(False)

    def run_cleanup(self):
        """
        Run the cleanup script in a separate thread.
        """
        self.log_message(self.cleanup_log, "Running cleanup...")
        threading.Thread(target=self.run_script, args=("auto_cleanup.bat" if os.name == "nt" else "auto_cleanup.sh", self.cleanup_log, "Cleanup completed successfully")).start()

    def monitor_performance(self):
        """
        Run the performance monitoring script in a separate thread.
        """
        self.log_message(self.performance_log, "Monitoring system performance...")
        self.stop_monitor_button.setEnabled(True)
        threading.Thread(target=self.run_script, args=("performance_monitor.bat" if os.name == "nt" else "performance_monitor.sh", self.performance_log, "Performance monitoring completed")).start()

    def stop_process(self):
        """
        Stop the currently running subprocess.
        """
        if self.process:
            self.process.terminate()
            self.log_message(self.performance_log, "Performance monitoring stopped.")
            self.status_bar.showMessage("Monitoring stopped.", 3000)
            self.stop_monitor_button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SystemOptimizer()
    window.show()
    sys.exit(app.exec())