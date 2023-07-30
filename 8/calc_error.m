close all; clear all;

%MATファイルの読み込み
load("calc_matlix.mat");

%要素数:N
N = size(Phi,1);


%a,bの標準偏差
sigma_a = 0;
sigma_b = 0;

%ルートの中身の計算
for j= 1:N
  sigma_a = sigma_a + Phi_dagger(2,j)^2;
  sigma_b = sigma_b + Phi_dagger(1,j)^2;
end

%標準偏差の計算
sigma_a = STD * sqrt(sigma_a);
sigma_b = STD * sqrt(sigma_b);

save("calc_matlix.mat");
