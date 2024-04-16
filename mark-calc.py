marks = [
        ("example year", 1, [
            ("module one", 0.4, [
                ("assignment one", 0.15, 100),
                ("assignment two", 0.85, 100)
                ]),
            ("module two", 0.6, ("exam", 1, 100))
            ])
        ]
'''This uses a recursive algorithm to calculate overall mark from weighted 
marks as long as your marks are in the format (name, weight, mark) where 
mark can be a list, tuple or ultimately, an int. weightings should sum to 
1 on each level.'''


def recurseMark(marks):
    match marks:
        case list():
            return sum(map(recurseMark, marks))
        case (n, w, m):
            return w * recurseMark(m)
        case int():
            return marks


print(recurseMark(marks))
