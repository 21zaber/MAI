parents("Bobby Jo Cox", "Bob Cox", "Joann Para").

shurin(X, Ans):-
	parents(_, X, Wife),
	parents(Wife, A, B),
	parents(Sh, A, B),
	parents(_, Sh, _).
