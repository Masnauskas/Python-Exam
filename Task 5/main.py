# Importuokite reikiamus modulius, kad veiktų žemiau nurodytos funkcijos

#importuojami moduliai
from modules.math.composition import composition as addition #skiriasi nuo žemiau parašytos funkcijos, tad importuojama 'as'
from modules.math.subtraction import substraction
from modules.math.division import division as divivsion #skiriasi nuo žemiau parašytos funkcijos, tad importuojama 'as'
from modules.math.multiplication import multiplication #skiriasi nuo žemiau parašytos funkcijos, tad importuojama 'as'

# importuojami kintamieji
from modules.numbers.numbers import one, two, three, four, five


# Matomai viskas kopijuota iš JS, nes su kabliataškiais
# Norėjau pridėti time.sleep(), bet parašyta, kad nekeistume kodo...

# Kitų failų ir žemiau esančio kodo nekeiskite
a = addition(one, four);
b = divivsion(four, two);
c = substraction(three, two);
d = multiplication(five, two);

print(a);
print(b);
print(c);
print(d);
