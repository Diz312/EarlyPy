__author__ = "Ismar Dupanovic"

rows=5
columns=5


def diag_mtrx(row, col):
    return 1 if row == col else 0

def rev_mtrx(row,col):
    return 1 if row + col == columns - 1 else 0

def create_mtrx(rows, columns, set_cell):
    return [[set_cell(row,col) for col in range(columns)] for row in range (rows)]

A=create_mtrx(rows,columns,rev_mtrx)

for x in A:
    print x