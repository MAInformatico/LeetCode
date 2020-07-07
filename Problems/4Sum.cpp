class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        vector<vector<int>>result;
        for(int i=0;i<=n-4;i++){
            for(int j=i+1;j<=n-3;j++){
                int l=j+1,k=n-1;
                while(l<k){
                    if(nums[i]+nums[j]+nums[l]+nums[k]==target){
                        result.push_back({nums[i],nums[j],nums[l],nums[k]});
                        l++;
                    }else if(nums[i]+nums[j]+nums[l]+nums[k]>target){
                        k--;
                    }else{
                        l++;
                    }
                }
            }
        }
        sort(result.begin(),result.end());
        result.resize(distance(result.begin(),unique(result.begin(),result.end())));
        return result;
    }
};
