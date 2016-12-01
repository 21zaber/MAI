%Matlab - ����� ���������� �������� ��� ������� ����� ����������� ����������
%� ���������� ���� ����������������, ������������ � ���� ������.
%���� MATLAB �������� ��������������� ���������������� ������ ����������������, 
%���������� ���������� �� �������� ��������� ������, ������� ������ �������, 
%��������������� ����� ����������, ��������-��������������� ����������� � 
%���������� � ����������, ���������� �� ������ ������ ����������������.
%��������� ������������.

%����� ��� ���� ��� �����������.

%{
����� ��� ����
��� �������������
�����������.
%}

a = 42.0;
%���������� ���������� � "������� ������������" (workspace)
%��� �������� ������� ���� ����� ������� ������������
%������� ����� ������� � �������� ���������, � ����� ����������� ������� ������������
%��� �������, ��� � ������� �� ������������� � �������� ��� � ����������� � ���� ��������� ������ 
whos;%������ ���������� � ������� ������������, � ��������� ������� � ����

doc whos;%������������

clc;%�������� ���� ������

clear a;%������� ���������� �� �������� ������������, ���������� ������

a = 42.0;
b = 42.0e-5;
save test.mat;%��������� ���������� �� �������� ������������
clear;
load test.mat;%��������� ���������� � ������� ������������

s = 'String.';
disp(s);
fprintf('a = %f, b = %f, s = %s\n', a, b, s);

%�������� ���������
if a < 10
    disp('a is small');
elseif a <= 30
    disp('a is not so small');
else
    disp('a is large');
end

switch s
    case 'foo' 
        warning('s is foo');
    case {'bar','String.'}
        disp('s is fine.');
    otherwise
        error('s is unexpected');
end

%�����
while a > 10
    a = a - 5;
    if strcmp(s, 'String.')
        break;
    end
end

for i = 1 : 5
    fprintf('i = %d\n', i);
end

%�������
arr = [-31 4 0 14 5];
for i = 1 : length(arr)
    disp(arr(i));
end

%�������
mat = [1 2 3;
       4 5 6;
       7 8 9];
[m, n] = size(mat);
[~, n] = size(mat);

mat = zeros(m, n);
mat = ones(m, n);
mat = eye(m, n);

mat1 = diag(-5:5);
mat2 = diag(-5:5,-1);
mat3 = diag(-5:5, 1);
%%
n  = 2
m = 5
mat4 = rand(m, n);
mat5 = rand(m, n);
mat = blkdiag(mat4, mat5);
%%
mat = mat1 + mat2 + mat3;
mat = mat4 * 5 - mat5' * mat5;
mat1 = rand(3, 2);
%mat = mat1 * mat1; error
mat = mat1 .* mat1;
mat = mat1 .^ 3;
%%
mat1 = rand(3, 3);
mat2 = rand(3, 3);
mat = [mat1 mat2];
%%
mat = [mat1; mat2];

matsmall = [1 2;
            3 4];
mat = repmat(matsmall, 2, 3);

mat1 = rand(5, 5);
part = mat1(1 : 3, :);
part = mat1(1 : 2 : 5, 3 : end);

arr = rand(1, 5);
arr = sort(arr);
mat = rand(4, 4);
mat1 = sort(mat, 1);
mat2 = sort(mat, 2);
mat3 = reshape(mat, 2, 8);
%%
%�������� : � �������������� ��������� �������
a = 1 : 5;
b = 2 : 0.1 : 3;
%%
a = rand(10, 1);
w = (a > 0.5);
w1 = a(w);
a(w) = 0.5;

a = rand(10, 1);
a(a > 0.5) = 0.5;

a = [0 2 0;
     1 3 0];
[i, j] = find(a);
w = (a == 1);
[i, j] = find(a == 1);

%���������
student.name = 'Vasya Pupkin';
student.age = 21;
student.marks = rand(20);

%������� �����
seq = cell(2, 3);
for i = 1 : 2
    for j = 1 : 3
        seq{i, j} = rand(i, j);
    end
end
seq{1, 3} = student;
seq{2, 2} = 'Student';

seq2 = {'abc', 2; student, seq };

arr = 1 : 10;
seq = con2seq(arr);
arr = cell2mat(seq);

%�������
time = 0 : 0.1 : 2 * pi;
val = sin(time);
plot(time, val);

figure;
hold on;
plot(time, sin(time), '-b');
plot(time, cos(time), '.r');
xlabel('time');
ylabel('value');
axis([0 2 * pi -1 1]);
%axis tight;
legend('sin', 'cos');

plot3(sin(time), cos(time), time);
grid on;

[X,Y] = meshgrid(-2:0.2:2, -2:0.2:2);
Z = X .* exp(-X.^2 - Y.^2);
surf(X,Y,Z);

%�������
y = lectFunc(2,3);
y = feval('lectFunc', 3, 3);%���������� ������� �� ��������� �����
y = feval('lectFunc2', 3, 3);
sqr = @(x) x.^2;%���������� �������
x = 1:0.2:10;
y = sqr(x);

%����������
try
    y = lectFunc(1);
catch err
    if (strcmp(err.identifier,'FunctionCall:Arguments'))
         disp('i caught my exception');
     else
         rethrow(err);
    end
end