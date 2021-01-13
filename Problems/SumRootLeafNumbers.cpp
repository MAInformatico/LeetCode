/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <string>
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        int result=0;
        string aux="";
        explore(root,aux,result);
        return result;
    }
    
    void explore(TreeNode* root,string aux,int &currentResult){
        if(root==NULL)
            return;
        if(root->left==NULL&&root->right==NULL){
            aux+=to_string(root->val);
            currentResult+=stoi(aux);
            return;
        }
        //DFS
        explore(root->left,aux+to_string(root->val),currentResult);
        explore(root->right,aux+to_string(root->val),currentResult);
    }
};
