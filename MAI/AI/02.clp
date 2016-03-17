(deftemplate foo
    (slot age)
)
(deftemplate foo1
    (slot q )
)

(defrule coco
=>
    (assert ( foo1 (q 150)))
)
(reset)
(assert (foo (age 15)))
(run)
(facts)

