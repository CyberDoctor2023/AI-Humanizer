import sys
import random
import re
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QTextEdit, QPushButton, QProgressBar)
from PyQt6.QtGui import QPainter, QColor, QLinearGradient
from PyQt6.QtCore import Qt, QTimer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("杰哥的降AI工具")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(20, 20, 20, 20)

        self.input_area = QTextEdit(self)
        self.input_area.setPlaceholderText(
            "在这里输入文本（第一行将被视为主标题）...")
        layout.addWidget(self.input_area)

        self.magic_button = QPushButton("施展双重魔法", self)
        self.magic_button.clicked.connect(self.perform_double_magic)
        layout.addWidget(self.magic_button)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        self.output_area = QTextEdit(self)
        self.output_area.setPlaceholderText("处理后的文本将出现在这里...")
        self.output_area.setReadOnly(True)
        layout.addWidget(self.output_area)

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(230, 243, 255))
        gradient.setColorAt(1, QColor(240, 230, 255))
        painter.fillRect(self.rect(), gradient)

    def perform_double_magic(self):
        input_text = self.input_area.toPlainText()
        if input_text:
            self.progress_bar.setValue(0)
            self.magic_button.setEnabled(False)

            # 格式化文本，确保段落之间有空行
            formatted_text = self.format_paragraphs(input_text)

            # 第一次混淆
            processed_text = self.apply_magic(formatted_text)
            self.progress_bar.setValue(50)

            # 使用 QTimer 来延迟第二次混淆，以便更新进度条
            QTimer.singleShot(100, lambda: self.second_magic(processed_text))
        else:
            self.output_area.setPlainText("请先输入一些文本哦~")

    def second_magic(self, text):
        # 第二次混淆
        final_text = self.apply_magic(text)
        self.progress_bar.setValue(100)
        self.output_area.setPlainText(final_text)
        self.magic_button.setEnabled(True)

    def format_paragraphs(self, text):
        # 将原文本中的段落分开，确保每段之间有一个空行
        paragraphs = text.split('\n')
        formatted_paragraphs = []

        for paragraph in paragraphs:
            if paragraph.strip():  # 非空段落才处理
                formatted_paragraphs.append(paragraph.strip())

        # 将格式化后的段落列表重新拼接，每段之间加一个空行
        return '\n\n'.join(formatted_paragraphs)

    def is_subtitle(self, line):
        return len(line.split()) <= 5 or line.endswith(':') or line.startswith(
            '#')

    def apply_magic(self, text):
        paragraphs = text.split('\n\n')
        processed_paragraphs = []

        for i, paragraph in enumerate(paragraphs):
            if i == 0:  # 保留主标题
                processed_paragraphs.append(paragraph)
            else:
                lines = paragraph.split('\n')
                processed_lines = []
                for line in lines:
                    if self.is_subtitle(line):
                        processed_lines.append(line)  # 保留小标题
                    else:
                        processed_lines.append(self.process_paragraph(line))
                processed_paragraphs.append('\n'.join(processed_lines))

        return '\n\n'.join(processed_paragraphs)

    def process_paragraph(self, paragraph):
        words = paragraph.split()
        processed_words = []
        for word in words:
            word = self.process_word(word)
            processed_words.append(word)

        processed_text = ' '.join(processed_words)
        return self.apply_space_variations(processed_text)

    def process_word(self, word):
        if len(word) > 1 and random.random() < 0.15:  # 15% 概率改变首字母大小写
            word = word[0].swapcase() + word[1:]
        return word

    def apply_space_variations(self, text):
        punctuation = r'[,.\?!:;]'
        parts = re.split(f'({punctuation})', text)
        result = []
        for part in parts:
            if re.match(punctuation, part):
                space = self.get_random_space()
                result.append(part + space)
            else:
                result.append(part)
        return ''.join(result).strip()

    def get_random_space(self):
        rand = random.random()
        if rand < 0.33:  # 33% 概率没有空格
            return ''
        elif rand < 0.66:  # 33% 概率两个空格
            return '  '
        elif rand < 0.99:  # 33% 概率一个空格
            return ' '
        else:  # 1% 概率三个空格
            return '   '


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
