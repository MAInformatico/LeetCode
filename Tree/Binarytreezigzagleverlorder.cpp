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
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>>matrix;
   
        if(root==NULL) return matrix;
        vector<int>aux;

        deque<TreeNode*>q;
        q.push_back(root);

        bool flag=false;

        while(!q.empty()){
            int l=q.size();
            for(int i=0;i<l;i++){
               TreeNode* current=  q.front();
                q.pop_front();
                 aux.push_back(current->val);
                if(current->left)
                    q.push_back(current->left);
                if(current->right)
                    q.push_back(current->right);

            }
            if (flag) 
            reverse(begin(aux), end(aux));
            flag = !flag;
            matrix.push_back(aux);
            aux.clear();
        }

    return matrix;
    }
};
