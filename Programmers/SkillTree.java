package algorithm;

import java.util.Arrays;
public class SkillTree {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        int[] skill_index = new int[skill.length()];
        int[] sorted_skill_index = new int[skill.length()];
        
        for(String skill_tree : skill_trees){
            for(int i=0; i<skill.length(); i++){
                int idx = skill_tree.indexOf(skill.substring(i, i+1));
                if(idx == -1){
                    idx = skill_tree.length() + 1;
                }
                skill_index[i] = idx;
            }
            sorted_skill_index = skill_index.clone();
            Arrays.sort(sorted_skill_index);
            if(Arrays.equals(skill_index, sorted_skill_index)){
                answer++;
            }
        }
        return answer;
    }
}