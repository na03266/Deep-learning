import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QMessageBox, QMenu

class MinesweeperGame(QMainWindow):
    def __init__(self, rows, cols, mines):
        super().__init__()

        # 게임 설정 초기화
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.remaining_tiles = rows * cols - mines
        self.game_over = False


        # UI 초기화
        self.init_ui()

    def init_ui(self):
        # 윈도우 설정
        self.setWindowTitle("지뢰찾기")
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout()

        # 버튼 그리드 생성
        for r in range(self.rows):
            for c in range(self.cols):
                self.buttons[r][c] = QPushButton(self)
                self.buttons[r][c].setFixedSize(40, 40)
                self.buttons[r][c].setCheckable(True)
                self.buttons[r][c].clicked.connect(lambda state, row=r, col=c: self.tile_clicked(row, col))
                self.buttons[r][c].setContextMenuPolicy(Qt.CustomContextMenu)  # 우클릭 메뉴 설정
                self.buttons[r][c].customContextMenuRequested.connect(lambda pos, row=r, col=c: self.show_context_menu(pos, row, col))  # 우클릭 메뉴 이벤트 연결
                self.grid_layout.addWidget(self.buttons[r][c], r, c)

        self.central_widget.setLayout(self.grid_layout)
        self.place_mines()
        self.calculate_numbers()

    def show_context_menu(self, pos, row, col):
        if not self.game_over and not self.revealed[row][col]:
            self.buttons[row][col].setDown(True)  # 버튼을 누른 상태로 변경하여 효과 표시
            menu = QMenu(self)
            flag_action = menu.addAction("깃발 표시")
            action = menu.exec_(self.buttons[row][col].mapToGlobal(pos))
            if action == flag_action:
                self.toggle_flag(row, col)
            self.buttons[row][col].setDown(False)  # 버튼을 누른 상태 해제


    def toggle_flag(self, row, col):
        if self.buttons[row][col].text() == '':
            self.buttons[row][col].setText('F')
        else:
            self.buttons[row][col].setText('')

    def place_mines(self):
        # 지뢰 배치
        mine_positions = random.sample(range(self.rows * self.cols), self.mines)
        for position in mine_positions:
            row = position // self.cols
            col = position % self.cols
            self.board[row][col] = 'X'

    def calculate_numbers(self):
        # 주변 지뢰 개수 계산
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == 'X':
                    continue
                count = 0
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if 0 <= r + dr < self.rows and 0 <= c + dc < self.cols:
                            if self.board[r + dr][c + dc] == 'X':
                                count += 1
                self.board[r][c] = count

    def tile_clicked(self, row, col):
        if self.game_over:
            return

        if self.revealed[row][col]:
            return

        self.revealed[row][col] = True
        self.buttons[row][col].setChecked(True)

        if self.board[row][col] == 'X':
            self.buttons[row][col].setText('X')
            self.end_game(False)
        else:
            self.remaining_tiles -= 1
            self.buttons[row][col].setText(str(self.board[row][col]))
            self.buttons[row][col].setEnabled(False)
            if self.board[row][col] == 0:
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if 0 <= row + dr < self.rows and 0 <= col + dc < self.cols:
                            if not self.revealed[row + dr][col + dc]:
                                self.tile_clicked(row + dr, col + dc)
            if self.remaining_tiles == 0:
                self.end_game(True)

    def end_game(self, is_winner):
        # 게임 종료 처리
        self.game_over = True
        if is_winner:
            message = "축하합니다! 승리하셨습니다."
        else:
            message = "지뢰를 밟았습니다. 게임 오버."
            self.reveal_all_mines()  # 게임 종료 시 모든 지뢰를 표시

        result = QMessageBox.information(self, "게임 종료", message, QMessageBox.Ok | QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            self.restart_game()
        else:
            sys.exit()

    def reveal_all_mines(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == 'X':
                    self.buttons[r][c].setText('X')

    def restart_game(self):
        self.init_game()
        for r in range(self.rows):
            for c in range(self.cols):
                self.buttons[r][c].setEnabled(True)
                self.buttons[r][c].setText('')
                self.buttons[r][c].setChecked(False)
                self.revealed[r][c] = False


def main():
    app = QApplication(sys.argv)
    game = MinesweeperGame(rows=10, cols=10, mines=20)
    game.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
