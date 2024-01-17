#include <stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
   int arr[n][n],r,l;
for(int i=0;i<n;i++)
{
    for(int j=0;j<n;j++)
    {
        scanf("%d",&arr[i][j]);
    }
}
int countdown=0,countdownzero=0,countup=0,countupzero=0;
    for(int i=0;i<n;i++)
{
    for(int j=0;j<n;j++)
    {
        if(i>j)
        {
            countdown++;
            if(arr[i][j]==0)
            {
                countdownzero++;
            }
        }
        if(i<j)
        {
            countup++;
            if(arr[i][j]==0)
            {
                countupzero++;
            }
        }
    }
}
if(countdown==countdownzero)
printf("Upper triangular matrix");
else if(countup==countupzero)
printf("Lower triangular matrix");
else
printf("Neither Upper nor Lower triangular matrix");


    return 0;
