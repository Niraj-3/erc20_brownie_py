// contracts/OurToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract OurToken is ERC20 {
    //eth
    constructor(uint256 initialSupply) ERC20("NToken", "NT") {
        _mint(msg.sender, initialSupply);
    }
}