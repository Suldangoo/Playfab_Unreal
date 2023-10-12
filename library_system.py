from flask import Flask, render_template, request, redirect

app = Flask(__name__) # Flask 사용

# 멤버와 책 정보 저장
members = {}  # {"이름": "전화번호", ...}
books = {}    # {"책 제목": "작가", ...}
borrowed_books = {}  # {"이름": ["책 제목", ...], ...}

@app.route('/')
def index():
    return render_template('index.html', members=members, books=books)

@app.route('/add_member', methods=['POST'])
def add_member():
    name = request.form['name']
    phone = request.form['phone']
    
    # 멤버 추가
    members[name] = phone

    return redirect('/')

@app.route('/delete_member', methods=['POST'])
def delete_member():
    name = request.form['name']
    
    # 멤버 삭제
    if name in members:
        del members[name]

    return redirect('/')

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']

    # 책 추가
    books[title] = {"작가": author, "상태": "대출 가능"}

    return redirect('/')

@app.route('/delete_book', methods=['POST'])
def delete_book():
    title = request.form['title']
    author = request.form['author']

    # 책 삭제: 제목과 작가가 일치하는 경우에만 삭제
    if title in books and books[title]["작가"] == author:
        del books[title]

    return redirect('/')

@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    member_name = request.form['member_name']
    title = request.form['title']

    # 대출 조건: 멤버가 존재하며, 책도 존재하고, 책 상태가 '대출 가능'이어야 함
    if member_name in members and title in books and books[title]["상태"] == "대출 가능":
        books[title]["상태"] = "대출 중"
        if member_name not in borrowed_books:
            borrowed_books[member_name] = []
        borrowed_books[member_name].append(title)

    return redirect('/')

@app.route('/return_book', methods=['POST'])
def return_book():
    member_name = request.form['member_name']
    title = request.form['title']

    # 반납 조건: 멤버가 존재하며, 책도 존재하고, 멤버가 해당 책을 대출 중이어야 함
    if member_name in members and title in books and member_name in borrowed_books and title in borrowed_books[member_name]:
        books[title]["상태"] = "대출 가능"
        borrowed_books[member_name].remove(title)

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
