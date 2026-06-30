#include <stdio.h> 
#include <stdlib.h>
#include <stdbool.h>

int add (int x, int y)
{
	
	int answer;
	answer = x+y;
	return answer;
	
}

int sub (int x, int y)
{
	
	int answer;
	answer = x-y;
	return answer;
	
}

int  mult (int x, int y)
{
	
	int answer;
	answer = x*y;
	return answer;
	
}

bool division (int x, int y,float *answer)
{
	
	if( y == 0)
	{
		return false;
		
	}else{
		
		*answer = (float)x/(float)y;
		return true;
		
	}

	return answer;
	
}

int main(int argc, char* argv[])
{
	bool loop = true;
	do
	{
		int v1;
		int v2;
		v1 = atoi(argv[1]);
		v2 = atoi(argv[2]);
		printf("0 if done\n");
		printf("1 for Addition\n");
		printf("2 for Subtraction\n");
		printf("3 for Multiplication\n");
		printf("4 for Division\n");
		int want;
		scanf("%d", &want);
		if(want==0){
			
			loop = false;
			
		}else if(want==1){
			
			int answer;
			answer = add(v1,v2);
			printf("%d\n", answer);
			
		}else if(want==2){
			
			int answer;
			answer = sub(v1,v2);
			printf("%d\n", answer);
			
		}else if(want==3){
			
			int answer;
			answer = mult(v1,v2);
			printf("%d\n", answer);
			
		}else if(want==4){
			float answer;
			if(division(v1, v2, &answer)){
				printf("%f\n", answer);
			}else{
				printf("\n You can't divide by 0\n");
			}

		}
		
		
	}
	while (loop);
	printf("Program will now terminate");
	exit(EXIT_SUCCESS);
};