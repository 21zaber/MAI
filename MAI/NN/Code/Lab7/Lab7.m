clear;
clc;
%%
trange = 0 : 0.025 : 2 * pi;
x = ellipse(trange, 0.3, 0.7, 0, 0, pi / 4);
xseq = con2seq(x);

plot(x(1, :), x(2, :), '-r', 'LineWidth', 2);

net = feedforwardnet(1, 'trainlm');
net.layers{1}.transferFcn = 'purelin';

net = configure(net, x);
net = init(net);
view(net);
net.trainParam.epochs = 100;
net.trainParam.goal = 1.0e-5;
net = train(net, xseq, xseq);

yseq = sim(net, xseq);
y = cell2mat(yseq);

plot(x(1, :), x(2, :), '-r', y(1, :), y(2, :), '-b', 'LineWidth', 2);
%%

phi = 0.01 : 0.025 : 11 * pi / 6;
r = 1 ./ sqrt(phi);
x = [r .* cos(phi); r .* sin(phi)];
xseq = con2seq(x);

plot(x(1, :), x(2, :), '-r', 'LineWidth', 2);

net = feedforwardnet([10 1 10], 'trainlm');

net = configure(net, xseq, xseq);
net = init(net);
view(net);
net.trainParam.epochs = 2000;
net.trainParam.goal = 1.0e-5;
net = train(net, xseq, xseq);

yseq = sim(net, xseq);
y = cell2mat(yseq);

plot(x(1, :), x(2, :), '-r', y(1, :), y(2, :), '-b', 'LineWidth', 2);
%%
phi = 0.01 : 0.025 : 11 * pi / 6;
r = 1 ./ sqrt(phi);
x = [r .* cos(phi); r .* sin(phi); phi];
xseq = con2seq(x);

plot3(x(1, :), x(2, :), x(3, :), '-r', 'LineWidth', 2);

net = feedforwardnet([10 2 10], 'trainlm');

net = configure(net, xseq, xseq);
net = init(net);
view(net);
net.trainParam.epochs = 10000;
net.trainParam.goal = 1.0e-5;
net = train(net, xseq, xseq);

yseq = sim(net, xseq);
y = cell2mat(yseq);

plot3(x(1, :), x(2, :), x(3, :), '-r', y(1, :), y(2, :), y(3, :), '-b', 'LineWidth', 2);