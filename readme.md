# Problem 1
You are given an array of objects representing items to be put in a knapsack. The objects have 3 attributes: "name", "weight", and "value". The items need to be selected so that the total "weight" does not exceed the maximum "weight" and the "value" is maximized.

* Test Case 1: 
  * knapsack([{ "name":'map', "weight":9, "value":150 }, { "name":'compass', "weight":13, "value":35 }, { "name":'water', "weight":153, "value":200 }, { "name":'sandwich', "weight":50, "value":160 }, { "name":'glucose', "weight":15, "value":60 }, { "name":'tin', "weight":68, "value":45 }, { "name":'banana', "weight":27, "value":60 }, { "name":'apple', "weight":39, "value":40 }], 100) should return 405.
* Test Case 2: 
  * knapsack([{ "name":'map', "weight":9, "value":150 }, { "name":'compass', "weight":13, "value":35 }, { "name":'water', "weight":153, "value":200 }, { "name":'sandwich', "weight":50, "value":160 }, { "name":'glucose', "weight":15, "value":60 }, { "name":'tin', "weight":68, "value":45 }, { "name":'banana', "weight":27, "value":60 }, { "name":'apple', "weight":39, "value":40 }], 200) should return 510.
* Test Case 3: 
  * knapsack([{ "name":'cheese', "weight":23, "value":30 }, { "name":'beer', "weight":52, "value":10 }, { "name":'suntan cream', "weight":11, "value":70 }, { "name":'camera', "weight":32, "value":30 }, { "name":'T-shirt', "weight":24, "value":15 }, { "name":'trousers', "weight":48, "value":10 }, { "name":'umbrella', "weight":73, "value":40 }], 100) should return 145.
* Test Case 4: 
  * knapsack([{ "name":'cheese', "weight":23, "value":30 }, { "name":'beer', "weight":52, "value":10 }, { "name":'suntan cream', "weight":11, "value":70 }, { "name":'camera', "weight":32, "value":30 }, { "name":'T-shirt', "weight":24, "value":15 }, { "name":'trousers', "weight":48, "value":10 }, { "name":'umbrella', "weight":73, "value":40 }], 200) should return 185.
* Test Case 5: 
  * knapsack([{ "name":'waterproof trousers', "weight":42, "value":70 }, { "name":'waterproof overclothes', "weight":43, "value":75 }, { "name":'note-case', "weight":22, "value":80 }, { "name":'sunglasses', "weight":7, "value":20 }, { "name":'towel', "weight":18, "value":12 }, { "name":'socks', "weight":4, "value":50 }, { "name":'book', "weight":30, "value":10 }], 100) should return 237.
* Test Case 6: 
  * knapsack([{ "name":'waterproof trousers', "weight":42, "value":70 }, { "name":'waterproof overclothes', "weight":43, "value":75 }, { "name":'note-case', "weight":22, "value":80 }, { "name":'sunglasses', "weight":7, "value":20 }, { "name":'towel', "weight":18, "value":12 }, { "name":'socks', "weight":4, "value":50 }, { "name":'book', "weight":30, "value":10 }], 200) should return 317.'


# Problem 2
Given a string (string brackets) containing just the characters '(', ')', '{', '}', '[' and ']', return a result to determine if the input string is valid. A valid string must adhere to the following rules:

1. Open brackets must be closed by the same type of brackets.

2. Open brackets must be closed in the correct order.

Example:

* Test Case 1: 
  * ( ) [ ] { } should return true
* Test Case 2: 
  * ( [ ) ] should return false
* Test Case 3: 
  * { { [] ( } } ) should return false
* Test Case 4: 
  * { [ ( ) ] } should return true


# Problem 3
Given a short video, (use your own > 60 second video), use OpenCV to clip a 5 second clip from the 00:30 mark to the 00:35 mark and draw a red 100 x 100 pixel sized box in the middle of the video.

# Running the Solution

When you run the problemsMain.py file it will first execute the Problem 3 solution by displaying the clip and generated rectangle and also saves the resultant clip as output-problem-3.mp4 file in the project folder.

There after it will run all the test cases to the Problem 1 and Problem 2.