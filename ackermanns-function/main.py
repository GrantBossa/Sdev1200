#
# Grant Bossa
# March 15, 2025
# Ackermann's Function Programming Project
# SDEV 1200
#
'''
# Instructions  

Ackermann's Function is a recursive mathematical algorithm that can be used to test how well a system optimizes its 
performance of recursion. Design a function `ackermann(m, n)`, which solves Ackermann�s function. Use the following 
logic in your function:

`If m = 0 then return n + 1 
If n = 0 then return ackermann(m - 1, 1) 
Otherwise, return ackermann(m - 1, ackermann(m, n - 1))`

Once you�ve designed your function, test it by calling it with small values for m and n.
'''

def ackermann(m,n):
    if m == 0 :
        return n + 1 
    if n == 0 :
        return ackermann(m - 1, 1) 
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
 
def main():
    # error handling is for exiting nicely for recursion errors.
    try :
        m = int(input("Please enter the m value: "))
        n = int(input("Please enter the n value: "))
        z = ackermann(m, n)
        print(f"The Ackermann value is {z}")

    except Exception as e:
        print(f" {Exception}: {e}")
        
# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__":
    main()
