clear;
clc;
fsamp = 44100; %Frecuencia de sampleo
fcuts = [2000 3000]; 
%Fpass limite de la banda de paso
%Fstop comienzo de la banda eliminada
mags = [1 0];
devs = [0.891 0.001];
%Apass atenuación en el limite de la banda de paso
%Astop atenuación en el comienzo de la banda eliminada

load handel.mat
t = (0:length(y)-1)/Fs;
[n,Wn,beta,ftype] = kaiserord(fcuts,mags,devs,fsamp);
% n = orden del filtro
% beta = el factor de forma
% Wn =  restricciones de frecuencia
%ftype = tipo de filtro
L = length(t);
bhi = fir1(n,Wn,ftype,kaiser(n+1,beta),'noscale');
outhi = filter(bhi,1,y);

subplot(3,2,1)
plot(t,y)
title('Señal original')
ys = ylim;

subplot(3,2,3)
plot(t,outhi)
title('Señal Filtro ventana Kaiser')
xlabel('Time (s)')
ylim(ys)

%Filtro Chebyshev
[b,a] = cheby1(6,60,0.891);
%Coeficientes de función de transferencia
dataOut = filter(b,a,y);

subplot(3,2,5)
plot(t,dataOut)
title('Señal Filtro pasa bajos Chebyshev')
xlabel('Time (s)')
ylim(ys)


f1 = fft(y);
f2 = fft(outhi);
f3 = fft(dataOut);

P2 = abs(f1/L);
P1 = P2(1:L/2+1);
P1(2:end-1)=2*P1(2:end-1);
f = Fs*(0:(L/2))/L;
subplot(3,2,2)
plot(f,P1)
title('Espectro de Frecuencias de la Señal Original')


P2 = abs(f2/L);
P1 = P2(1:L/2+1);
P1(2:end-1)=2*P1(2:end-1);
f = Fs*(0:(L/2))/L;
subplot(3,2,4)
plot(f,P1)
title('Espectro de Frecuencias de la Señal Filtro Kaiser ')

P2 = abs(f3/L);
P1 = P2(1:L/2+1);
P1(2:end-1)=2*P1(2:end-1);
f = Fs*(0:(L/2))/L;
subplot(3,2,6)
plot(f,P1)
title('Espectro de Frecuencias de la Señal Filtro Chebyshev')


% %Audio original
% load handel.mat;
% playerObj = audioplayer(y,Fs);
% start = playerObj.SampleRate * 6;
% play(playerObj,start);

% %Audio filtro ventana kaiser
% playerObj1 = audioplayer(outhi,Fs);
% start1 = playerObj1.SampleRate * 4;
% play(playerObj1,start1);


% playerObj2 = audioplayer(outhi,Fs);
% start2 = playerObj2.SampleRate * 4;
% play(playerObj2,start2);


