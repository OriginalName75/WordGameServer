from WordGameServer.settings import BIBLI, POINTS_5, POINTS_4, POINTS_3, \
    POINTS_2

def matrix_checker(matr):
    answer = []
    points = matrix_checker_aux(matr, answer)
    matr = reverse_matr(matr)
    points = matrix_checker_aux(matr, answer, points = points,reverse = True )
    
    return {"points" : points, "dots": answer}
def reverse_matr(matr):
    a = [0] * 5
    for i in range(5):
        a[i] = [0] * 5
    
    for i in range(5):
        for j in range(5):
            a[i][j] = matr[j][i]
    
    return a
def matrix_checker_aux(matr, answer, points = 0, reverse = False):
    
    
    index_line = 0
    for m in matr:
        line = ""
        for n in m:
            line += n
        is_word = BIBLI.check(line)
        
        if is_word:
            points += POINTS_5
            if reverse:
                answer.append([[0, index_line], [4, index_line]])
            else:
                answer.append([[index_line, 0], [index_line, 4]])
            break
        l = [[0,3], [1,4]]
        break_line = False
        for indexes in l:
            i = indexes[0]
            j = indexes[1]
            is_word = BIBLI.check(line[i:j+1])
            if is_word:
                points += POINTS_4
                if reverse:
                    answer.append([[i, index_line], [j, index_line]])
                else:
                    answer.append([[index_line, i], [index_line, j]])
                
                break_line = True
                break
        if break_line:
            break
        l = [[0,2], [1,3], [2,4]]
        is_first = True
        for indexes in l:
            i = indexes[0]
            j = indexes[1]
            is_word = BIBLI.check(line[i:j+1])
            if is_word:
                points += POINTS_3
                if reverse:
                    answer.append([[i, index_line], [j, index_line]])
                else:
                    answer.append([[index_line, i], [index_line, j]])
                break_line = True
                if is_first:
                    is_word = BIBLI.check(line[3:5])
                    if is_word:
                        
                        points += POINTS_2
                        if reverse:
                            answer.append([[3, index_line], [4, index_line]])
                        else:
                            answer.append([[index_line, 3], [index_line, 4]])
                break
            is_first = False
        if break_line:
            break
        l = [[0,1], [1,2], [2,3], [3,4]]
        for indexes in l:
            i = indexes[0]
            j = indexes[1]
            is_word = BIBLI.check(line[i:j+1])
            if is_word:
                points += POINTS_2
                if reverse:
                    answer.append([[i, index_line], [j, index_line]])
                else:
                    answer.append([[index_line, i], [index_line, j]])
    return points
        
        
        