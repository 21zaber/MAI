function [ o ] = parabola( t, p, x0, y0, alpha )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
r = p ./ (1 - cos(t));
x1 = r .* cos(t); 
y1 = r .* sin(t);
o = [x1 * cos(alpha) - y1 * sin(alpha) + x0;
     x1 * sin(alpha) + y1 * cos(alpha) + y0];
end

