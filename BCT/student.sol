//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract studentAdd{
    //structure
    struct Student{
        string name;
        uint256 rollno;

    }
    //array
    Student[] public studentarr;
    function addStudent(string memory name,uint rollno) public{
        for(uint i=0;i<studentarr.length;i++){
            if(studentarr[i].rollno==rollno){
                revert("student with this roll no already exists");
            }
        }
        studentarr.push(Student(name,rollno));

    }
    function getStudentslength() public view returns(uint){
        return studentarr.length;

    }
    function displayAllstudent() public view returns(Student[] memory){
        return studentarr;
    }

    function getStudentByIndex(uint idx) public view returns (Student memory){
        require(idx<studentarr.length,"index out of bound!");
        return studentarr[idx];
    }
    

    //fallback
    fallback() external payable { }
    receive() external payable { }
}
