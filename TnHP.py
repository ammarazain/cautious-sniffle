def nthHarmonic(N) :  
    harmonic = 1.00
    for i in range(2, N + 1) : 
        harmonic += 1 / i 
    return harmonic     
if _name_ == "_main_" : 
  
    N = 8
    print(round(nthHarmonic(N),5)) 
  
