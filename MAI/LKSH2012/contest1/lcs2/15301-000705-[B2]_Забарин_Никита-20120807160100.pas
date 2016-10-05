program a03;

{$APPTYPE CONSOLE}

uses
  SysUtils, Math;

var
 s1, s2, ans : string;
 i, j, x, y : integer;
 d : array [0..2000, 0..2000] of integer;

begin
  reset(input, 'lcs2.in');
  rewrite(output, 'lcs2.out');
  readln(s1);
  readln(s2);
  fillchar(d, sizeof(d), 0);

  for i := 1 to length(s1) do
    for j := 1 to length(s2) do
      if s1[i] = s2[j] then
        d[i, j] := d[i - 1, j - 1] + 1
      else
        d[i, j] := max(d[i, j - 1], d[i - 1, j]);

  x := length(s1);
  y := length(s2);
  ans := '';
  while (x > 0) and (y > 0) do
    if s1[x] = s2[y] then begin
      ans := s1[x] + ans;
      dec(x);
      dec(y);
    end
    else
      if d[x - 1, y] > d[x, y - 1] then
        dec(x)
      else
        dec(y);

  writeln(ans);
end.
 