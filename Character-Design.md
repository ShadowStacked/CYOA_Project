# General
## Base Character Class
* Name: String
* Hit_Points: Int/Float
* Attack: Int/Float
* Fruit_Ability_Attack: Int/Float
* Defense: Int/Float
* Speed: Int/Float
* Fruit_Ability: String

## Player Character
* Derived from base character class
* Can_Harm_Logia_People: Boolean

## Final Boss (logia user: while transformed is true, each successful hit makes them 20% less invulnerable (100/5 => head, legs, arms). This should simulate hitting a body part making it revert to normal form.)
* Derived from base character class
* Transformed: Int (determines if they are vulnerable at that time, starts at 100 at initial transformation, goes down 20 each successful hit)