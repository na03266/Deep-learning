import tkinter as tk
from tkinter import ttk, messagebox

# 도서 목록을 저장할 딕셔너리 생성
library = {}

# 대출한 도서를 저장할 딕셔너리 생성
borrowed_books = {}

# 도서 추가 함수
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    isbn = isbn_entry.get()
    
    if isbn and title and author:
        library[isbn] = {"title": title, "author": author, "is_borrowed": False}
        update_listbox()
        clear_entries()
    else:
        messagebox.showwarning("경고", "도서 정보를 모두 입력하세요.")

# 도서 검색 함수
def search_book():
    isbn = isbn_entry.get()
    book = library.get(isbn)
    
    if book:
        title_label.config(text="도서 제목: " + book["title"])
        author_label.config(text="저자: " + book["author"])
        if book["is_borrowed"]:
            status_label.config(text="대출 상태: 대출 중")
        else:
            status_label.config(text="대출 상태: 대출 가능")
    else:
        messagebox.showinfo("알림", "해당 ISBN으로 등록된 도서가 없습니다.")
        clear_labels()

# 도서 대출 함수
def borrow_book():
    isbn = isbn_entry.get()
    book = library.get(isbn)
    
    if book:
        if book["is_borrowed"]:
            messagebox.showinfo("알림", "이미 대출 중인 도서입니다.")
        else:
            book["is_borrowed"] = True
            borrowed_books[isbn] = book
            update_listbox()
            search_book()
            clear_entries()
    else:
        messagebox.showinfo("알림", "해당 ISBN으로 등록된 도서가 없습니다.")

# 도서 반납 함수
def return_book():
    isbn = isbn_entry.get()
    book = borrowed_books.get(isbn)
    
    if book:
        book["is_borrowed"] = False
        del borrowed_books[isbn]
        update_listbox()
        search_book()
        clear_entries()
    else:
        messagebox.showinfo("알림", "대출 중인 도서 목록에 없습니다.")
        clear_entries()

# 목록 업데이트 함수
def update_listbox():
    book_listbox.delete(*book_listbox.get_children())
    for isbn, book in library.items():
        status = "대출 중" if book["is_borrowed"] else "대출 가능"
        book_listbox.insert("", "end", values=(isbn, book["title"], book["author"], status))

# 엔트리 내용 지우는 함수
def clear_entries():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    isbn_entry.delete(0, tk.END)

# 레이블 내용 지우는 함수
def clear_labels():
    title_label.config(text="")
    author_label.config(text="")
    status_label.config(text="")

# 메인 윈도우 생성
window = tk.Tk()
window.title("도서 관리 프로그램")
window.configure(bg="white")

# 스타일 설정
style = ttk.Style()
style.configure("TButton", foreground="black", background="white")
style.configure("TLabel", foreground="black", background="white")

# 입력 위젯 및 버튼 생성
title_label = ttk.Label(window, text="도서 관리 프로그램", font=("Arial", 16), background="white")
title_entry = ttk.Entry(window, width=40, font=("Arial", 12))
title_label_entry = ttk.Label(window, text="도서 제목", background="white")
author_entry = ttk.Entry(window, width=40, font=("Arial", 12))
author_label_entry = ttk.Label(window, text="저자", background="white")
isbn_entry = ttk.Entry(window, width=20, font=("Arial", 12))
isbn_label_entry = ttk.Label(window, text="도서 ISBN", background="white")
add_button = ttk.Button(window, text="도서 추가", command=add_book, style="TButton")
search_button = ttk.Button(window, text="도서 검색", command=search_book, style="TButton")
borrow_button = ttk.Button(window, text="대출", command=borrow_book, style="TButton")
return_button = ttk.Button(window, text="반납", command=return_book, style="TButton")

# 도서 목록 트리뷰 생성
book_listbox = ttk.Treeview(window, columns=("ISBN", "Title", "Author", "Status"), show="headings", height=10)
book_listbox.heading("ISBN", text="ISBN")
book_listbox.heading("Title", text="Title")
book_listbox.heading("Author", text="Author")
book_listbox.heading("Status", text="Status")
book_listbox.column("ISBN", width=150)
book_listbox.column("Title", width=300)
book_listbox.column("Author", width=200)
book_listbox.column("Status", width=100)

# 위젯 배치
title_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
title_label_entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")
title_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=5)
author_label_entry.grid(row=2, column=0, padx=10, pady=5, sticky="w")
author_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=5)
isbn_label_entry.grid(row=3, column=0, padx=10, pady=5, sticky="w")
isbn_entry.grid(row=3, column=1, padx=10, pady=5)
add_button.grid(row=3, column=2, padx=10, pady=5)
search_button.grid(row=3, column=3, padx=10, pady=5)
borrow_button.grid(row=4, column=2, padx=10, pady=5)
return_button.grid(row=4, column=3, padx=10, pady=5)
book_listbox.grid(row=5, column=0, columnspan=4, rowspan=3, padx=10, pady=10, sticky="nsew")

# 스크롤바 추가
scrollbar = ttk.Scrollbar(window, orient="vertical", command=book_listbox.yview)
scrollbar.grid(row=5, column=4, rowspan=3, sticky="ns")
book_listbox.configure(yscrollcommand=scrollbar.set)

# 메인 루프 시작
update_listbox()
window.mainloop()
