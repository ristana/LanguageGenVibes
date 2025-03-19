"""GUI module for the translation application."""
from typing import Dict, List
import sys
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
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextCursor
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
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Language selection
        lang_layout = QHBoxLayout()
        lang_label = QLabel("Select Language:")
        self.lang_combo = QComboBox()
        # Capitalize language names for display
        languages = [lang.title() for lang in get_available_languages()]
        self.lang_combo.addItems(languages)
        lang_layout.addWidget(lang_label)
        lang_layout.addWidget(self.lang_combo)
        layout.addLayout(lang_layout)
        
        # Chat history
        history_label = QLabel("Chat History:")
        self.history_text = QTextEdit()
        self.history_text.setReadOnly(True)
        layout.addWidget(history_label)
        layout.addWidget(self.history_text)
        
        # Input area
        input_label = QLabel("Enter Text:")
        self.input_text = QTextEdit()
        self.input_text.setMaximumHeight(100)
        layout.addWidget(input_label)
        layout.addWidget(self.input_text)
        
        # Buttons
        button_layout = QHBoxLayout()
        self.translate_btn = QPushButton("Translate")
        self.copy_btn = QPushButton("Copy History")
        self.clear_btn = QPushButton("Clear")
        
        button_layout.addWidget(self.translate_btn)
        button_layout.addWidget(self.copy_btn)
        button_layout.addWidget(self.clear_btn)
        layout.addLayout(button_layout)
        
        # Connect signals
        self.translate_btn.clicked.connect(self.translate_text)
        self.copy_btn.clicked.connect(self.copy_history)
        self.clear_btn.clicked.connect(self.clear_all)
        
        # Initialize chat history
        self.chat_history: List[Dict[str, str]] = []

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