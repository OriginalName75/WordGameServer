from WordGameServer.settings import BIBLI, POINTS_5, POINTS_4, POINTS_3, \
    POINTS_2
def matrix_checker(cells):
    matr = [0] * 5
    for i in range(5):
        matr[i] = [0] * 5
        for j in range(5):
            matr[i][j] = "_"
    for c in cells:
        matr[c.row][c.col] = c.letter 
    
    return _matrix_checker(matr)
    
    
def _matrix_checker(matr):
    answer = []
    points = _matrix_checker_aux(matr, answer)
    matr = _reverse_matr(matr)
    points = _matrix_checker_aux(matr, answer, points = points,reverse = True )
    
    return {"points" : points, "dots": answer}
def _reverse_matr(matr):
    a = [0] * 5
    for i in range(5):
        a[i] = [0] * 5
    
    for i in range(5):
        for j in range(5):
            a[i][j] = matr[j][i]
    
    return a
def _matrix_checker_aux(matr, answer, points = 0, reverse = False):
    
    
    index_line = 0
    for m in matr:
        line = ""
        for n in m:
            line += n
        is_word = BIBLI.check(line)
        
        if is_word:
            points += POINTS_5
            answer.append({"line" : reverse, "i" : 0, "j": 4, "index_line": index_line})
        
        else:
            l = [[0,3], [1,4]]
            break_line = False
            for indexes in l:
                i = indexes[0]
                j = indexes[1]
                is_word = BIBLI.check(line[i:j+1])
                if is_word:
                    points += POINTS_4
                    answer.append({"line" : reverse, "i" : i, "j": j, "index_line": index_line})
                    
                    break_line = True
                    break
            if not break_line:
                
                l = [[0,2], [1,3], [2,4]]
               
                for indexes in l:
                    i = indexes[0]
                    j = indexes[1]
                    is_word = BIBLI.check(line[i:j+1])
                    if is_word:
                        points += POINTS_3
                        answer.append({"line" : reverse, "i" : i, "j": j, "index_line": index_line})
                        break_line = True
                        
                        break

            
            
      
        index_line += 1
    return points
        
        
        