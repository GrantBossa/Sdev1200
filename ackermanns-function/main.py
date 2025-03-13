#
# Name
# Date
# Ackermann's Function Programming Project
# SDEV 1200
#
'''
`If m = 0 then return n + 1 
If n = 0 then return ackermann(m - 1, 1) 
Otherwise, return ackermann(m - 1, ackermann(m, n - 1))`
'''
def A(m,n):
    if m == 0 :
        return n + 1 
    if n == 0 :
        return A(m - 1, 1) 
    else:
        return A(m - 1, A(m, n - 1))
 
def main():
    # Initial Variables
    try :
        m = int(input("Please enter the m value: "))
        n = int(input("Please enter the n value: "))
        z = A(m, n)
        print(f"The Ackermann value is {z}")
    except Exception as e:
        print(f" {Exception}: {e}")
        
# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == "__main__":
    main()
