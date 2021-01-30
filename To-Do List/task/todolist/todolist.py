# Write your code here
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
today = datetime.today()


def find_and_print_todos_on(on_day):
    rows_found = session.query(Table).filter(Table.deadline == on_day.date()).all()
    if len(rows_found) == 0:
        print("Nothing to do!")
    else:
        for row_index, row_task in enumerate(rows_found):
            print(f'{row_index + 1}. {row_task.task}')


while True:
    print("""1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit""")

    choice = int(input())
    if choice == 0:
        print("\nBye!")
        break
    elif choice == 1:
        print(f"\nToday {datetime.strftime(today, '%d %b')}:")
        find_and_print_todos_on(today)
        print()
    elif choice == 2:
        day_of_week = today.weekday()
        for i in range(0, 7):
            day = (today + timedelta(days=i))
            print(datetime.strftime(day, "\n%A %d %b:"))
            find_and_print_todos_on(day)
        print()
    elif choice == 3:
        print("\nAll tasks:")
        rows = session.query(Table).order_by(Table.deadline).all()

        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for index, row in enumerate(rows):
                print(f'{index + 1}. {row.task}. '
                      f'{row.deadline.day} {row.deadline.strftime("%b")}')
        print()
    elif choice == 4:
        print("\nMissed tasks:")
        rows = session.query(Table).filter(Table.deadline < today.date())\
            .order_by(Table.deadline).all()

        if len(rows) == 0:
            print("Nothing is missed!")
        else:
            for index, row in enumerate(rows):
                print(f'{index + 1}. {row.task}. {datetime.strftime(row.deadline, "%d %b")}')

        print()
    elif choice == 5:
        task = input("\nEnter task\n")
        deadline = input("Enter deadline\n")
        year, month, day = deadline.split("-")
        new_row = Table(task=task, deadline=datetime(int(year), int(month), int(day)))
        session.add(new_row)
        session.commit()
        print("The task has been added!\n")
    elif choice == 6:
        rows = session.query(Table).order_by(Table.deadline).all()

        if len(rows) == 0:
            print("\nNothing to delete")
        else:
            row_ids = []
            print("\nChoose the number of the task you want to delete:")
            for index, row in enumerate(rows):
                print(f'{index + 1}. {row.task}. {datetime.strftime(row.deadline, "%d %b")}')
                row_ids.append(row.id)

            del_index = int(input())
            session.query(Table).filter(Table.id == row_ids[del_index - 1]).delete()
            session.commit()
            print("The task has been deleted!")

        print()

