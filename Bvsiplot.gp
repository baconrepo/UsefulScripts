
set autoscale

f(x)=a*x
fit f(x) 'BvsI.txt' using 1:3 via a
plot 'BvsI.txt' using 1:3:2:4 with xyerrorbars title 'Data', f(x) title 'fit line'
set title 'B[mT] vs Current[A]'
set xlabel 'Current(A)'
set ylabel 'B Field Strength (mT)'
set term jpeg
set out 'BvsI.jpg'
replot
set term qt
quit

