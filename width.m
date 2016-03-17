function [ val ] = width(y, D)
%WIDTH caluclates witdth of the dam given y
p = 62.5;
val = p*(D-y).*(40-20*exp(-(0.01*y).^(2)));


end

