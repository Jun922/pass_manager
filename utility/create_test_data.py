import os
from datetime import datetime


class Data:
    def __init__(self, table):
        self.table = table
        self.sql = ["INSERT INTO pw_recorder_app ('id', 'name', 'password', 'created_at', 'updated_at') values",]
        
    def into_vals(self, id, name, pw):
        now = datetime.now()
        self.sql.append(fr"({id}, '{name}', '{pw}', '{now}', '{now}'),")

    
    def output_sql_file(self):
        path = f"{os.getcwd()}/utility/insert.sql"
        with open(path, mode="a", encoding="utf-8") as file:
            for val in self.sql[2:]:
                file.write(f"\n{val}")

        for num, val in enumerate(self.sql):
            if num == 0:
                with open(path, mode="w", encoding="utf-8") as file:
                    file.writelines(val)
            else:
                with open(path, mode="a", encoding="utf-8") as file:
                    if num == len(self.sql)-1:
                        file.write(f"\n{val[:-1]}")
                    else:
                        file.write(f"\n{val}")



def main():
    table = "pw_recorder_app"
    obj = Data(table)
    for loop in range(1, 51):
        tmp = str(loop).zfill(3)
        obj.into_vals(loop, f"site{tmp}", tmp)
    obj.output_sql_file()


if __name__ == "__main__":
    main()