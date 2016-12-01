function y = lectFunc(a, b)

if (nargin ~= 2)
    error('FunctionCall:Arguments', 'Wrong number of arguments');
end
y = a + b;