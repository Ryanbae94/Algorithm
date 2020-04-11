package algorithm;
import java.util.Arrays;
class Solution {
    public int solution(int no, int[] works) {
        int result = 0;
        int temp = 0;
        Arrays.sort(works);
        
        for(int i=0; i<no; i++){
            for(int j=works.length-1; j>0; j--){
                if(works[j] < works[j-1]){
                    temp = works[j];
                    works[j] = works[j-1];
                    works[j-1] = temp;
                }else{
                    break;
                }                
            }
            if(works[works.length-1] == 0){
                break;
            }else{
                works[works.length-1]--;
            }
        }
        for(int i : works){
            result += i * i;
        }
                
        return result;
    }
}