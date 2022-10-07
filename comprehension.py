import sys

def main(text, *args):
    my_ints = sys.argv[1:]
    x = list(map(int, my_ints))
    
    y = [i * 10 if i % 3 == 0 else i for i in x]
                
        
    return(y)
    
print(main(sys.argv[1:]))