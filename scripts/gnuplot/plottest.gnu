# Note you need gnuplot 4.4 for the pdfcairo terminal.

#set terminal pdfcairo
set terminal pdfcairo size 12cm,7.3cm font "Helvetica,11" linewidth 4 rounded
set output "test.pdf"

# left bottom right top radiusX radiusY x's
f_low(a,b,c,d,rx,ry,x)=a<x && x<a+rx ? \
     -ry*sqrt(1-((x-a-rx)/rx)**2)+b+ry : \
     a+rx<x && x<c-rx ? b :c-rx<x && x<c ?\
     -ry*sqrt(1-((x-c+rx)/rx)**2)+b+ry : 1/0

f_up(a,b,c,d,rx,ry,x)=a<x && x<a+rx ?\
     ry*sqrt(1-((x-a-rx)/rx)**2)+d-ry : \
     a+rx<x && x<c-rx ? d :c-rx<x && x<c ?\
     ry*sqrt(1-((x-c+rx)/rx)**2)+d-ry : 1/0

# axis
set style line 80 lt rgb "#3F3F3F"
# grid
set style line 81 lt 0  # dashed
set style line 81 lt rgb "#808080"  # grey
set grid back linestyle 81

set border 3 back linestyle 80 lt 1 lc rgb "#3F3F3F"

set xtics nomirror
set ytics nomirror

#set border 31 front linestyle 80
set style fill transparent solid 0.25
set style function filledcurves y1=0
set clip two

set style line 1 lt rgb "#25FF0000" lw 0.8 pt 0
set style line 2 lt rgb "#FF0000" lw 0 pt 2

set key box ls 80 linewidth 0.7
set key noinvert spacing 1.2 width 0 height 0.2

set xrange [2250:10250]
set xtics 500
set ytics 0.005
set yrange [0:0.0625]
set xtic rotate by -45

set boxwidth 250 absolute

set sample 1000
unset colorbox

delta=0.0005


# num:              1   2             3               4               5               6
# data:             x   whisker_min   box_min         mean            box_high        whisker_high
# whisker plot:     x   box_min       whisker_min     whisker_high    box_high
plot "test.dat" using 1:3:2:6:5:xtic(1) with candlesticks ls 2 notitle, \
    "" using 1:4:2:6:4:(75) with candlesticks ls 1 title '10% Knotenänderung' whiskerbars, \
    "" using ($1-125):($5):(250):(0) with vec nohead ls 1 notitle, \
    "" using ($1-125):($3):(250):(0) with vec nohead ls 1 notitle, \
    "" using ($1-125):($5):(0):($5 - $3 > delta ? -delta : $3 - $5) with vec nohead ls 1 notitle, \
    "" using ($1+125):($5):(0):($5 - $3 > delta ? -delta : $3 - $5) with vec nohead ls 1 notitle, \
    "" using ($1-125):($3):(0):($5 - $3 > delta ? delta : $5 - $3) with vec nohead ls 1 notitle, \
    "" using ($1+125):($3):(0):($5 - $3 > delta ? delta : $5 - $3) with vec nohead ls 1 notitle
