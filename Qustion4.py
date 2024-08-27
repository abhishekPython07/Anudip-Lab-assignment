a=6
for i in range (a):

    for j in range(i,a):
        print(" ",end="  ")
    for k in range(i+1):
        print("*",end="  ")
    print()  


    #         * 
    #       * * 
    #     * * * 
    #   * * * * 
    # * * * * *