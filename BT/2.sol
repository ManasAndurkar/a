// // SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

// progma solidity ^0.8.0;

//

// contract Mycontract {
//     string name;       // stored in contract storage , global variable

//     uint public age;   // automatically get function is made if it is public

//     constructor() {   // if argument was given to constructor then we have to give at the time of deploy
//         name = "rahul";
//     }

//     function getname() public view returns (string memory) {   // in case of int , use only returns (uint)
//         // view  is used only for getting
//         return name;
//     }

//     // function setname(string newname) public  {
//     //     name = newname;
//     // }
//      function setage(uint nage) public  {
//         age = nage;
//     }
// }




contract array{

    //  2 types of array :
    // static and dynamic

    uint[4] public arr = [1,2,3,4] ;    //static array of size 4(0 to 3 index)

    uint[] public darr ;    // dynamic array

    function setstaticarr(uint index , uint value) public{
        arr[index] = value;
    }

    function lenofarr() public view returns (uint){
        return arr.length ; 
    }


    function pushindarr(uint value) public {
        darr.push(value);
    }

    function popdarr() public {
        darr.pop();
    }

}