from conn import konektor
from prettytable import from_db_cursor



def get_users():
    cursor = konektor.cursor()
    sql = "SELECT * FROM test"
    cursor.execute(sql)
    table = from_db_cursor(cursor)
    table.field_names = ["ID", "Jméno", "Příjmení", "Třída"]
    print(table)


def get_users_by_id(id: int):
    cursor = konektor.cursor()
    sql = "SELECT * FROM test WHERE id=%s"
    user = (id, )
    cursor.execute(sql, user)
    table = from_db_cursor(cursor)
    table.field_names = ["ID", "Jméno", "Příjmení", "Třída"]
    print(table)


def printhelp():
    print("\n")
    print("1) Vypiš uživatele podle ID")
    print("2) Vypiš uživatle podle třídy")


if __name__ == "__main__":
    get_users()
    printhelp()
    action = int(input("Vyber možnost ze seznamu: "))

    if action == 1:
        get_users_by_id(1)


