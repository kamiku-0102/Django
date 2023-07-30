close all; clear all;

%行列の定義(計画行列Phi, 測定データt)
Phi = [1 1; 1 2; 1 3; 1 4; 1 5];
t = [9; 10; 14; 15; 16];

%%行列計算%%
%Phiの転置行列
Phi_T = Phi.';

%Phiの転置行列とPhiの積
Phi_T_Phi = Phi_T * Phi;


%ムーア-アーペンローズの擬似逆行列
Phi_dagger = Phi_T_Phi \ Phi_T;

%%行列計算%%


%MATファイルへワークスペース変数を保存
save("calc_matlix.mat");