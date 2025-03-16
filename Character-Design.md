## Base Character Class
* Name: String
* Base_Health: Int/Float
* Base_Attack: Int/Float
* Special_Attack: Int/Float (fruit attack, 0 if character has leopard fruit)
* Defense: Int/Float
* Speed: Int/Float
* Fruit_Ability: String (leopard, acid, or salt) 
* Haki_Points: Int (1 - 10)
* Weapon: Weapon class (will take an enum of either spear, axe, sword) 

## Player Character
* Derived from base character class

## Normal Enemy 1 
### (Marine in 1st fight of pirate intro)
* Derived from base character class

## Normal Enemy 2
### (Pirate in 1st fight of marine intro)
* Derived from base character class

## Final Boss 
### (logia user: while transformed is true, they can only be hurt if the player has haki points)
* Derived from base character class
* Transformed: Int (determines if they are vulnerable at that time, starts at 100 at initial transformation, goes down 20 each successful hit)