def main():
    n = int(input('Enter number of wheels :'))
    assert n<=10
    #PXi_1 = 1/(10 - i)
    PofE = 1
    for i in range(0,n,1):
        PofE = PofE*(1/(10 - i))

    print('Probability is : ',PofE)

if __name__=='__main__':
    main()




