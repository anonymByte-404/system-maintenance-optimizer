import sys
import os
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QTabWidget
from PyQt6.QtGui import QIcon

class SystemOptimizer(QWidget):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("System Maintenance Optimizer")
    self.setGeometry(100, 100, 500, 400)
    self.setStyleSheet("background-color: #2E2E2E; color: white;")

    layout = QVBoxLayout()

    self.tabs = QTabWidget()
    self.tabs.setStyleSheet("QTabWidget::pane { border: 1px solid gray; }")
    
    self.cleanup_tab = QWidget()
    self.cleanup_tab_layout = QVBoxLayout()
    
    self.cleanup_button = QPushButton("Run Cleanup")
    self.cleanup_button.setStyleSheet("background-color: #1E90FF; color: white; padding: 8px; border-radius: 5px;")
    self.cleanup_button.setIcon(QIcon.fromTheme("edit-clear"))
    self.cleanup_button.clicked.connect(self.run_cleanup)
    
    self.cleanup_log = QTextEdit()
    self.cleanup_log.setReadOnly(True)
    
    self.cleanup_tab_layout.addWidget(self.cleanup_button)
    self.cleanup_tab_layout.addWidget(self.cleanup_log)
    self.cleanup_tab.setLayout(self.cleanup_tab_layout)

    self.performance_tab = QWidget()
    self.performance_tab_layout = QVBoxLayout()
    
    self.monitor_button = QPushButton("Monitor Performance")
    self.monitor_button.setStyleSheet("background-color: #32CD32; color: white; padding: 8px; border-radius: 5px;")
    self.monitor_button.setIcon(QIcon.fromTheme("view-refresh"))
    self.monitor_button.clicked.connect(self.monitor_performance)
    
    self.performance_log = QTextEdit()
    self.performance_log.setReadOnly(True)
    
    self.performance_tab_layout.addWidget(self.monitor_button)
    self.performance_tab_layout.addWidget(self.performance_log)
    self.performance_tab.setLayout(self.performance_tab_layout)

    self.tabs.addTab(self.cleanup_tab, "Cleanup")
    self.tabs.addTab(self.performance_tab, "Performance")

    layout.addWidget(self.tabs)
    self.setLayout(layout)

  def run_cleanup(self):
    self.cleanup_log.append("Running cleanup...")
    project_root = os.path.dirname(os.path.abspath(__file__))
    
    try:
      if os.name == "nt":
        cleanup_script = os.path.join(project_root, "scripts", "windows", "auto_cleanup.bat")
        result = subprocess.run([cleanup_script], check=True, capture_output=True, text=True, shell=True)
        self.cleanup_log.append(f"Cleanup completed successfully: {result.stdout}")
      else:
        cleanup_script = os.path.join(project_root, "scripts", "linux", "auto_cleanup.sh")
        result = subprocess.run(["bash", cleanup_script], check=True, capture_output=True, text=True)
        self.cleanup_log.append(f"Cleanup completed successfully: {result.stdout}")
    except subprocess.CalledProcessError as e:
      self.cleanup_log.append(f"Error during cleanup: {e.stderr}")

  def monitor_performance(self):
    self.performance_log.append("Monitoring system performance...")
    project_root = os.path.dirname(os.path.abspath(__file__))
    
    try:
      if os.name == "nt":
        monitor_script = os.path.join(project_root, "scripts", "windows", "performance_monitor.bat")
        result = subprocess.run([monitor_script], check=True, capture_output=True, text=True, shell=True)
        self.performance_log.append(f"Performance monitoring completed: {result.stdout}")
      else:
        monitor_script = os.path.join(project_root, "scripts", "linux", "performance_monitor.sh")
        result = subprocess.run(["bash", monitor_script], check=True, capture_output=True, text=True)
        self.performance_log.append(f"Performance monitoring completed: {result.stdout}")
    except subprocess.CalledProcessError as e:
      self.performance_log.append(f"Error during performance monitoring: {e.stderr}")

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = SystemOptimizer()
  window.show()
  sys.exit(app.exec())
