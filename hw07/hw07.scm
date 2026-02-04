(define (square n) (* n n))

(define (pow base exp) (cond ((= exp 0) 1) ((= exp 1) base) 
((= exp 2) (square base)) 
((> exp 2) (if (even? exp) (pow (pow base (quotient exp 2)) 2) (* base (pow base (- exp 1)))))))

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (begin (define y (repeatedly-cube (- n 1) x)) (pow y 3))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))
