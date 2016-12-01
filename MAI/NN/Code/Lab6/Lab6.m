clear;
clc;
%% p.1
X = [0 1.5;
     0 1.5];
clusters = 8;
points = 10;
deviation = 0.1;
P = nngenc(X, clusters, points, deviation);

figure;
hold on;
grid on;
scatter(P(1, :), P(2, :), 15, [0 1 0], 'filled');

net = competlayer(8);
net = configure(net, P);
view(net);
net.divideFcn = '';
net.trainParam.epochs = 50;
net = train(net, P);

R = zeros(2, 5) + 1.5 * rand(2, 5);
res = vec2ind(sim(net, R));

figure;
hold on;
grid on;
scatter(P(1, :), P(2, :), 15, [0 1 0], 'filled');
scatter(R(1, :), R(2, :), 15, [1 0 0], 'filled');
%% p.2
X = [0 1.5;
     0 1.5];
clusters = 8;
points = 10;
deviation = 0.1;
P = nngenc(X, clusters, points, deviation);

net = newsom(X, [2, 4]);
net.trainParam.epochs = 150;
net = train(net, P);

R = zeros(2, 5) + 1.5 * rand(2, 5);
res = vec2ind(sim(net, R));

figure;
hold on;
grid on;
plotsom(net.IW{1, 1}, net.layers{1}.distances)
scatter(P(1, :), P(2, :), 15, [0 1 0], 'filled');
scatter(R(1, :), R(2, :), 15, [1 0 1], 'filled');

%%
%net = configure(net, X);
plotsomtop(net)
figure;
plotsomnc(net)
figure;
plotsomplanes(net)
figure;
plotsomnd(net)
figure;
plotsomhits(net,P)
figure;
plotsompos(net,P)

%%
%gridtop, hextop, tritop or randtop
% dist, boxdist, linkdist, and mandist
%net = selforgmap([8 5],'topologyFcn','gridtop','distanceFcn','dist');
net = selforgmap([4 2],'topologyFcn','hextop','distanceFcn','linkdist');
%net = selforgmap([8 5],'topologyFcn','tritop','distanceFcn','boxdist');
%net = selforgmap([8 5],'topologyFcn','randtop','distanceFcn','mandist');  
%net = selforgmap([8],'topologyFcn','hextop','distanceFcn','linkdist');
%%
net = configure(net, X);

plotsomtop(net)

plotsomnc(net)

%Each ith subplot shows the weights from the ith input to the layer's 
%neurons, with the most negative connections shown as blue, zero 
%connections as black, and the strongest positive connections as red.
plotsomplanes(net)

%plotsomnd(net) plots a SOM layer showing neurons as gray-blue patches and
%their direct neighbor relations with red lines. The neighbor patches are 
%colored from black to yellow to show how close each neuron's weight vector
%is to its neighbors.
plotsomnd(net)

%plots a SOM layer, with each neuron showing the number of input vectors
%that it classifies. The relative number of vectors for each neuron is
%shown via the size of a colored patch.
plotsomhits(net,P)
figure;
plotsompos(net,P)
%%
net = selforgmap([2 4], 'topologyFcn','hextop','distanceFcn','linkdist');
net = configure(net, X);
view(net);
net.divideFcn = '';

%1)Ordering Phase
%This phase lasts for the given number of steps. The neighborhood distance
%starts at a given initial distance, and decreases to the tuning 
%neighborhood distance (1.0). As the neighborhood distance decreases over
%this phase, the neurons of the network typically order themselves in the
%input space with the same topology in which they are ordered physically. 
net.inputWeights{1,1}.learnParam.init_neighborhood = 3;
net.inputWeights{1,1}.learnParam.steps = 100;
%2)Tuning Phase
%This phase lasts for the rest of training or adaption. The neighborhood
%size has decreased below 1 so only the winning neuron learns for each sample. 
net.trainParam.epochs = 150;
net = train(net, P);

R = zeros(2, 5) + 1.5 * rand(2, 5);
res = vec2ind(sim(net, R));

figure;
hold on;
grid on;
scatter(P(1, :), P(2, :), 5, [0 1 0], 'filled');
scatter(net.IW{1}(:, 1), net.IW{1}(:, 2), 5, [0 0 1], 'filled');
scatter(R(1, :), R(2, :), 5, [1 0 0], 'filled');
plotsom(net.IW{1, 1}, net.layers{1}.distances);
%%
N = 20;
T = -1.5 * ones(2, N) + 3 * rand(2, N);

figure;
hold on;
grid on;
plot(T(1,:), T(2,:), '-V', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'g', 'MarkerSize', 7);

%net = newsom(T, N);
net = selforgmap(N);
net = configure(net, T);
view(net);
net.divideFcn = '';
net.trainParam.epochs = 600;
net = train(net, T);

figure;
hold on;
grid on;
plotsom(net.IW{1,1}, net.layers{1}.distances);
plot(T(1,:), T(2,:), 'V', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'g', 'MarkerSize', 7);
%%
%[-1.2 0.5 1.4  0.7 -0.3 -0.1 0.7  -1.3 -0.4 -1   1.2 1.4;
%-0.8 1   -0.9 0.2 0    0.4  -0.6 0.9  0.8  -1.2 1.1 1 ]

%[-1 1 -1 -1 1 1 -1 -1 1 -1 -1 -1];


P = [-1.2 0.5 1.4  0.7 -0.3 -0.1 0.7  -1.3 -0.4 -1   1.2 1.4;
     -0.8 1   -0.9 0.2 0    0.4  -0.6 0.9  0.8  -1.2 1.1 1 ];
T = [-1 1 -1 -1 1 1 -1 -1 1 -1 -1 -1];

plotpv(P, max(0, T));
%%
Ti = T;
Ti(Ti == 1) = 2;
Ti(Ti == -1) = 1;
Ti = ind2vec(Ti);

%percentage = [nnz(T(T == -1)) nnz(T(T == 1))] / numel(T);
%net = newlvq(12, percentage, 0.1);
net = lvqnet(12, 0.1);
net = configure(net, P, Ti);
view(net)
%initfcn = midpoint
net.IW{1,1}
%train ratio, unions of subclasses
net.LW{2,1}

net.trainParam.epochs = 300;
net = train(net, P, Ti);

[X,Y] = meshgrid([-1.5 : 0.1 : 1.5], [-1.5 : 0.1 : 1.5]);
res = sim(net, [X(:)'; Y(:)']);
res = vec2ind(res) - 1;
figure;
plotpv([X(:)'; Y(:)'], res);
%%
point = findobj(gca,'type','line');
set(point,'Color','g');
%%
hold on;
plotpv(P, max(0, T));