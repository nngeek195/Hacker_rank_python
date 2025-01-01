import cmath

def process(z):
    size = abs(z)
    angle = cmath.phase(z)
    print(size)
    print(angle)
    
    
    
if __name__=='__main__':
    userIN = input()
    z = complex(userIN)
    process(z)
    
