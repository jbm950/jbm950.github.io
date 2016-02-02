fprintf('\nPart a\n')
Num = [1 1 5 -50];
Denom = [1 26 614 4369 39380 356000];
H = tf(Num, Denom)

fprintf('Part b\n\n')
[Z, P, K] = zpkdata(H, 'v');
fprintf('Zeros:\n\t%s\n\t%s\n\t%s\n\n', num2str(Z(1)), num2str(Z(2)), num2str(Z(3)))
fprintf('Poles:\n\t%s\n\t%s\n\t%s\n\n', num2str(P(1)), num2str(P(2)), num2str(P(3)))
fprintf('Gain: %d\n\n', K)

fprintf('Part c\n\nGraph attached\n\n')
step(5*H)

fprintf('Part d\n\n')
A = [1 2 5 90];
B = [1 56 -67];
C = conv(A, B);
fprintf('%ds^5%+ds^4%+ds^3%+ds^2%+ds%+d\n\n', C)

fprintf('Part e\n')
z = [1, -56];
p = [-1, -1+2j, -1-2j];
k = 5;
h = zpk(z, p, k)
