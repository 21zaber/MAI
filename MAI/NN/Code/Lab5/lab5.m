clear;
clc;
%%
%figure;
%hold on;
%plot(cell2mat(p2), '-b');
%%
%g(k) = cos(?3k2 + 5k + 10), k ? [0.24, 2.7] [2, 4, 4]
k1 = 0 : 0.025 : 1;
p1 = sin(4 * pi * k1);
t1 = -ones(size(p1));
k2 = 0.24 : 0.025 : 2.7;
g = @(k)cos(-3 * k.^2 + 5 * k + 10);
p2 = g(k2);
t2 = ones(size(p2));

%%

R = {2; 2; 4};
P = [repmat(p1, 1, R{1}), p2, repmat(p1, 1, R{2}), p2, repmat(p1, 1, R{3}), p2];
T = [repmat(t1, 1, R{1}), t2, repmat(t1, 1, R{2}), t2, repmat(t1, 1, R{3}), t2];

Pseq = con2seq(P);
Tseq = con2seq(T);

net = layrecnet(1 : 2, 8, 'trainoss');
net.layers{1}.transferFcn = 'tansig';
net.layers{2}.transferFcn = 'tansig';
net = configure(net, Pseq, Tseq);
view(net);

[p, Pi, Ai, t] = preparets(net, Pseq, Tseq);
net.trainParam.epochs = 100;
net.trainParam.goal = 1.0e-5;
net = train(net, p, t, Pi, Ai);
Y = sim(net, p, Pi, Ai);

figure;
hold on;
plot(cell2mat(t), '-b');
plot(cell2mat(Y), '-r');
plot(cell2mat(p1), '-g');
legend('эталонные', 'предсказанные');

Yc = zeros(1, numel(Y));
for i = 1 : numel(Y)
    if Y{i} >= 0
        Yc(i) = 1;
    else
        Yc(i) = -1;
    end
end
display(nnz(Yc == T(3 : end)))
%%
target0 = [-1 -1 -1 -1 -1 -1 -1 -1 -1 -1;
           -1 -1 -1 +1 +1 +1 +1 -1 -1 -1;
           -1 -1 +1 +1 +1 +1 +1 +1 -1 -1;
           -1 +1 +1 +1 -1 -1 +1 +1 +1 -1;
           -1 +1 +1 +1 -1 -1 +1 +1 +1 -1;
           -1 +1 +1 +1 -1 -1 +1 +1 +1 -1;
           -1 +1 +1 +1 -1 -1 +1 +1 +1 -1;
           -1 +1 +1 +1 -1 -1 +1 +1 +1 -1;
           -1 +1 +1 +1 -1 -1 +1 +1 +1 -1;
           -1 -1 +1 +1 +1 +1 +1 +1 -1 -1;
           -1 -1 -1 +1 +1 +1 +1 -1 -1 -1;
           -1 -1 -1 -1 -1 -1 -1 -1 -1 -1];
target1 = [-1 -1 -1 +1 +1 +1 +1 -1 -1 -1;
           -1 -1 -1 +1 +1 +1 +1 -1 -1 -1;
           -1 -1 -1 +1 +1 +1 +1 -1 -1 -1;
           -1 -1 -1 +1 +1 +1 +1 -1 -1 -1;
           -1 -1 -1 +1 +1 +1 +1 -1 -1 -1;
           -1 -1 -1 +1 +1 +1 +1 -1 -1 -1;
           -1 -1 -1 +1 +1 +1 +1 -1 -1 -1;
           -1 -1 -1 +1 +1 +1 +1 -1 -1 -1;
           -1 -1 -1 +1 +1 +1 +1 -1 -1 -1;
           -1 -1 -1 +1 +1 +1 +1 -1 -1 -1;
           -1 -1 -1 +1 +1 +1 +1 -1 -1 -1;
           -1 -1 -1 +1 +1 +1 +1 -1 -1 -1];
