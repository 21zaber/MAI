program c01;

{$APPTYPE CONSOLE}

uses
  SysUtils, Math;

const
  inf = 1000000000;

type
  dmas = record
    s, f, len : integer;
  end;
  TElem = record
    key, id, next : integer;
  end;

var
  mas : array [0..500000] of TElem;
  m, num : array[1..100000] of integer;
  n, k, a, b, i, c, T, count, v0 : integer;
  time_in, up, color : array [1..100000] of integer;
  ans : array[-1..500000] of boolean;

procedure add (const x, id : integer; var a : integer);
begin
  //mas[a].next := c;
  mas[c].next := a;
  mas[c].id := id;
  mas[c].key := x;
  a := c;
  inc(c);
end;

procedure dfs (v, q : integer);
var
  w, vto, vfrom : integer;
begin
  time_in[v] := T;
  inc(T);
  up[v] := time_in[v];
  color[v] := 1;



  w := m[v];
  while w <> -1 do begin
    vto := mas[w].key;
    vfrom := mas[w].id;
    if color[vto] = 0 then begin
      if v = v0 then inc(num[v]);
      dfs(vto, vfrom);
      up[v] := min(up[v], up[vto]);
      if (up[vto] >= time_in[v]) and (v <> v0) then ans[v] := true;
    end
    else if vfrom <> q then
      up[v] := min(up[v], time_in[vto]);
    w := mas[w].next;
  end;
end;


begin
  reset(input, 'points.in');
  rewrite(output, 'points.out');
  readln(n, k);
  c := 1;
  for i:= 1 to n do
    m[i] := -1;
  for i := 1 to k do begin
    readln(a, b);
    add(b, i, m[a]);
    add(a, i, m[b]);
  end;
  fillchar(time_in, sizeof(time_in), 0);
  fillchar(color, sizeof(color), 0);
  fillchar(up, sizeof(up), 0);
  T := 0;
  for i := 1 to n do begin
    if color[i] = 0 then begin
      v0 := i;
      dfs(v0, 0);
    end;
    if num[v0] > 1 then ans[v0] := true;
  end;
  count := 0;
  for i := 1 to k do
    if ans[i] then inc(count);
  writeln(count);
  for i := 1 to k do
    if ans[i] then write(i, ' ');
end.
 