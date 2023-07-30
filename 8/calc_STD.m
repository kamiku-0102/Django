close all; clear all;

%MATファイルの読み込み
load("calc_matlix.mat");

%要素数:N
N = size(Phi,1);

%偏差:deviation,分散:variance
variance = 0;
deviation = 0;

for i = 1:N
    deviation = a * Phi(i,2) + b - t(i);
    variance = variance +  deviation^2;
end

variance = variance / 5;

%標準偏差:STD(standard deviation)
STD = sqrt(variance);


save("calc_matlix.mat");
