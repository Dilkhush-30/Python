"""  
 +----------+----------+---------+-------+
|   Name   | Semester | Subject | Marks |
+----------+----------+---------+-------+
| Dilkhush |   4th    |   DBMS  |   55  |
|   Alka   |   4th    |   DSA   |   32  |
| Anupriya |   4th    |   O.S   |   36  |
+----------+----------+---------+-------+
"""

from prettytable import PrettyTable
table = PrettyTable(["Name","Semester","Subject","Marks"])
table.add_row(["Dilkhush","4th","DBMS","55"])
table.add_row(["Alka","4th","DSA","32"])
table.add_row(["Anupriya","4th","O.S","36"])
print(table)