def nonrec_merge_sort(a,s):
    group=1
    while group<=s:
        step=group*2
        for i in range(s-group*2,step):
            a1=[0]*group
            a2=[0]*group
            res=[0]2+group
            copy(a,a1,i,i+group-1)
            copy(a,a2,i+group,i+2*group-1)
            merge(a1,a2,res)
        #copy res into array at index i
        group=group*2