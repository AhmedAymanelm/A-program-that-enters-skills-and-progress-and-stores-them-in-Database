import sqlite3
db = sqlite3.connect('data.db')
cr = db.cursor()
user_msg=("""
what Do you want ?

s => show skills
a => show skills
d => delete skills
u => update skills
q=> quit the app
choose option: 
"""
)
uid=9
user_in = input(user_msg)
def commit_and_close():
    db.commit()
    db.close()
    print("The approval has been completed and the connection has been closed")

def add_skill():
    skill_name = str(input("Please enter the skill: ")).capitalize().strip()
    cr.execute(f"select name from skills where name = '{skill_name}' and user_id = {uid}")
    result = cr.fetchone()
    if result ==None:
       prog = int(input("Please enter progress: "))
       cr.execute(f"insert into skills(name,progress,user_id) values('{skill_name}','{prog}%',{uid}) ")
       print("The skill has been added successfully")
       commit_and_close()
    else:
        print("This skill exists, you cannot add it again")
        add_and_up = input("Do you want to change it? (y or n)")
        if add_and_up == 'y':
            update_skill()
        elif add_and_up == 'n':
            print("okay see you")
        else:
            print("Wrong choice, please choose the correct option")
            commit_and_close()

def delete_skill():
    skill_name = str(input("Please enter the skill: ")).capitalize().strip()
    cr.execute(f"DELETE FROM skills where name='{skill_name}' and user_id = {uid}")
    print("The skill has been deleted successfully")
    commit_and_close()

def update_skill():
    skill_name = str(input("Please enter the skill: ")).capitalize().strip()
    new_prog = int(input("Please enter  a new progress: "))
    cr.execute(f"update skills set progress='{new_prog}%'  where name = '{skill_name}' and user_id = {uid} ")
    print("The skill has been update successfully")
    commit_and_close()

def show_skill():
    cr.execute(f"select * from skills where user_id={uid}")
    result = cr.fetchall()
    print(f"you have {len(result)} skills")

    if len(result)>0:
       print("These are your skills")
       for row in result:
           print(f"the skills is =>{row[1]}", end=' ')
           print(f"the progress is =>{row[2]}")

    else:
        print("You don't have any skill")
        addition = input("Do you want to add any skill? (y or n): ").strip().lower()

        if addition == 'y':
            add_skill()
        elif addition == 'n':
            print("Well, the program has been stopped")
        else:
            print("Wrong choice, please choose the correct option")
        commit_and_close()


commend_list = ['s','a','d','u','q']
if user_in in commend_list:
    if user_in == "s":
        show_skill()

    elif user_in == 'a':
        add_skill()

    elif user_in == 'd':
        delete_skill()

    elif user_in == 'u':
        update_skill()

    else:
        print("the app is closed")



else:
    print("Wrong choice, please choose the correct option")






