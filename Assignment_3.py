# CHIRAG SAMAIYA
# 0176CD231051
# LNCTE

logged_user = ''
logged = False
record={}
def register():
    print("__REGISTRATION PAGE__")
    global record
    username=input("Enter your username: ").lower()
    if username in record:
        print("Username already exists")
    else:
        password = input("Enter password: ")
        name = input("Enter your full name: ")
        email = input("Enter your email: ")
        contact= int(input("Enter you contact number: "))
        course=input("Enter you course name: ")
        college= input("Enter the name of your college: ")
        city= input("Enter your city: ")
        record[username] = {'username': username, 'password': password, 'name': name, 'email': email, 'contact': contact, 'course': course, 'college': college, 'city': city }
        print("Registration successful!")
    login()

def login():
    global logged_user
    global logged
    print("__LOGIN PAGE__")
    user=input("Enter your username:").lower()
    if user in record:
        pas=input("Enter your password: ")
        if pas==record[user]['password']:
            logged_user= user
            logged= True
            show_profile()
        else:
            print("Invalid password")
            login()
    else:
        print("Username doesn't exist, please check or register!")
        main()

def show_profile():
    if logged== False:
        print("Please login/register first")
        main()
    else:
        user =record[logged_user]
        print("__STUDENT PROFILE__")
        print(f"Username: {user['username']}")
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Contact: {user['contact']}")
        print(f"Course: {user['course']}")
        print(f"College: {user['college']}")
        print(f"City: {user['city']}")
        main()
        
def update_profile():
    if logged== False:
        print("Please login/register first")
        main()
    else:
        print("__STUDENT PROFILE__")
        user =record[logged_user]
        res=input("Enter what to update: ").lower()
        if res=='username':
            new=input("Enter your username: ").lower()
            if new in record:
                print("Username already exists")
            user=new
        elif res=='name':
            user['name'] = input("Enter new name: ")
        elif res=='email':
            user['email'] = input("Enter new email: ")
        elif res=='contact':
            user['contact'] = int(input("Enter new contact number: "))
        elif res=='course':
            user['course'] = input("Enter new course: ")
        elif res=='college':
            user['college'] = input("Enter new college: ")
        elif res=='city':
            user['city'] = input("Enter new city: ")
        else:
            print("Invalid input")
        print("Profile updated successfully!")
        show_profile()
        
def quiz():
    if not logged:
        print("Please login first.")
        return

    categories = {
        "DSA": [
            {"q1": "Which data structure uses LIFO?", "options": ["A) Queue", "B) Stack", "C) Array", "D) Tree"], "a": "B"},
            {"q2": "What is time complexity of binary search?", "options": ["A) O(n)", "B) O(log n)", "C) O(n^2)", "D) O(1)"], "a": "B"},
            {"q3": "Which data structure uses FIFO?", "options": ["A) Queue", "B) Stack", "C) Tree", "D) Graph"], "a": "A"},
            {"q4": "Which traversal is used in BFS?", "options": ["A) Depth First", "B) Breadth First", "C) Preorder", "D) Inorder"], "a": "B"},
            {"q5": "Which structure is used for recursion?", "options": ["A) Queue", "B) Array", "C) Stack", "D) List"], "a": "C"}
        ],
        "DBMS": [
            {"q1": "What does SQL stand for?", "options": ["A) Structured Query Language", "B) Simple Query Language", "C) Sequence Query Language", "D) Standard Question Language"], "a": "A"},
            {"q2": "Which is a DBMS?", "options": ["A) MySQL", "B) Oracle", "C) PostgreSQL", "D) All of these"], "a": "D"},
            {"q3": "Primary key is used for?", "options": ["A) Uniqueness", "B) Duplication", "C) Indexing", "D) Joining"], "a": "A"},
            {"q4": "Which normal form removes transitive dependency?", "options": ["A) 1NF", "B) 2NF", "C) 3NF", "D) BCNF"], "a": "C"},
            {"q5": "Which command is used to remove a table?", "options": ["A) DELETE", "B) REMOVE", "C) DROP", "D) CLEAR"], "a": "C"}
        ],
        "PYTHON": [
            {"q1": "Who developed Python?", "options": ["A) James Gosling", "B) Guido van Rossum", "C) Dennis Ritchie", "D) Bjarne Stroustrup"], "a": "B"},
            {"q2": "What is the output of print(2**3)?", "options": ["A) 6", "B) 8", "C) 9", "D) 12"], "a": "B"},
            {"q3": "Which keyword defines a function?", "options": ["A) func", "B) define", "C) def", "D) function"], "a": "C"},
            {"q4": "Which of these is a mutable datatype?", "options": ["A) tuple", "B) list", "C) string", "D) frozenset"], "a": "B"},
            {"q5": "Which operator is used for floor division?", "options": ["A) /", "B) //", "C) %", "D) **"], "a": "B"}
        ]
    }

    print("\n__QUIZ CATEGORIES__")
    for cat in categories.keys():
        print("-", cat)
    choice = input("Enter category (DSA/DBMS/PYTHON): ").upper()

    if choice not in categories:
        print("Invalid category.")
        return

    questions = categories[choice]
    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}. {q['q']}")
        for opt in q['options']:
            print(opt)
        ans = input("Enter your answer (A/B/C/D): ").upper()
        if ans == q['a']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {q['a']}")

    print(f"\n Quiz completed! Your score: {score}/{len(questions)}")

            
def logout():
    global logged
    global logged_user
    if not logged:
        print("please login first")
    conf=input("Are you sure you want to logout (Yes/No): ").lower()
    if conf=='yes':
        logged= False
        logged_user= ''
        print("_LOGGED OUT_")
        main()
    else:
        main()
    
def terminate():
    exit()

def main():
    print("__STUDENT REGISTRATION SYSTEM__")
    response = input('''
        Choose option:
        1. Registration
        2. Login
        3. Show profile
        4. Update profile
        5. Logout
        6. Main Menu
        7. Exit

            select option 1/2/3/4/5/6/7: ''')

    if response == '1':
        register()
    elif response == '2':
        login()
    elif response == '3':
        show_profile()
    elif response == '4':
        update_profile()
    elif response == '5':
        if logged==True:
            logout()
        else:
            print("Please login/register first")
            main()
    elif response == '6':
        main()
    elif response == '7':
        terminate()
    else:
        print("Invalid Choice, Please select correct option")
        main()
main()