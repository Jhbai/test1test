import sys
import run_cython


print(run_cython.fibo(int(sys.argv[1])))
