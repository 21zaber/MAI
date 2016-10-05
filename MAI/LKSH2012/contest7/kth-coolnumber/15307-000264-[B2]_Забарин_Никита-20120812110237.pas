program c01;

{$APPTYPE CONSOLE}

uses
  SysUtils;

var
 d : array [0..20, 0..2000, 0..3] of int64;
 l, r, ll, w : int64;
 k : integer;



function msum (const n : string; const flag : boolean): int64;
var
  i, l, r : integer;
begin
  fillchar(d, sizeof(d), 0);
  for i := 0 to strtoint(n[1]) - 1 do
    inc(d[1, i mod k, 1]);
  inc(d[1, strtoint(n[1]) mod k, 0]);

  for l := 0 to length(n) - 1 do begin
    for r := 0 to k - 1 do begin

      for i := 0 to 9 do
        inc(d[l + 1, (i + r) mod k, 1], d[l, r mod k, 1]);

      for i := 0 to strtoint(n[l + 1]) - 1 do
        inc(d[l + 1, (i + r) mod k, 1], d[l, r mod k, 0]);

      inc(d[l + 1, (strtoint(n[l + 1]) + r) mod k, 0], d[l, r mod k, 0]);
    end;
  end;
  {for l := 0 to length(n) do begin
    for i := 0 to k - 1 do
      write('[', d[l, i, 0], ',', d[l, i, 1], ']');
    writeln;
  end;
  writeln(n);}
  result := d[length(n), 0, 1];
  if flag then
    inc(result, d[length(n), 0, 0]);
 // writeln(n, ' ', result);
end;

function bin(l, r : int64): int64;
var
  m : int64;
begin
  result := l;
  if r = l then exit;
  m := (l + r) div 2;
  if msum(inttostr(m), true) - ll >= w then
    result := bin(l, m)
  else
    result := bin(m + 1, r);
end;

begin
  reset(input, 'kth-coolnumber.in');
  rewrite(output, 'kth-coolnumber.out');
  readln(l, r, k, w);
  ll := msum(inttostr(l), False);
  if msum(inttostr(r), True) - msum(inttostr(l), False) < w then
    write('-1')
  else
    write(bin(l, r));
end.
 