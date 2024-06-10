(brilisp
    (define ((print int) (n int)))

    (define ((print_bool int) (b bool))
        (set (T int) (const 1))
        (set (F int) (const 0))
        (br b print_true print_false)
        (label print_true)
        (set (tmp int) (call print T))
        (ret tmp)
        (label print_false)
        (set (tmp int) (call print F))
        (ret tmp))

    (define ((main int))
        (set (v int) (const 4))
        (set (o1 int) (const 1))
        (set (bp (ptr bool)) (alloc v))
        (set (bp2 (ptr bool)) (ptradd bp o1))
        (set (b bool) (const true))
        (store bp b)
        (store bp2 b)
        (set (b bool) (load bp2))
        (set (tmp int) (call print_bool b))
        (ret tmp)))
