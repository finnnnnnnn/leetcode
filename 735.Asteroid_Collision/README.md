例:a=[8,-8,10,2,-5]
    １．a[0]入finalAster,a[0]/abs(a[0])入direction
    ２．若a[1]/abs(a[1])==1,将a[1]的值和方向入栈后继续；否则，比较a[0],a[1]两者绝对值，若abs(a[1])>abs(a[0]),则finalAster[]和direction[]pop，a[1]的值和方向入栈；若相等，finalAster[]和direction[]pop；否则，pass.
    ３．重复如２所示的步骤


