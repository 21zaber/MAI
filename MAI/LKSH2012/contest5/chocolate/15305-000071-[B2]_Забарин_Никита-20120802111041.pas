program a02;

{$APPTYPE CONSOLE}

uses
  SysUtils, Math;

var
 w, h, k, i, x, y : integer;
 mas : array [0..1000, 0..1000] of integer;

begin
  reset(input, 'chocolate.in');
  rewrite(output, 'chocolate.out');
  fillchar(mas, sizeof(mas), 0);
  read(w, h, k);
  for i := 1 to k do begin
    read(x, y);
    mas[x, y] := 1;
  end;
  for x := 1 to w do
    for y := 1 to h do begin
      for i := 1 to x do
        mas[x, y] := max(mas[x, y], mas[x - i, y] +  mas[i, y]);
      for i := 1 to y do
        mas[x, y] := max(mas[x, y], mas[x, y - i] +  mas[x, i]);
    end;
  write(mas[w, h]);
end.
 