
# This file was *autogenerated* from the file KnutsonTaoPuzzleSolver.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_0 = Integer(0); _sage_const_5 = Integer(5)
from sage.combinat.knutson_tao_puzzles import KnutsonTaoPuzzleSolver
ps=KnutsonTaoPuzzleSolver('HT')
solns=ps('0101', '0101')
ps.plot(solns).show()
plot(x**_sage_const_2 ,(x,_sage_const_0 ,_sage_const_5 )).save("my_plot.png")





