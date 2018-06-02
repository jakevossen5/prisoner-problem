# PrisonerStats

This project was inspired by [100 Prisoners Problem](https://news.ycombinator.com/item?id=16984815) that I first saw on Hacker News. 
A great description of this problem can be found [here](http://datagenetics.com/blog/december42014/index.html).

The basics are, there are 100 prisoners, each with a number.
There are 100 boxes.
Each prisoner gets to pick 50 of the 100 boxes, and if every prisoner finds their own number, then the whole group survives.
But if one prisoner doesn't find his number, it all fails. 
The group gets to talk once before they start opening boxes, but after that they can't communicate.

At first it seems hopeless, as it is .5^100 odds of making it, but doing some clever math you can have them survive about 30% of the time.
The 'tick' is that you number all of the boxes, and each prisoner starts by opening the box with his number on the outside.
Then, if that number is not his, he goes to the box numbered with the number he found inside that box.
This way, he is guaranteed to be in a loop with his number in it, and we can calculate the odds of a loop being greater than 50 in length.
I am obviously not very qualified to talk on the statistics part, the articles linked above go in a lot more detail. 

But, I am naturally suspicious of statisticians and they scare me a little, so I decided to code it in Python to test it out, and sure enough, you get about .31 every time, just as the papers suggest.

Please ignore spelling mistakes, was not goal of project.
