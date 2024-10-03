; Definition for a binary tree node.
#|

; val : integer?
; left : (or/c tree-node? #f)
; right : (or/c tree-node? #f)
(struct tree-node
  (val left right) #:mutable #:transparent)

; constructor
(define (make-tree-node [val 0])
  (tree-node val #f #f))

|#
(define/contract (is-same-tree p q)
  (-> (or/c tree-node? #f) (or/c tree-node? #f) boolean?)
  (cond
    [(and (not p) (not q)) #t] ; Begge trær er null, returner true
    [(or (not p) (not q)) #f]  ; Enten p eller q er null, returner false
    [(not (= (tree-node-val p) (tree-node-val q))) #f] ; Verdiene er ikke like, returner false
    [else
     (and (is-same-tree (tree-node-left p) (tree-node-left q)) ; Rekursiv sjekk av venstre subtre
          (is-same-tree (tree-node-right p) (tree-node-right q)))])) ; Rekursiv sjekk av høyre subtre