##plot of T vs L

set xlabel 'Length of String (cm)'
set ylabel 'Period (s)'
set title 'T vs L'
set key top left

#set xrange[0:5]
#set yrange[0:10]

set autoscale

f(x) = s*x
fit f(x) 'Data01.txt' using 4:3:6:8 xyerror via s

plot 'Data01.txt' using 4:5:6:9 title 'Data points' with xyerrorbars, f(x) title 'fit s=0.0385741'


set term jpeg
set output 'TPlot.jpg'
replot
set term qt
quit

