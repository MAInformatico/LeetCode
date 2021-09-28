/**
 * @param {string[]} emails
 * @return {number}
 */

var numUniqueEmails = function(emails) {    
    const filterEmails = new Set();

    for (const iter of emails) {
        const arr = iter.split("@");
        arr[0] = (arr[0].split("+"))[0]; 
        arr[0] = arr[0].replace(/\./g, "");
        
        filterEmails.add(arr.join("@"));
    }

    return filterEmails.size;
};
