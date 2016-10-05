program a01;

{$R+}
{$D+}
{$Q+}

{$APPTYPE CONSOLE}

uses
  SysUtils;

var
 f : array [-1..1000000]  of int64;
 mas : array [-1..1000000] of integer;
 n, k, i, id, x : integer;
 ch : char;

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
  while i < n do begin
    inc(f[i], x);
    up(i);
  end;
end;

function Sum (r : integer) : int64;
begin
  result := 0;
  while r >= 0 do begin
    inc(result, f[r]);
    down(r);
  end;
end;

begin
  reset(input, 'sum.in');
  rewrite(output, 'sum.out');
  fillchar(mas, sizeof(mas), 0);
  fillchar(f, sizeof(f), 0);
  readln(n ,k);
  for i := 1 to k do begin
    read(ch);
    readln(id, x);
    if ch = 'A' then begin
      UpDate(id - 1, x - mas[id]);
      mas[id] := x;
    end;
    if ch = 'Q' then begin
      writeln(Sum(x - 1) - Sum(id - 2));
    end;
  end;
end.
