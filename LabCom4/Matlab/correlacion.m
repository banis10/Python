N = 100;
x = 0 :1/N:1;

y = sin(100*2*pi*x);
y1 = sin(200*2*pi*x);
y2 = sin(300*2*pi*x);
y3 = sin(400*2*pi*x);
 
c = xcorr(y,y,'coeff');
c1 = xcorr(y,y1,'coeff');
c2 = xcorr(y,y2,'coeff');
c3 = xcorr(y,y3,'coeff');
 
max(c)
max(c1)
max(c2)
max(c3)

