plot 'BvsX.txt' using 2:1:4:3 with xyerrorbars
set autoscale

set title 'B[mT] vs Position[cm]'
set xlabel 'Position (cm)'
set ylabel 'B Field Strength (mT)'
set term jpeg
set out 'BvsX.jpg'
replot
set term qt
quit

