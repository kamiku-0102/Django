close all; clear all;

%MATファイルの読み込み
load("calc_matlix.mat");

%パラメータ
w = Phi_dagger * t;
disp(w);

b = w(1);
a = w(2);
x = 0:0.1:6;
y = a * x + b;


%グラフの作成
plot(x, y, 'LineWidth',2);

%範囲の指定
xlim([0 6]);
ylim([0 18]);

%データのプロット
hold on;
plot(Phi(:,2), t, '.', 'MarkerSize',15);
hold off;