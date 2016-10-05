program b01;

{$R+}
{$D+}
{$Q+}

{$APPTYPE CONSOLE}

uses
  SysUtils;

var
 f : array [-1..150, -1..150, -1..150]  of int64;
 n, m, x1, x2, y1, y2, z1, z2, v : integer;

procedure up (var x : integer);
begin
  x := x or (x + 1);
end;

procedure down (var x : integer);
begin
  x := (x and (x + 1)) - 1;
end;

procedure UpDate(x, y, z, v : integer);
var
 x0, y0, z0 : integer;
begin
  x0 := x;
  while x0 < n do begin
    y0 := y;
    while y0 < n do begin
      z0 := z;
      while z0 < n do begin
        inc(f[x0, y0, z0], v);
        up(z0);
      end;
      up(y0);
    end;
    up(x0);
  end;
end;

function Sum (x, y, z : integer) : int64;
var
 x0, y0, z0 : integer;
begin
  result := 0;
  x0 := x;
  while x0 >= 0 do begin
    y0 := y;
    while y0 >= 0 do begin
      z0 := z;
      while z0 >= 0 do begin
        inc(result, f[x0, y0, z0]);
        down(z0);
      end;
      down(y0);
    end;
    down(x0);
  end;
end;

begin
  reset(input, 'stars.in');
  rewrite(output, 'stars.out');
  fillchar(f, sizeof(f), 0);
  readln(n);
  m := 1;
  while m <> 3 do begin
    read(m);
    if m = 1 then begin
      readln(x1, y1, z1, v);
      //dec(x1); dec(y1); dec(z1);
      UpDate(x1, y1, z1, v);
    end;
    if m = 2 then begin
      readln(x1, y1, z1, x2, y2, z2);
      dec(x1); dec(y1); dec(z1);
      //dec(x2); dec(y2); dec(z2);
      writeln(Sum(x2, y2, z2) - Sum(x1, y1, z1) -
              Sum(x1, y2, z2) - Sum(x2, y1, z2) - Sum(x2, y2, z1) +
              Sum(x1, y1, z2) + Sum(x1, y2, z1) + Sum(x2, y1, z1));
    end;
  end;
end.
