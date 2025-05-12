// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Contextora {
    string public constant name = "Contextora";
    string public constant symbol = "CTXT";

    mapping(address => uint256) public balances;

    function mint(address account, uint256 amount) external {
        balances[account] += amount;
    }
}
