program b01;

{$APPTYPE CONSOLE}

uses
  SysUtils, Math;

const
 powers : array [1..18] of integer = (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072);

type
  TTable = array [1..18, 1..100000] of integer;

var
  n, m, u, v, i, ans : integer;
  table : TTable;
  mas : array [1..100000] of integer;



function mlog (a : integer): integer;
var
  i : integer;
begin
  i := 1;
  while a >= powers[i] do inc(i);
  if i = 1 then inc(i);
  result := i - 1;
end;

procedure Build();
var
  len, l, i : integer;
begin
  len := 1;
  for l:= 1 to mlog(n) do begin
    for i:= 1 to n - len + 1 do
      if l = 1 then
        table[l, i] := mas[i]
      else
        table[l, i] := min(table[l - 1, i], table[l - 1, i + len div 2]);
    len := len shl 1;
  end;
end;

function MyMin (l, r : integer): integer;
var
  t : integer;
begin
  if r < l then begin
    t := r;
    r := l;
    l := t;
  end;
  t := mlog(r - l);
  result := min(table[t, l], table[t, r - (1 shl (t - 1)) + 1]);
end;

begin
  reset(input, 'sparse.in');
  rewrite(output, 'sparse.out');
  readln(n, m, mas[1]);
  readln(u, v);
  for i := 2 to n do
    mas[i] := (23 * mas[i - 1] + 21563) mod 16714589;
  ans := 0;
  Build;
  for i := 1 to m do begin
    ans := MyMin(u, v);
    if i <> m then begin
      u := ((17 * u + 751 + ans + 2 * i) mod n) + 1;
      v := ((13 * v + 593 + ans + 5 * i) mod n) + 1;
    end;
  end;
  write(u, ' ', v, ' ', ans);
end.
 