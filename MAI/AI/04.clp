(deffacts initial-state
      (Ds 800)        
      (Dm 2)     
      (Da 2)  
          (Dar 1))    

(defrule  rule1
  (Ds 10)         
  (Dm 1)     
  (Da 1)         
=>
 (printout t  "Rule1: Vr=A, Vm=10, T=0, I=1, G=tor "  crlf))


(defrule  rule2
  (Ds 10)         
  (Dm 2)     
  (Da 2)         
=>
 (printout t  "Rule2: Vr=B, Vm=10, T=1, I=1, G=line, Rm=40, J=80, S=60 "  crlf))    

(defrule  rule3
  (Ds 300)         
  (Dm 2)        
=>
 (printout t  "Rule3: Vr=B, Vm=20, T=2, I=1, G=tor "  crlf))

(defrule  rule4
  (Ds 300)            
  (Da 3)         
=>
 (printout t  "Rule4: Vr=C, Vm=40, T=3, I=2, G= line, Rm=50, J=75, S=75"  crlf))

(defrule  rule5
  (Ds 800)         
  (Dm 2)     
  (Da 2)         
  (Dar 1)   
=>
 (printout t  "Rule5: Vr=B, Vm=60, T=4, I=2, G= line, Rm=60, J=70, S=70 "  crlf))

(defrule  rule6_7
  (Ds 800)             
  (Dar ?num)  
=>
  (if (< ?num 3)  
    then
     (printout t "Rule6: Vr=B, Vm=40, T=6, I=3, G= line, Rm=60, J=60, S=75 "  crlf)
    else
     (printout t "Rule7: Vr=C, Vm=80, T=6, I=3, G= line, Rm=60, J=60, S=75 "  crlf))) 
