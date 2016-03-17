(defrule unity
   (interest games)
   (experience threeD)
   (experience csharp)
   (agecat above12)
=>
   (assert (learn unity))
)

(defrule xna
   (interest games)
   (experience csharp)
   (agecat above12)
=>
   (assert (learn xna))
)

(defrule kodu
   (interest games)
   (agecat above6)
=>
   (assert (learn kodu))
)

(defrule scratch "Everyone above 6 should learn to scratch"
   (agecat above6)
=>
   (assert (learn scratch))
)

(defrule csharp
   (agecat above12)
   (not (experience csharp))
   (interest programming)
=>
   (assert (learn csharp))
)

(defrule age-above-12
   (age ?x)
   (test (>= ?x 12))
=>
   (assert (agecat above12))
)

(defrule age-above-6
   (age ?x)
   (test (and (> ?x 6) (< ?x 12)))
=>
   (assert (agecat above6))
)
