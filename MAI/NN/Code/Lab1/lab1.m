clear;
clc;
%%
x = [26, -40, -15, 2, -33, 40;
     31, -33, -45, -17, -30, 17] ./ 10.0;
t = [0 1 1 0 1 0];

%%
x = [26, 30, -15, 2, -33, 40;
     31, 20, -45, -17, -30, 17] ./ 10.0;
t = [0 1 1 0 1 0];

%%
x = [-12, -25, 11, 32, 23, 8, 40, 31;
     8, -21, -24, 48, -16, -40, -37, -24] ./ 10.0;
t = [1 1 0 1 0 0 0 0;
     1 1 1 0 0 1 0 0];

%%
x = [randi(100,1,6);
    randi(100,1,6);] ./ 10.0;
t = randi(2,1,6) - 1;

%%
%==========================================================================
% построить сеть
net = perceptron('hardlim', 'learnp');

% отобразить структуру сети
display(net);
%view(net);
%mae = Mean absolute error performance function
%trainc = Cyclical order weight/bias training
net.inputs{1}
net.layers{1}
net.outputs{1}
net.inputWeights{1,1}
net.biases{1}
net.layerWeights
net.inputConnect
net.biasConnect
net.layerConnect
net = configure(net, x, t);
%view(net);
net.IW{1,1}
net.b{1}
net.LW

% инициализировать сеть случайными значениями
net.inputweights{1,1}.initFcn = 'rands';
net.biases{1}.initFcn = 'rands';
net = init(net);

net.IW{1,1} % веса
net.b{1} % смещение

% отобразить обучающую выборку и дискриминантную линию
y = net(x);
mae(t - y)
%[Y,~,~,E,perf] = sim(net, {x}, {}, {}, {t})
plotpv(x,t), grid
plotpc(net.IW{1,1},net.b{1});

%обучение сети
net.trainParam.epochs = 100;
[net,tr] = train(net, x, t);
y = net(x);
mae(t - y)
plotpv(x,t), grid
plotpc(net.IW{1,1},net.b{1});

%%
%генерация тестовой выборки
left = min(x, [], 2);
right = max(x, [], 2);
testpoints_num = 5;
testpoints = repmat(left, 1, testpoints_num) + repmat(right - left, 1, testpoints_num) .* rand(2, testpoints_num);
testclasses = net(testpoints);

%%
testpoints = [randi(100,1,5); randi(100,1,5)] ./ 10.0 - 5;
testclasses = [randi(2,1,5) - 1; randi(2,1,5) - 1]

%%
%запуск отображения тестовой выборки
plotpv(testpoints, testclasses);
point = findobj(gca,'type','line');
set(point,'Color','red');
hold on
plotpv(x, t)
plotpc(net.IW{1},net.b{1});
grid on
hold off

%%
net = init(net);
% алгоритм обучения по правилу Розенблатта
passes = 10;
samples = size(x, 2);
[~,samples] = size(x);
for i = 1 : passes
    for j = 1 : samples
        P = x(:, j);
        T = t(:, j);
        IW = net.IW{1,1};
        b = net.b{1};
        %Y = net(P);
        Y = hardlim(IW * P + b);
        E = T - Y;
    
        perf = mae(E);
        if (~perf)
            continue;
        end
    
        
        dW = E * P';
        db = E;
        net.IW{1,1} = IW + dW;
        net.b{1} = b + db;
    end

    % отобразить обучающую выборку и дискриминантную линию
    plotpv(x,t), grid
    plotpc(net.IW{1,1},net.b{1});
    if (~mae(t - net(x)))
        break;% perf=0 все сошлось
    end
end
%%
%Линейная неразделимость классов
net = init(net);
phi = [-pi : pi/8 : pi];
n = size(phi, 2);
x = [0.5 * sin(phi) 1.5 * sin(phi); 
     0.5 * cos(phi) 1.5 * cos(phi)];
t = [zeros(1, n) ones(1, n)];
plotpv(x, t), grid
plotpc(net.IW{1,1}, net.b{1});
[net,tr] = train(net, x, t);
y = net(x);
mae(t - y)
plotpv(x,t), grid
plotpc(net.IW{1,1},net.b{1});
