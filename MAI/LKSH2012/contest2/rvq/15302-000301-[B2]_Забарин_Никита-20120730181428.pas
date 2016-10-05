program c01;

{$R+}

{$APPTYPE CONSOLE}

uses
  SysUtils, Math;

type
  TPoint = record
    x, y : integer;
  end;
  
  TElem = record
    mmax, mmin : integer;
    l, r : integer;
  end;

var
  m, k, i : integer;
  tree : array [0..1000000] of TElem;
  mas : array [0..300000] of integer;
  t : TElem;
  q : array [0..300000] of TPoint;

procedure Build(l, r, id : integer);
begin
  tree[id].l := l;
  tree[id].r := r;
  if r - l = 1 then begin
    tree[id].mmin := mas[l];
    tree[id].mmax := mas[l];
  end
  else begin
    Build(l, (r + l) div 2, id * 2);
    Build((r + l) div 2, r, id * 2 + 1);
    tree[id].mmin := min(tree[id * 2].mmin, tree[id * 2 + 1].mmin);
    tree[id].mmax := max(tree[id * 2].mmax, tree[id * 2 + 1].mmax);
  end;
end;

procedure UpDate(id, n : integer; v : integer);
begin
  if (n >= tree[id].r) or (n < tree[id].l) then exit;
  if tree[id].r - tree[id].l = 1 then begin
    tree[id].mmin := v;
    tree[id].mmax := v;
  end
  else begin
    Update(id * 2, n, v);
    Update(id * 2 + 1, n, v);
    tree[id].mmin := min(tree[id * 2].mmin, tree[id * 2 + 1].mmin);
    tree[id].mmax := max(tree[id * 2].mmax, tree[id * 2 + 1].mmax);
  end;
end;

function Proc(l, r, id : integer) : TElem;
var
 t1, t2 : TElem;
begin
  if (tree[id].l >= r) or (tree[id].r <= l) then begin
    result.mmin := 1000000000;
    result.mmax := -1000000000;
    exit;
  end;
  if (l <= tree[id].l) and (tree[id].r <= r) then begin
    result.mmax := tree[id].mmax;
    result.mmin := tree[id].mmin;
    exit;
  end;
  t1 := Proc(l, r, id * 2);
  t2 := Proc(l, r, id * 2 + 1);
  result.mmin := min(t1.mmin, t2.mmin);
  result.mmax := max(t1.mmax, t2.mmax);
end;

begin
  reset(input, 'rvq.in');
  rewrite(output, 'rvq.out');
  readln(k);
  m := -1 ;
  for i := 1 to k do begin
    readln(q[i].x, q[i].y);
    if abs(q[i].x) > m then m := abs(q[i].x);
    if q[i].y > m then m := q[i].y;
  end;
  for i := 0 to m do
    mas[i] := (sqr(i mod 12345)) mod 12345 + (sqr(i mod 23456) mod 23456 * (i mod 23456)) mod 23456;
  Build(1, m + 1, 1);
  for i:= 1 to k do begin
    if q[i].x < 0 then
      UpDate(1, abs(q[i].x), q[i].y)
    else begin
      t := Proc(q[i].x, q[i].y + 1, 1);
      writeln(t.mmax - t.mmin);
    end;
  end;


end.
 