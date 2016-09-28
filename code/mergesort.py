def mergesort(a):
    if len(a)>1:
        half=int(len(a)/2)
        rh=a[half:]
        lh=a[:half]

        mergesort(lh)
        mergesort(rh)

        d=0
        e=0
        f=0
        #loops for merging
        while d<len(lh) and e<len(rh):
            if lh[d]>rh[e]:
                a[f]=rh[e]
                f=f+1
                e=e+1
            else:
                a[f]=lh[d]
                f=f+1
                d=d+1
        while d<len(lh):
            a[f]=lh[d]
            f=f+1
            d=d+1
        while e<len(rh):
            a[f]=rh[e]
            f=f+1
            e=e+1
