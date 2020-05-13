var searchInsert = function(nums, target) {
    let result = 0;
  if (nums.includes(target)  === false){
      let i = 0;
      while(nums[i]<target){
          i++;
      }
      result = i;
  }
  else{
      result = nums.indexOf(target);
  }    
    return result;
};
