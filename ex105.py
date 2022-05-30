grades = dict()


def grade(*g, sit=False):

    grades['total'] = len(g)
    grades['highest grade'] = max(g)
    grades['lowest grade'] = min(g)
    grades['average grade'] = sum(g) / len(g)
    if sit:
        if grades['average grade'] < 5:
            grades['situation'] = 'awful'
        if grades['average grade'] > 5 and grades['average grade'] < 8:
            grades['situation'] = 'Good'
        if grades['average grade'] > 8:
            grades['situation'] = 'Amazing'
    return grades


results = grade(5.5, 9.5, 10, 6.5, sit=True)
print(results)