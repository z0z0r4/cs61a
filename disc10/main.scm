(define (fit total n)
    (define (f total n k)
        (if (and (= n 0) (= total 0))
            #t
        (if (or (< n 0) (< total 0) (< total (* k k)))
            #f
            (or (f (- total (* k k)) (- n 1) (+ k 1)) (f total n (+ k 1)))
        )))
    (f total n 1))