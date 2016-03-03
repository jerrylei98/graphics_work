import math

def make_translate( x, y, z ):
    m = [[x],[y],[z],[1]]
    return m

def make_scale( x, y, z ):
    pass
    
def make_rotX( theta ):   
    pass

def make_rotY( theta ):
    pass

def make_rotZ( theta ):
    pass

def new_matrix(rows = 4, cols = 4):
    #given
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    #works
    c1 = 0 #row counter
    while c1 < len(matrix):
        s = "["
        c2 = 0 #column counter
        while c2 < len(matrix[0]):
            s += " " + str(matrix[c1][c2]) 
            c2 += 1
        s += " ]"
        print s
        c1 += 1

    
def ident( matrix ):
    #works
    c1 = 0
    while c1 < len(matrix):
        c2 = 0
        while c2 < len(matrix[0]):
            if c1 == c2:
                matrix[c1][c2] = 1
            else:
                matrix[c1][c2] = 0
            c2+=1
        c1+=1
    return matrix

def scalar_mult( matrix, x ):
    #works
    c1 = 0
    while c1 < len(matrix):
        c2 = 0
        while c2 < len(matrix[0]):
            matrix[c1][c2] = matrix[c1][c2] * x
            c2 += 1
        c1+=1
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m_fill = new_matrix(len(m1), len(m2[0]))
    c1 = 0
    while c1 < len(m_fill):
        c2 = 0
        while c2 < len(m_fill[0]):
            pass


m_test = new_matrix(4, 2)
m_test[0][0] = 5
m_test[0][1] = 3
m_test[0][2] = 7
m_test[0][3] = 12
m_test[1][0] = 2
m_test[1][1] = 4
m_test[1][2] = 9
m_test[1][3] = 8
print print_matrix(m_test)


print print_matrix(make_translate(4,5,6))
