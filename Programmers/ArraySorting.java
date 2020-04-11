package algorithm;

public class ArraySorting {
	public boolean solution(int[] arr) {
        boolean answer = false;
        boolean ascending = true;
        boolean descending = true;
        for(int i=0; i<arr.length-1; i++){
            if(arr[i] >= arr[i+1]){
                ascending = true;
            }else{
                ascending = false;
                break;
            }
        }
        for(int j=0; j<arr.length-1; j++){
            if(arr[j] <= arr[j+1]){
                descending = true;
            }else{
                descending = false;
                break;
            }
        }
        if((ascending == true && descending == false) || (ascending == false && descending == true)){
            answer = true;
        } 
        return answer;
    }
}
