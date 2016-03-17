clear all
%Del 1
p = 62.5;
y = [0, 5, 10, 15, 20];
w = [20, 20.05, 20.25, 20.51, 21.18];

I = trapz(y,p*(20-y).*w);

disp(['Answer to part 1 is ', num2str(I)]);

%Del 2 and 3
D = 10:100;

F = zeros(size(D));
errorvals = zeros(size(D));
hvals = zeros(size(D));
nvals = zeros(size(D));

%error that we will have
tol = 1e-3;
h = D(1)/2;

for i=1:length(D) 
    h = D(i)/2;
    yh = linspace(0, D(i), D(i)./h+1);
    y2h = linspace(0, D(i), D(i)./(2*h)+1);
    

    inth = trapz(yh, width(yh, D(i)));
    int2h = trapz(y2h, width(y2h, D(i)));
    
    %calculate initial error
    error = abs(inth-int2h)/3;
    
    %if the error is two large, decrease h until its ok
    while error > tol
        
        %reduce step-size
        h = 0.5*h;
        
        %the old "h" is now "2h", so reassign
        int2h = inth;
        
        %form data points for new h
        yh = linspace(0, D(i), D(i)./h+1);
       
        %compute the integral
        inth = trapz(yh, width(yh, D(i)));
        
        %compute the error
        error = (inth-int2h)/3;
    end
    errorvals(i) = error;
    F(i) = inth;
    hvals(i) = h;
    nvals(i) = D(i)./h;
end

figure;
subplot(311)
plot(D, errorvals, '-o');
xlabel('D, fot')
ylabel('Error estimate')
subplot(312)
plot(D, hvals,'-o');
xlabel('D, fot')
ylabel('h, fot')
subplot(313)
plot(D, nvals, '-o');
xlabel('D, fot')
ylabel('n')
