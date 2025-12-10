import sys
import random
import re
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QTextEdit, QPushButton, QProgressBar, QMessageBox)
from PyQt6.QtCore import QTimer

# PyQt 主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.current_probability = 0.15

    def initUI(self):
        self.setWindowTitle("文本混淆工具")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(20, 20, 20, 20)

        self.input_area = QTextEdit(self)
        self.input_area.setPlaceholderText("在这里输入文本（第一行将被视为主标题）...")
        layout.addWidget(self.input_area)

        self.low_prob_button = QPushButton("低概率", self)
        self.low_prob_button.clicked.connect(lambda: self.set_probability(0.15))
        layout.addWidget(self.low_prob_button)

        self.medium_prob_button = QPushButton("中概率", self)
        self.medium_prob_button.clicked.connect(lambda: self.set_probability(0.20))
        layout.addWidget(self.medium_prob_button)

        self.high_prob_button = QPushButton("高概率", self)
        self.high_prob_button.clicked.connect(lambda: self.set_probability(0.30))
        layout.addWidget(self.high_prob_button)

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

    def set_probability(self, prob):
        self.current_probability = prob

    def perform_double_magic(self):
        input_text = self.input_area.toPlainText()
        if input_text:
            self.progress_bar.setValue(0)
            self.magic_button.setEnabled(False)
            self.magic_button.setText("处理中...")

            formatted_text = self.format_paragraphs(input_text)
            processed_text = self.apply_magic(formatted_text)
            self.progress_bar.setValue(50)

            QTimer.singleShot(100, lambda: self.second_magic(processed_text))
        else:
            QMessageBox.warning(self, "警告", "请先输入一些文本哦~")

    def second_magic(self, text):
        final_text = self.apply_magic(text)
        self.progress_bar.setValue(100)
        self.output_area.setPlainText(final_text)
        self.magic_button.setEnabled(True)
        self.magic_button.setText("施展双重魔法")

    def format_paragraphs(self, text):
        paragraphs = text.split('\n')
        formatted_paragraphs = [paragraph.strip() for paragraph in paragraphs if paragraph.strip()]
        return '\n\n'.join(formatted_paragraphs)

    def is_subtitle(self, line):
        return len(line.split()) <= 5 or line.endswith(':') or line.startswith('#')

    def apply_magic(self, text):
        paragraphs = text.split('\n\n')
        processed_paragraphs = []

        for i, paragraph in enumerate(paragraphs):
            if i == 0:
                processed_paragraphs.append(paragraph)
            else:
                lines = paragraph.split('\n')
                processed_lines = [self.process_paragraph(line) if not self.is_subtitle(line) else line for line in lines]
                processed_paragraphs.append('\n'.join(processed_lines))

        return '\n\n'.join(processed_paragraphs).strip()

    def process_paragraph(self, paragraph):
        words = paragraph.split()
        processed_words = [self.process_word(word, paragraph) for word in words]
        processed_text = ' '.join(processed_words)
        return self.apply_space_variations(processed_text)

    def process_word(self, word, sentence):
        if len(word) > 1 and random.random() < 0.05:  # 大小写处理概率限制在5%
            word = word[0].swapcase() + word[1:]
        return word



    def apply_space_variations(self, text):
        punctuation = r'[,.\?!:;]'
        parts = re.split(f'({punctuation})', text)
        result = []
        for part in parts:
            if re.match(punctuation, part):
                # 根据原来的概率规则添加空格
                space = self.get_random_space()
                result.append(part + space)
            else:
                result.append(part)
        return ''.join(result).strip()

    def get_space_probability(self):
        return self.current_probability

    def get_random_space(self):
        # 随机返回1到3个空格：33%概率没有空格，33%概率两个空格，33%一个空格，1%三个空格
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
