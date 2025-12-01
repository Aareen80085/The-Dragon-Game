# Dragon Slayer Game - Technical Report

## Abstract

This report presents a comprehensive analysis of "Dragon Slayer," a text-based role-playing game implemented in Python. The game features turn-based combat mechanics, a quest system with number-guessing puzzles, and dynamic difficulty scaling through player buffs. The player engages in battle against a dragon with options to fight or flee to a village quest that can provide significant power upgrades. This document examines the game's architecture, mechanics, implementation details, and provides recommendations for future enhancements.

## 1. Introduction

Dragon Slayer is an interactive console-based adventure game that combines traditional RPG combat with puzzle-solving elements. The game demonstrates fundamental programming concepts including object-oriented design, random number generation, input validation, and game loop architecture. Players must strategically decide whether to continue fighting a powerful dragon or seek assistance through a village quest that offers substantial combat advantages.

## 2. Work Documentation

### Game Flow

The game follows a main loop structure that continues until either the player or dragon is defeated. Within this loop, players make tactical decisions that affect the battle outcome and can access a secondary quest system that modifies core gameplay parameters.

### 2.1 Combat System

The combat system implements turn-based mechanics where:

- Damage calculation uses randomization within bounds defined by attack_power
- Player initiates attacks first when choosing to fight
- Dragon counterattacks if it survives the player's turn
- Health values are reduced by damage amounts until one combatant reaches zero or below

### 2.2 Quest Mechanism

When players choose to flee (option 2), they encounter a number-guessing minigame:

- A secret two-digit number is randomly generated (range: 10-99)
- Players receive 5 attempts to guess correctly
- Input validation ensures only numeric entries are processed
- Contextual hints guide players based on digit count errors
- Success grants the "Dragon Breaker" buff, increasing attack_power to 1000
- After quest completion (success or failure), players return to the main battle

### 2.3 Input Validation

The quest system includes robust validation:

- Non-numeric inputs are rejected with appropriate messaging
- Single-digit guesses receive hints about missing place values
- Three-digit guesses are flagged as exceeding requirements
- Valid two-digit guesses proceed to comparison logic

### 2.4 Game States

Three possible end states exist:

1. **Player Victory**: Dragon health reaches zero while player survives
2. **Player Defeat**: Player health reaches zero while dragon survives
3. **Ongoing Battle**: Loop continues until one condition is met

![image.png](attachment:866e99b9-fe89-4204-a4f4-56c43ce00d78:image.png)

## 3. System Architecture

### 3.1 Class Structure

The game employs an object-oriented architecture with two primary entity classes:

**Player Class**

- Attributes: name (string), health (integer, initial value 100), attack_power (random integer between 5-10)
- Methods: attack(), is_alive()
- Represents the human-controlled character with relatively low starting power

**Dragon Class**

- Attributes: name (string, fixed as "Dragon"), health (integer, initial value 120), attack_power (random integer between 50-100)
- Methods: attack(), is_alive()
- Represents the antagonist with significantly higher combat capabilities

![image.png](attachment:aa73e232-9a5b-4a5d-a575-9a3dacfdd287:image.png)

https://miro.com/app/board/uXjVJ4hkB3Y=/?share_link_id=414655211566

## 5. Technical Analysis

### 5.1 Strengths

- **Clear Object-Oriented Design**: Separation of concerns between player and enemy entities
- **Engaging Gameplay Loop**: Multiple strategic options create decision-making depth
- **Robust Input Validation**: Comprehensive error checking in the quest system
- **Dynamic Difficulty**: The buff system allows players who struggle in combat to gain advantages through puzzle-solving
- **User Feedback**: Consistent status updates and clear messaging enhance user experience

### 5.2 Areas for Improvement

- **Balance Issues**: The 1000 attack_power buff makes combat trivial after the quest, reducing challenge
- **Limited Replayability**: Static dragon stats and single enemy type limit variety
- **No Healing Mechanism**: Players cannot recover health, making early mistakes potentially fatal
- **Quest Repeatability**: Players can only attempt the village quest once per game session
- **Random Difficulty Variance**: Dragon attack_power range (50-100) creates significant luck-based difficulty swings

## 6. Recommendations

### 6.1 Gameplay Enhancements

- Implement a more balanced buff system (e.g., attack_power multiplied by 3-5 instead of set to 1000)
- Add healing potions or rest mechanics between combat rounds
- Introduce multiple enemy types with varied stats and abilities
- Create a leveling system based on successful attacks or quest completion
- Allow quest reattempts with increasing difficulty or decreasing rewards

### 6.2 Technical Improvements

- Add save/load functionality for persistent progress
- Implement error handling for unexpected inputs
- Create configuration files for easy stat balancing
- Add unit tests for combat calculations and input validation
- Develop a graphical user interface for enhanced accessibility

### 6.3 Content Expansion

- Multiple quest types beyond number guessing (riddles, inventory management, etc.)
- Story elements that provide context for the dragon battle
- Achievement system to track player accomplishments
- Multiple endings based on player choices and performance

## 7. Conclusion

Dragon Slayer successfully demonstrates fundamental game development concepts within a text-based framework. The combination of combat and puzzle-solving creates an engaging experience that balances skill and strategy. The object-oriented architecture provides a solid foundation for future expansion, while the current implementation offers clear, maintainable code suitable for educational purposes or as a prototype for more complex games.

The game's primary achievement is its integration of multiple gameplay systems into a cohesive experience. While balance improvements and additional content would enhance long-term engagement, the current version effectively showcases core programming principles including class design, control flow, random number generation, and user input handling. With the recommended enhancements, Dragon Slayer could evolve into a more sophisticated RPG experience while maintaining its accessible, console-based charm.

---

**Document Information**

- Report Type: Technical Documentation
- Subject: Dragon Slayer Game Analysis
- Programming Language: Python 3.x
- Date: November 2025
