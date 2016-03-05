import math

def cos_trunc(theta):
    j = math.cos(theta)
    return float('%.3f' % j)

def sin_trunc(theta):
    j = math.sin(theta)
    return float('%.3f' % j)

def degree2radian(theta):
    conv = math.pi/180
    return theta * conv

def make_translate( x, y, z ):
    return [[1,0,0,x],
            [0,1,0,y],
            [0,0,1,z],
            [0,0,0,1]]
    

def make_scale( x, y, z ):
    return [[x,0,0,0],
            [0,b,0,0],
            [0,0,z,0],
            [0,0,0,1]]
    
def make_rotX( theta ):   
    return [[1,0,0,0],
            [0,cos_trunc(theta),-sin_trunc(theta),0],
            [0,sin_trunc(theta),cos_trunc(theta),0],
            [0,0,0,1]]

def make_rotY( theta ):
    return [[cos_trunc(theta),0,-sin_trunc(theta),0],
            [0,1,0,0],
            [sin_trunc(theta),0,cos_trunc(theta),0],
            [0,0,0,1]]

def make_rotZ( theta ):
    return [[cos_trunc(theta),-sin_trunc(theta),0,0],
            [sin_trunc(theta),cos_trunc(theta),0,0],
            [0,0,1,0],
            [0,0,0,1]]

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
        c2 = 0 #column counter
        s = ''
        while c2 < len(matrix[0]):
            s += "\t" + str(matrix[c1][c2]) + "\t"
            c2 += 1
        if c1 == 0:
            print u'\u23A1' + s + u'\u23A4'
        elif c1 == len(matrix) -1 :
            print u'\u23A3' + s + u'\u23A6' + '\n'
        else:
            print u'\u23A2' + s + u'\u23A5'
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
            matrix[c1][c2] *=  x
            c2 += 1
        c1+=1
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    
    if not len(m1[0]) == len(m2):
        print "Matrices cannot be multiplied.\n"
        return []
    
    m_fill = new_matrix(len(m2[0]), len(m1))
    c1 = 0
    while c1 < len(m1):
        c2 = 0
        while c2 < len(m2[0]):
            s = 0
            c3 = 0
            while(c3 < len(m2)):
                s += m1[c1][c3] * m2[c3][c2]
                c3 += 1
            m_fill[c1][c2] = int(s)
            c2 += 1
        c1+= 1
    return m_fill


"""
Testing:

m1 = new_matrix(3,2)
m1[0][0] = 1
m1[0][1] = 2
m1[0][2] = 3
m1[1][0] = 4
m1[1][1] = 5
m1[1][2] = 6

print_matrix(m1)
m2 = new_matrix(2,4)
m2[0][0] = 7
m2[0][1] = 8
m2[1][0] = 9
m2[1][1] = 10
m2[2][0] = 11
m2[2][1] = 12

print_matrix(m2)

print_matrix(matrix_mult(m2, m1))

"""