target2 = [+1 +1 +1 +1 +1 +1 +1 +1 -1 -1;
           +1 +1 +1 +1 +1 +1 +1 +1 -1 -1;
           -1 -1 -1 -1 -1 -1 +1 +1 -1 -1;
           -1 -1 -1 -1 -1 -1 +1 +1 -1 -1;
           -1 -1 -1 -1 -1 -1 +1 +1 -1 -1;
           +1 +1 +1 +1 +1 +1 +1 +1 -1 -1;
           +1 +1 +1 +1 +1 +1 +1 +1 -1 -1;
           +1 +1 -1 -1 -1 -1 -1 -1 -1 -1;
           +1 +1 -1 -1 -1 -1 -1 -1 -1 -1;
           +1 +1 -1 -1 -1 -1 -1 -1 -1 -1;
           +1 +1 +1 +1 +1 +1 +1 +1 -1 -1;
           +1 +1 +1 +1 +1 +1 +1 +1 -1 -1;];
target3 = [-1 -1 +1 +1 +1 +1 +1 +1 -1 -1;
           -1 -1 +1 +1 +1 +1 +1 +1 +1 -1;
           -1 -1 -1 -1 -1 -1 -1 +1 +1 -1;
           -1 -1 -1 -1 -1 -1 -1 +1 +1 -1;
           -1 -1 -1 -1 -1 -1 -1 +1 +1 -1;
           -1 -1 -1 -1 +1 +1 +1 +1 -1 -1;
           -1 -1 -1 -1 +1 +1 +1 +1 -1 -1;
           -1 -1 -1 -1 -1 -1 -1 +1 +1 -1;
           -1 -1 -1 -1 -1 -1 -1 +1 +1 -1;
           -1 -1 -1 -1 -1 -1 -1 +1 +1 -1;
           -1 -1 +1 +1 +1 +1 +1 +1 +1 -1;
           -1 -1 +1 +1 +1 +1 +1 +1 -1 -1];
target4 = [-1 +1 +1 -1 -1 -1 -1 +1 +1 -1;
           -1 +1 +1 -1 -1 -1 -1 +1 +1 -1;
           -1 +1 +1 -1 -1 -1 -1 +1 +1 -1;
           -1 +1 +1 -1 -1 -1 -1 +1 +1 -1;
           -1 +1 +1 -1 -1 -1 -1 +1 +1 -1;
           -1 +1 +1 +1 +1 +1 +1 +1 +1 -1;
           -1 +1 +1 +1 +1 +1 +1 +1 +1 -1;
           -1 -1 -1 -1 -1 -1 -1 +1 +1 -1;
           -1 -1 -1 -1 -1 -1 -1 +1 +1 -1;
           -1 -1 -1 -1 -1 -1 -1 +1 +1 -1;
           -1 -1 -1 -1 -1 -1 -1 +1 +1 -1;
           -1 -1 -1 -1 -1 -1 -1 +1 +1 -1];
target6 = [+1 +1 +1 +1 +1 +1 -1 -1 -1 -1;
           +1 +1 +1 +1 +1 +1 -1 -1 -1 -1;
           +1 +1 -1 -1 -1 -1 -1 -1 -1 -1;
           +1 +1 -1 -1 -1 -1 -1 -1 -1 -1;
           +1 +1 +1 +1 +1 +1 -1 -1 -1 -1;
           +1 +1 +1 +1 +1 +1 -1 -1 -1 -1;
           +1 +1 -1 -1 +1 +1 -1 -1 -1 -1;
           +1 +1 -1 -1 +1 +1 -1 -1 -1 -1;
           +1 +1 -1 -1 +1 +1 -1 -1 -1 -1;
           +1 +1 -1 -1 +1 +1 -1 -1 -1 -1;
           +1 +1 +1 +1 +1 +1 -1 -1 -1 -1;
           +1 +1 +1 +1 +1 +1 -1 -1 -1 -1];
target9 = [-1 -1 -1 -1 +1 +1 +1 +1 +1 +1;
           -1 -1 -1 -1 +1 +1 +1 +1 +1 +1;
           -1 -1 -1 -1 +1 +1 -1 -1 +1 +1;
           -1 -1 -1 -1 +1 +1 -1 -1 +1 +1;
           -1 -1 -1 -1 +1 +1 -1 -1 +1 +1;
           -1 -1 -1 -1 +1 +1 -1 -1 +1 +1;
           -1 -1 -1 -1 +1 +1 +1 +1 +1 +1;
           -1 -1 -1 -1 +1 +1 +1 +1 +1 +1;
           -1 -1 -1 -1 -1 -1 -1 -1 +1 +1;
           -1 -1 -1 -1 -1 -1 -1 -1 +1 +1;
           -1 -1 -1 -1 +1 +1 +1 +1 +1 +1;
           -1 -1 -1 -1 +1 +1 +1 +1 +1 +1];
