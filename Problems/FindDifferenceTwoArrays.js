/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    let result = [];
    auxNums1 = new Set(nums1);
    auxNums2 = new Set(nums2);
    const firstOnlyElements = [...auxNums1].filter(element => !auxNums2.has(element));
    const secondOnlyElements = [...auxNums2].filter(element => !auxNums1.has(element));
    result.push(firstOnlyElements);
    result.push(secondOnlyElements);
    return result;
};
