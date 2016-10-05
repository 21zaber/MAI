program a01;

{$APPTYPE CONSOLE}

uses
  SysUtils,
  Math;

type
  TElem = record
    value : int64;
    l, r : integer;
  end;
  TTree = array [1..300000] of TElem;

var
  used, inv, minv : TTree;
  mas : array [1..200000] of integer;
  n, i : integer;

function func (a, b : int64) : int64;
begin
  result := a + b;
end;

procedure Build(var tree : TTree; l, r, id : integer);
begin
  tree[id].l := l;
  tree[id].r := r;
  if r - l = 1 then
    tree[id].value := mas[l]
  else begin
    Build(tree, l, (r + l) div 2, id * 2);
    Build(tree, (r + l) div 2, r, id * 2 + 1);
    tree[id].value := func(tree[id * 2].value, tree[id * 2].value);
  end;
end;

procedure UpDate(var tree : TTree; id, n : integer; v : int64);
begin
  if (n >= tree[id].r) or (n < tree[id].l) then exit;
  if tree[id].r - tree[id].l = 1 then
    tree[id].value := v
  else begin
    Update(tree, id * 2, n, v);
    Update(tree, id * 2 + 1, n, v);
    tree[id].value := func(tree[id * 2].value, tree[id * 2 + 1].value);
  end;
end;

function Proc(var tree : TTree; l, r, id : integer) : int64;
begin
  if (tree[id].l >= r) or (tree[id].r <= l) then begin
    result := 0;
    exit;
  end;
  if (l <= tree[id].l) and (tree[id].r <= r) then begin
    result := tree[id].value;
    exit;
  end;
  result := func(Proc(tree, l, r, id * 2), Proc(tree, l, r, id * 2 + 1));
end;

begin
  reset(input, 'mega.in');
  rewrite(output, 'mega.out');

  fillchar(used, sizeof(used), 0);
  fillchar(inv, sizeof(inv), 0);
  fillchar(minv, sizeof(minv), 0);
  fillchar(mas, sizeof(mas), 0);

  readln(n);

  Build(used, 0, n, 1);
  Build(inv, 0, n, 1);
  Build(minv, 0, n, 1);

  for i := 0 to n - 1 do
    readln(mas[i]);

  for i := 0 to n - 1 do begin
    UpDate(used, 1, mas[i] - 1, 1);
    UpDate(inv, 1, mas[i] - 1, Proc(used, mas[i], n, 1));
    UpDate(minv, 1, mas[i] - 1, Proc(inv, mas[i], n, 1));
  end;

  write(Proc(minv, 0, n, 1));
end.
