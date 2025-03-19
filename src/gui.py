"""GUI module for the translation application."""
from typing import Dict, List
import sys
import os
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QTextEdit,
    QPushButton,
    QLabel,
    QScrollArea,
    QMessageBox,
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QTextCursor, QPalette, QColor, QBrush, QPixmap
from .translator import Translator
from .languages import get_available_languages


class TranslationWindow(QMainWindow):
    """Main window for the translation application."""

    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        self.setWindowTitle("Fictional Language Translator")
        self.setMinimumSize(800, 600)
        
        # Initialize translator
        self.translator = Translator()
        
        # Create main widget and layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        layout = QVBoxLayout(self.main_widget)
        
        # Set up the background textures
        self.textures = {
            'cybernetic': 'CyberneticBinary.png',
            'dwarvish': 'DwarvishRunic.png',
            'insectoid': 'AlienInsectoid.png',
            'celestial': 'EtherealCelestial.png',
            'necrotic': 'NecroticUndead.png',
            'elvish': 'EtherealCelestial.png'  # Using celestial texture as fallback for elvish
        }
        
        # Language selection
        lang_layout = QHBoxLayout()
        lang_label = QLabel("Select Language:")
        lang_label.setStyleSheet("color: white; font-weight: bold;")
        self.lang_combo = QComboBox()
        self.lang_combo.setStyleSheet("""
            QComboBox {
                background-color: #D3D3D3;
                border: 1px solid #A9A9A9;
                border-radius: 3px;
                padding: 5px;
            }
            QComboBox:hover {
                background-color: #E8E8E8;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: url(assets/icon.ico);
                width: 12px;
                height: 12px;
            }
        """)
        
        # Capitalize language names for display
        languages = [lang.title() for lang in get_available_languages()]
        self.lang_combo.addItems(languages)
        lang_layout.addWidget(lang_label)
        lang_layout.addWidget(self.lang_combo)
        layout.addLayout(lang_layout)
        
        # Chat history
        history_label = QLabel("Chat History:")
        history_label.setStyleSheet("color: white; font-weight: bold;")
        self.history_text = QTextEdit()
        self.history_text.setReadOnly(True)
        self.history_text.setStyleSheet("""
            QTextEdit {
                background-color: rgba(128, 128, 128, 180);
                border: 1px solid #A9A9A9;
                border-radius: 5px;
                color: white;
                padding: 10px;
            }
        """)
        layout.addWidget(history_label)
        layout.addWidget(self.history_text)
        
        # Input area
        input_label = QLabel("Enter Text:")
        input_label.setStyleSheet("color: white; font-weight: bold;")
        self.input_text = QTextEdit()
        self.input_text.setMaximumHeight(100)
        self.input_text.setStyleSheet("""
            QTextEdit {
                background-color: rgba(128, 128, 128, 180);
                border: 1px solid #A9A9A9;
                border-radius: 5px;
                color: white;
                padding: 10px;
            }
        """)
        layout.addWidget(input_label)
        layout.addWidget(self.input_text)
        
        # Buttons
        button_layout = QHBoxLayout()
        button_style = """
            QPushButton {
                background-color: #D3D3D3;
                border: 1px solid #A9A9A9;
                border-radius: 3px;
                padding: 5px 15px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #E8E8E8;
            }
            QPushButton:pressed {
                background-color: #C0C0C0;
            }
        """
        
        self.translate_btn = QPushButton("Translate")
        self.translate_btn.setStyleSheet(button_style)
        self.copy_btn = QPushButton("Copy History")
        self.copy_btn.setStyleSheet(button_style)
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.setStyleSheet(button_style)
        
        button_layout.addWidget(self.translate_btn)
        button_layout.addWidget(self.copy_btn)
        button_layout.addWidget(self.clear_btn)
        layout.addLayout(button_layout)
        
        # Connect signals
        self.translate_btn.clicked.connect(self.translate_text)
        self.copy_btn.clicked.connect(self.copy_history)
        self.clear_btn.clicked.connect(self.clear_all)
        self.lang_combo.currentTextChanged.connect(self.update_background)
        
        # Initialize chat history
        self.chat_history: List[Dict[str, str]] = []
        
        # Set initial background
        self.update_background(self.lang_combo.currentText())

    def update_background(self, language: str) -> None:
        """Update the background texture based on the selected language."""
        language = language.lower()
        if language in self.textures:
            texture_path = os.path.join('assets', self.textures[language])
            if os.path.exists(texture_path):
                pixmap = QPixmap(texture_path)
                # Scale the pixmap to fit the window while maintaining aspect ratio
                scaled_pixmap = pixmap.scaled(
                    self.size(),
                    Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                    Qt.TransformationMode.SmoothTransformation
                )
                
                # Create a palette and set the background
                palette = self.main_widget.palette()
                palette.setBrush(
                    QPalette.ColorRole.Window,
                    QBrush(scaled_pixmap)
                )
                self.main_widget.setAutoFillBackground(True)
                self.main_widget.setPalette(palette)

    def resizeEvent(self, event) -> None:
        """Handle window resize events to update the background scaling."""
        super().resizeEvent(event)
        self.update_background(self.lang_combo.currentText())

    def translate_text(self) -> None:
        """Translate the input text and update the chat history."""
        input_text = self.input_text.toPlainText().strip()
        if not input_text:
            QMessageBox.information(
                self,
                "Translation",
                "Please enter some text to translate."
            )
            return
            
        try:
            selected_lang = self.lang_combo.currentText().lower()
            translated_text = self.translator.translate(input_text, selected_lang)
            
            # Add to chat history
            self.chat_history.append({
                "original": input_text,
                "translated": translated_text,
                "language": selected_lang.title()
            })
            
            # Update history display
            self.update_history_display()
            
            # Clear input
            self.input_text.clear()
            
        except Exception as e:
            QMessageBox.critical(
                self,
                "Translation Error",
                f"An error occurred during translation: {str(e)}"
            )

    def update_history_display(self) -> None:
        """Update the chat history display."""
        history_text = ""
        for entry in self.chat_history:
            history_text += f"[{entry['language']}]\n"
            history_text += f"Original: {entry['original']}\n"
            history_text += f"Translated: {entry['translated']}\n"
            history_text += "-" * 50 + "\n"
        
        self.history_text.setText(history_text)
        # Scroll to bottom
        scrollbar = self.history_text.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def copy_history(self) -> None:
        """Copy the chat history to clipboard."""
        if not self.chat_history:
            QMessageBox.information(
                self,
                "Copy History",
                "No translations to copy yet."
            )
            return
            
        self.history_text.selectAll()
        self.history_text.copy()
        cursor = self.history_text.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.Start)
        self.history_text.setTextCursor(cursor)
        QMessageBox.information(
            self,
            "Copy History",
            "Chat history copied to clipboard!"
        )

    def clear_all(self) -> None:
        """Clear the input and chat history."""
        if self.chat_history:
            reply = QMessageBox.question(
                self,
                "Clear History",
                "Are you sure you want to clear all translations?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                self.input_text.clear()
                self.chat_history.clear()
                self.update_history_display()


def main() -> None:
    """Run the GUI application."""
    app = QApplication(sys.argv)
    window = TranslationWindow()
    window.show()
    sys.exit(app.exec()) 