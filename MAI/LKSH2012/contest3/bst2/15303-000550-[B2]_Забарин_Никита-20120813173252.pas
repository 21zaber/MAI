program b01;

{$APPTYPE CONSOLE}

uses
  SysUtils;

const
  num = 100000;

type
  TElem = record
    x, y : integer;
    l, r : integer;
  end;
  TPair = record
    a, b : integer;
  end;

var
  stack, sz : array [0..num] of integer;
  r, t, i, n, q : integer;
  a : array [1..num] of TElem;
  s : string;
  tmp : TPair;

function cnt(t : integer): integer;
begin
 result := 0;
 if t = -1 then exit;
 result := sz[t];
end;

procedure update(t : integer);
begin
 if t = -1 then exit;
 sz[t] := cnt(a[t].l) + cnt(a[t].r) + 1;
end;

procedure push(a : integer);
begin
  inc(r);
  stack[r] := a;
end;

function new : integer;
begin
  result := stack[r];
  dec(r);
end;

function merge (t1, t2 : integer) : integer;
begin
  result := t2;
  if t1 = -1 then exit;
  result := t1;
  if t2 = -1 then exit;
  if (a[t1].y > a[t2].y) then begin
    a[t1].r := merge(a[t1].r, t2);
    update(t1);
    result := t1;
  end
  else begin
    a[t2].l := merge(t1, a[t2].l);
    update(t2);
    result := t2;
  end
end;

function split (t, k : integer): TPair;
var
  tmp : TPair;
begin
  result.a := -1;
  result.b := -1;
  if t = -1 then exit;
  if k > a[t].x then begin
    tmp := split(a[t].r, k);
    a[t].r := tmp.a;
    update(t);
    update(tmp.b);
    result.a := t;
    result.b := tmp.b;
  end
  else begin
    tmp := split(a[t].l, k);
    a[t].l := tmp.b;
    update(tmp.a);
    update(t);
    result.a := tmp.a;
    result.b := t;
  end;
end;

function exist (t, k: integer) : boolean;
begin
  result := false;
  if t = -1 then exit;
  result := true;
  if a[t].x = k then exit;
  if a[t].x > k then begin
    result := exist(a[t].l, k);
    exit;
  end;
  if a[t].x < k then begin
    result := exist(a[t].r, k);
    exit;
  end;
end;

function insert (t, k : integer) : integer;
var
  p : integer;
  tmp : TPair;
begin
  result := t;
  if exist(t, k) then exit;
  p := new;
  a[p].x := k;
  a[p].y := random(100000000);
  a[p].l := -1;
  a[p].r := -1;
  tmp := split(t, k);
  tmp.a := merge(tmp.a, p);
  result := merge(tmp.a, tmp.b);
end;

function delete (t, k : integer): integer;
begin
  result := -1;
  if t = -1 then exit;
  if a[t].x < k then begin
    a[t].r := Delete(a[t].r, k);
    result := t;
    exit;
  end;
  if a[t].x > k then begin
    a[t].l := delete(a[t].l, k);
    result := t;
    exit;
  end;
  result := merge(a[t].l, a[t].r);
end;



procedure exists (t, k: integer);
begin
 if exist(t, k) then
   writeln('true')
 else
   writeln('false');
end;

function next (t, key : integer): TPair;
var
  tmp : TPair;
  v : integer;
begin
  tmp := split(t, key + 1);
  v := tmp.b;
  result.b := v;
  result.a := tmp.a;
  if v = -1 then exit;
  while a[v].l <> -1 do
    v := a[v].l;
  tmp.a := merge(tmp.a, tmp.b);
  tmp.b := v;
  result :=  tmp;
end;

function prev (t, key : integer) : TPair;
var
  tmp : TPair;
  v : integer;
begin
  tmp := split(t, key);
  v := tmp.a;
  result.a := t;
  result.b := v;
  if v = -1 then exit;
  while a[v].r <> -1 do
    v := a[v].r;
  result.a := merge(tmp.a, tmp.b);
  result.b := v;
end;

function kth (t, key : integer): integer;
begin
  result := -1;
  if t = -1 then exit;
  
  result := -1;
  if cnt(t) < key then exit;

  if key <= cnt(a[t].l) then begin
    result := kth(a[t].l, key);
    exit;
  end;

  if key = cnt(a[t].l) + 1 then begin
    result := a[t].x;
    exit;
  end;
  
  result := kth(a[t].r, key - cnt(a[t].l) - 1);
end;



begin
  reset(input, 'bst2.in');
  rewrite(output, 'bst2.out');
  Randomize;
  fillchar(stack, sizeof(stack), 0);
  fillchar(a, sizeof(a), -1);
  r := 0;
  for i:= num downto 1 do push(i);
  t := -1;
  while not(eof(input)) do begin
    readln(s);
    if s[1] = 'i' then begin
      n := strtoint(copy(s, 8, 10));
      t := insert(t, n);
    end;
    if s[1] = 'e' then begin
      n := strtoint(copy(s, 8, 10));
      exists(t, n);
    end;
    if s[1] = 'd' then begin
      n := strtoint(copy(s, 8, 10));
      t := delete(t, n);
    end;
    if s[1] = 'n' then begin
      n := strtoint(copy(s, 6, 10));
      tmp := next(t, n);
      t := tmp.a;
      if  tmp.b = -1 then
        writeln('none')
      else
        writeln(a[tmp.b].x);
    end;
    if s[1] = 'p' then begin
      n := strtoint(copy(s, 6, 10));
      tmp := prev(t, n);
      t := tmp.a;
      if  tmp.b = -1 then
        writeln('none')
      else
        writeln(a[tmp.b].x);
    end;
    if s[1] = 'k' then begin
      n := strtoint(copy(s, 5, 10));
      q := kth(t, n);
      if  q = -1 then
        writeln('none')
      else
        writeln(q);
    end;
  end;
  close(input);
  close(output);
end.
