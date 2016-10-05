program d02;

{$APPTYPE CONSOLE}

uses
  SysUtils,
  Math;

var
  mas, d, used : array [0..1000001] of integer;
  n, i : integer;

procedure up (var x : integer);
begin
  x := x or (x + 1);
end;

procedure down (var x : integer);
begin
  x := (x and (x + 1)) - 1;
end;

procedure UpDate(i, x : integer);
begin
  while i < 1000000 do begin
    inc(used[i], x);
    up(i);
  end;
end;

function Sum (r : integer) : int64;
begin
  result := 0;
  while r >= 0 do begin
    inc(result, used[r]);
    down(r);
  end;
end;

begin
  reset(input, 'inverse.in');
  rewrite(output, 'inverse.out');

  fillchar(used, sizeof(used), 0);
  fillchar(d, sizeof(d), 0);
  fillchar(mas, sizeof(mas), 0);

  read(n);

  for i := 0 to n - 1 do
    read(mas[i]);

  for i := 0 to n - 1 do begin
    UpDate(mas[i], 1);
    d[mas[i]] := sum(1000000) - sum(mas[i]);
  end;
  n := 0;
  for i := 0 to 1000001 do inc(n, d[i]);
  write(n);
end.
