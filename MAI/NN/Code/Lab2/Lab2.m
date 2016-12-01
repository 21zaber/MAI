clear;
clc;
%% my var 21
t0 = 0.5;
tn = 4;
dt = 0.01;
func = @(t)cos(-3 * t.^2 + 10 * t - 5) - cos(t);

%% my var 21
t0 = 0;
tn = 2.5;
dt = 0.01;
func = @(t)cos(-3 * t.^2 + 10 * t + 10);

%%
t0 = 0.5;
tn = 3;
dt = 0.01;
func = @(t)cos(t.^2 - 15 * t + 3) - cos(t);

%%
z=func(0.5);
x = func(t0 : dt : tn);
y = func(t0 + dt : dt : tn + dt);
%%
xseq = con2seq(x);
yseq = con2seq(y);
%%
delays = 1 : 5;
lr = 0.01;
net = newlin(xseq, yseq, delays, lr);

view(net);
%%
net.inputWeights{1,1}.learnFcn
net.performFcn

net.inputWeights{1,1}.initFcn = 'rands';
net.biases{1}.initFcn = 'rands';
net = init(net);
%%
[Xs,Xi,~,Ts] = preparets(net, xseq, yseq);
for i = 1 : 50
    [net,Y,E] = adapt(net, Xs, Ts, Xi);
    Y = net(Xs, Xi);
    perf = perform(net, Ts, Y);
    display(sqrt(perf));
end
%%
figure;
hold on;
grid on;
plot(t0 + 5 * dt : dt : tn, cell2mat(Ts), '-b');
plot(t0 + 5 * dt : dt : tn, cell2mat(Y), '-r');
xlabel('t');
ylabel('y');
%%
figure;
hold on;
grid on;
plot(t0 + 5 * dt : dt : tn, cell2mat(E));
xlabel('t');
ylabel('error');
%%
delays = 1 : 3;
lr = maxlinlr(x, 'bias');
net = newlin(xseq, yseq, delays, lr);
net = configure(net, xseq, yseq);

view(net);
%%
net.inputWeights{1,1}.initFcn = 'rands';
net.biases{1}.initFcn = 'rands';
net = init(net);
%%
net.trainParam.epochs = 100;
net.trainParam.goal = 1.0e-6;
[Xs,Xi,Ai,Ts,Ews] = preparets(net, xseq, yseq);
net.trainFcn = 'trains';
%%

%%[net,tr] = train(net, Xs, Ts, Xi, Ai);
%net=train(net,Xs,Ts,Xi);
for i = 1 : net.trainParam.epochs
    [net,Y,E] = adapt(net, Xs, Ts, Xi);
    Y = net(Xs, Xi);
    perf = perform(net, Ts, Y);
    display(sqrt(perf));
    display(i);
end

[Y,Pf,Af,E,perf] = sim(net, Xs, Xi, Ai, Ts);
display(sqrt(perf));
%%
figure;
hold on;
grid on;
plot(t0 + 3 * dt : dt : tn, cell2mat(Ts), '-b');
plot(t0 + 3 * dt : dt : tn, cell2mat(Y), '-r');
xlabel('t');
ylabel('y');

figure;
hold on;
grid on;
plot(t0 + 3 * dt : dt : tn, cell2mat(E));
xlabel('t');
ylabel('error');
%%
steps = 100;

xt = func(tn - 3 * dt : dt : tn + (steps - 1) * dt);
yt = func(tn - 2 * dt : dt : tn + steps * dt);
xtseq = con2seq(xt);
ytseq = con2seq(yt);
[Xst,Xit,Ait,Tst] = preparets(net, xtseq, ytseq);
[Yt,Pft,Aft,Et,perft] = sim(net, Xst, Xit, Ait, Tst);
display(sqrt(perft))

figure;
hold on;
grid on;
plot(t0 + 3 * dt : dt : tn, cell2mat(Ts), '-b');
plot(t0 + 3 * dt : dt : tn, cell2mat(Y), '-r');

plot(tn + dt : dt : tn + steps * dt, cell2mat(Tst), '-.b');
plot(tn + dt : dt : tn + steps * dt, cell2mat(Yt), '-.r');
xlabel('t');
ylabel('y');
%%
t0 = 0;
tn = 2.5;
dt = 0.01;
func1 = @(t)cos(-3 * t.^2 + 5 * t + 10);
func2 = @(t)cos(-3 * t.^2 + 5 * t + 3*pi/2) / 6;
x = func1(t0 : dt : tn);
y = func2(t0 : dt : tn);
%%
D = 4;
Q = numel(t0 : dt : tn);
p = zeros(D, Q);
for i = 1 : D
    p(i, i : Q) = x(1 : Q - i + 1);
end
%%
net = newlind(p, y);
Y = net(p);
display(sqrt(mse(Y - y)));

figure;
hold on;
grid on;
plot(t0:dt:tn, y, '-b');
plot(t0:dt:tn, Y, '-r');

figure;
hold on;
grid on;
plot(t0:dt:tn, Y - y);