%%           
net = newhop([target9(:), target1(:), target3(:)]);
view(net);

iterations = 600;
res = sim(net, {1 iterations}, {}, target1(:));
res = reshape(res{iterations}, 12, 10);
res(res >=0 ) = 2;
res(res < 0 ) = 1;
map = [1, 1, 1; 0, 0, 0];
image(res);
colormap(map)
axis off
axis image

%%
rando = rand([12, 10]);
noise_degree = 0.2;
input = target3;
for i = 1:12
    for j = 1:10
        if rando(i, j) < noise_degree
            input(i, j) = -input(i, j);
        end
    end
end

res = reshape(input, 12, 10);
res(res >=0 ) = 2;
res(res < 0 ) = 1;
map = [1, 1, 1; 0, 0, 0];
figure('Name', 'Noised');
image(res);
colormap(map)
axis off
axis image

iterations = 100;
res = sim(net, {1 iterations}, {}, input(:));
res = reshape(res{iterations}, 12, 10);
res(res >=0 ) = 2;
res(res < 0 ) = 1;
map = [1, 1, 1; 0, 0, 0];
figure('Name', 'Recognised');
image(res);
colormap(map)
axis off
axis image
%%
rando = rand([12, 10]);
noise_degree = 0.3;
input = target9;
for i = 1:12
    for j = 1:10
        if rando(i, j) < noise_degree
            input(i, j) = -input(i, j);
        end
    end
end

res = reshape(input, 12, 10);
res(res >=0 ) = 2;
res(res < 0 ) = 1;
map = [1, 1, 1; 0, 0, 0];
figure('Name', 'Noised');
image(res);
colormap(map)
axis off
axis image

iterations = 100;
res = sim(net, {1 iterations}, {}, input(:));
res = reshape(res{iterations}, 12, 10);
res(res >=0 ) = 2;
res(res < 0 ) = 1;
map = [1, 1, 1; 0, 0, 0];
figure('Name', 'Recognised');
image(res);
colormap(map)
axis off
axis image

%%
p = [target0(:), target1(:), target2(:), target3(:), target4(:), target6(:), target9(:)];
Q = 7;
R = 120;
IW = [target0(:)';
      target1(:)';
      target2(:)';
      target3(:)';
      target4(:)';
      target6(:)';
      target9(:)'];
b = ones(Q, 1) * R;

a = zeros(Q, Q);
for i = 1 : Q
    a(:, i) = IW * p(:, i) + b;
end

net = newhop(a);
net.biasConnect(1) = 0;
net.layers{1}.transferFcn = 'poslin';

eps = 1 / (Q - 1);
net.LW{1, 1} = eye(Q, Q) * (1 + eps) - ones(Q, Q) * eps;
view(net);
%%
iterations = 600;
input = target1(:);
a1 = IW * input + b;
res = sim(net, {1 iterations}, {}, a1);
a2 = res{iterations};
ind = find(a2 == max(a2));
answer = IW(ind, :)';

res = reshape(answer, 12, 10);
res(res >=0 ) = 2;
res(res < 0 ) = 1;
map = [1, 1, 1; 0, 0, 0];
image(res);
colormap(map)
axis off
axis image

%%
iterations = 600;
rando = rand([12, 10]);
noise_degree = 0.3;
input = target9;
for i = 1:12
    for j = 1:10
        if rando(i, j) < noise_degree
            input(i, j) = -input(i, j);
        end
    end
end
res = reshape(input, 12, 10);
res(res >=0 ) = 2;
res(res < 0 ) = 1;
map = [1, 1, 1; 0, 0, 0];
figure('Name', 'Noised');
image(res);
colormap(map)
axis off
axis image
input = input(:)
a1 = IW * input + b;
res = sim(net, {1 iterations}, {}, a1);
a2 = res{iterations};
ind = find(a2 == max(a2));
answer = IW(ind, :)';

res = reshape(answer, 12, 10);
res(res >=0 ) = 2;
res(res < 0 ) = 1;
map = [1, 1, 1; 0, 0, 0];
figure('Name', 'Recognised');
image(res);
colormap(map)
axis off
axis image
