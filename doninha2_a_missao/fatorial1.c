#include <stdio.h>

long fatorial(long n)
{
    if ((n==1) || (n==0))
        return 1;
    else
        return ( fatorial(n-1)*n );
}

int main(int argc, char** argv)
{
    long n;
    
    printf("Fatorial recursivo !!!!\n\n");
    
    scanf("%ld",&n);
    printf("fat(%ld) = %ld\n", n, fatorial(n));

	return 0;
}