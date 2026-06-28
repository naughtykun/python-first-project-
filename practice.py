input("""Welcome to the program
-----------------------
press s to start:  """)

dialPad = ((1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            ("*", 0, "#"))

    
for cols in dialPad:
    for rows in cols:
        print(rows, end = " ")
    print()