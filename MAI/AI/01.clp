(deftemplate foo
    (slot age)
    (slot w)
)

(deftemplate foo1
    (slot q )
)
(assert (foo (age 15)))

(defrule coco
    ()
=>
    (assert (foo (w 150))) 
)

(reset)
(facts)
;"(run)"
(facts) 
