from conn import konektor


def Get_Users():
    cursor = konektor.cursor()
    sql = "SELECT * FROM test"
    cursor.execute(sql)
    result = cursor.fetchall()

    print("ID\t Jméno\t Příjmení\t Třída\t")
    for item in result:
        print(f"{item[0]}\t {item[1]}\t {item[2]}\t {item[3]}\t")

def Get_Users_By_ID(id: int):
    cursor = konektor.cursor()
    sql = "SELECT * FROM test WHERE id=?"
    data = (id, )
    cursor.execute(sql, data)
    result = cursor.fetchall()

    print("ID\t Jméno\t Příjmení\t Třída\t")
    for item in result:
        print(f"{item[0]}\t {item[1]}\t {item[2]}\t {item[3]}\t")



def PrintHelp():
    print("\n")
    print("1) Vypiš uživatele podle ID")
    print("2) Vypiš uživatle podle třídy")


if __name__ == "__main__":
    Get_Users()
    PrintHelp()
    action = int(input("Vyber možnost ze seznamu: "))

    if action == 1:
        Get_Users_By_ID(1)


