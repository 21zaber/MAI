(deftemplate data 
    (slot x) 
    (slot y)
)        

(defrule twice
    (data (x ?x) )
    (test (> ?x 2))
=>
    (assert (data (x 123)))
)

(reset)


(assert (data (x 3) (y 0)))
(facts)
(run)
(facts)
