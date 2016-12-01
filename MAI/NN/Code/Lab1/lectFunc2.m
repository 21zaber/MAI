function y = lectFunc2(varargin)

if(nargin ~= 2)
    error('FunctionCall:Arguments', 'Wrong number of arguments');
end
a = varargin{1};
b = varargin{2};
y = a + b;