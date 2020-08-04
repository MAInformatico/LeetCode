class Solution {
    public String simplifyPath(String path) {
        Stack<String> aux = new Stack<>();
        for(String i : path.split("/")){
            if(i.equals("..")){
                if(!aux.isEmpty())
                    aux.pop();
            }else if(i.length() > 0 && !i.equals(".")){
                aux.add(i);                              
            }
        }
        return "/" + String.join("/",aux);
    }
}
