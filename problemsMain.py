from typing import Dict, Union, List

def knapsackHelper(maxWeight:int, weight: List[int], value: List[int], n:int) -> int:
    """
    Finds the maximum value that can be obtained by filling a knapsack of
    maximum weight `maxWeight` with `n` items having given `weight` and `value`.

    Parameters:
    -----------
    maxWeight : int
        Maximum weight of the knapsack.
    weight : List[int]
        A list of integers representing the weight of each item.
    value : List[int]
        A list of integers representing the value of each item.
    n : int
        Number of items to choose from.

    Returns:
    --------
    int
        Maximum value that can be obtained by filling the knapsack.
    """

    dp = [0 for i in range(maxWeight+1)]

    for i in range(1, n+1):
        for w in range(maxWeight, 0, -1):
            if weight[i-1] <= w:
                dp[w] = max(dp[w], dp[w-weight[i-1]]+value[i-1])
    
    return dp[maxWeight]

def problemOne(knapsack:List[Dict[str, Union[str, int]]], maxWeight:int) -> int:
    """
    Finds the maximum value that can be obtained by filling a knapsack of
    maximum weight `maxWeight` with the items given in the list `knapsack`.

    Parameters:
    -----------
    knapsack : List[Dict[str, Union[str, int]]]
        A list of dictionaries representing the items available to fill the knapsack.
        Each dictionary has keys "name", "weight", and "value".
        - "name" : str
            A string representing the name of the item.
        - "weight" : int
            An integer representing the weight of the item.
        - "value" : int
            An integer representing the value of the item.
    maxWeight : int
        Maximum weight of the knapsack.

    Returns:
    --------
    int
        Maximum value that can be obtained by filling the knapsack.
    """

    weight : List[int] = [obj["weight"] for obj in knapsack]
    value : List[int] = [obj["value"] for obj in knapsack]

    n = len(knapsack)

    return knapsackHelper(maxWeight, weight, value, n)

def problemTwo(brackets:str) -> bool:
    """
    Check whether a given string of brackets is balanced or not.

    Args:
    brackets (str): A string of brackets consisting of parentheses, curly brackets and square brackets.

    Returns:
    bool: True if the brackets in the input string are balanced, False otherwise.

    The function checks if the input string has an even length, if not returns False. Then, it initializes
    a dictionary with the corresponding opening and closing brackets. It also initializes a stack to store the 
    opening brackets. The function loops through the input string, and if the bracket is an opening bracket, it
    pushes it into the stack. If the bracket is a closing bracket, it checks if the stack is empty, and returns False
    if it is. It then pops the last bracket from the stack and checks if it is the corresponding opening bracket for
    the closing bracket. If not, returns False. Finally, it checks if the stack is empty, and returns True if it is,
    False otherwise.

    """

    if len(brackets) % 2 != 0:
        return False
    
    bracketPair : Dict[str,str] = {'(':')', '{':'}', '[':']'}

    stack : List[str] = []

    for bracket in brackets:
        if bracket in bracketPair.keys():
            stack.append(bracket)
        
        else:
            if stack == []:
                return False
            
            temp = stack.pop()
            if bracket!= bracketPair[temp]:
                return False
    
    return stack == []


def problemThree():
    """
    Extract a clip from an input video file between specified start and end times, 
    draw a red rectangle in the middle of each frame of the clip, and save the resulting 
    frames to an output video file. Uses the OpenCV library.

    Parameters: 
        None

    Returns:
        None
    """

    import cv2

    # Read the input video file
    input_video = cv2.VideoCapture('moon1.mp4')

    # Set the start and end time of the clip to extract (in seconds)
    start_time = 30
    end_time = 35

    # Get the frame rate of the input video
    fps = input_video.get(cv2.CAP_PROP_FPS)

    # Set the start and end frame numbers of the clip to extract
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)

    # Set the output video codec and file name
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter('output-problem-3.mp4', fourcc, fps, (int(input_video.get(3)), int(input_video.get(4))))

    # Iterate over the frames of the input video and extract the clip
    for i in range(start_frame, end_frame):
        ret, frame = input_video.read()
        
        # Draw a red rectangle in the middle of the frame
        cv2.rectangle(frame, (int(frame.shape[1]/2-50), int(frame.shape[0]/2-50)), 
                    (int(frame.shape[1]/2+50), int(frame.shape[0]/2+50)), (0, 0, 255), 2)
        
        # Write the frame to the output video
        output_video.write(frame)

        # Display the resulting frames
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the resources
    input_video.release()
    output_video.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":

    problemThree()


    import unittest

    class TestIsProblemOne(unittest.TestCase):
        """
        This class contains six unit test cases for the problemOne function, which solves the 0/1 knapsack problem. Each test case checks that the function returns the correct maximum value for a given knapsack and maximum weight. The test cases are as follows:

        testOne: checks the maximum value for a knapsack with a maximum weight of 100.
        testTwo: checks the maximum value for a knapsack with a maximum weight of 200.
        testThree: checks the maximum value for a different knapsack with a maximum weight of 100.
        testFour: checks the maximum value for a different knapsack with a maximum weight of 200.
        testFive: checks the maximum value for yet another knapsack with a maximum weight of 100.
        testSix: checks the maximum value for yet another knapsack with a maximum weight of 200.

        Each test case creates a knapsack using a list of items, each represented as a dictionary with 'name', 'weight', and 'value' keys. The maximum weight is also specified. The function problemOne is then called with the knapsack and maximum weight as arguments, and the result is compared to the expected maximum value using the assertEqual method. If the test fails, an error message is displayed. Otherwise, a success message is displayed.
        """

        def testOne(self):
            
            # Test Case 1
            knapsack = [{ "name":'map', "weight":9, "value":150 }, { "name":'compass', "weight":13, "value":35 }, { "name":'water', "weight":153, "value":200 }, { "name":'sandwich', "weight":50, "value":160 }, { "name":'glucose', "weight":15, "value":60 }, { "name":'tin', "weight":68, "value":45 }, { "name":'banana', "weight":27, "value":60 }, { "name":'apple', "weight":39, "value":40 }]
            maxWeight = 100

            maxValue = problemOne(knapsack, maxWeight)

            print(f"""
            Test Case 1: (Problem 1, 0/1 Knapsack) 
            The Maximum Value of Knapsack is: {maxValue}
            """)
            self.assertEqual(maxValue, 405)
        
        def testTwo(self):
            # Test Case 2
            knapsack = [{ "name":'map', "weight":9, "value":150 }, { "name":'compass', "weight":13, "value":35 }, { "name":'water', "weight":153, "value":200 }, { "name":'sandwich', "weight":50, "value":160 }, { "name":'glucose', "weight":15, "value":60 }, { "name":'tin', "weight":68, "value":45 }, { "name":'banana', "weight":27, "value":60 }, { "name":'apple', "weight":39, "value":40 }]
            maxWeight = 200

            maxValue = problemOne(knapsack, maxWeight)

            print(f"""
            Test Case 2: (Problem 1, 0/1 Knapsack)
            The Maximum Value of Knapsack is: {maxValue}
            """)
            self.assertEqual(maxValue, 510)
        
        def testThree(self):
            # Test Case 3
            knapsack = [{ "name":'cheese', "weight":23, "value":30 }, { "name":'beer', "weight":52, "value":10 }, { "name":'suntan cream', "weight":11, "value":70 }, { "name":'camera', "weight":32, "value":30 }, { "name":'T-shirt', "weight":24, "value":15 }, { "name":'trousers', "weight":48, "value":10 }, { "name":'umbrella', "weight":73, "value":40 }]
            maxWeight = 100

            maxValue = problemOne(knapsack, maxWeight)

            print(f"""
            Test Case 3: (Problem 1, 0/1 Knapsack)
            The Maximum Value of Knapsack is: {maxValue}
            """)
            self.assertEqual(maxValue, 145)        
        
        def testFour(self):
            # Test Case 4
            knapsack = [{ "name":'cheese', "weight":23, "value":30 }, { "name":'beer', "weight":52, "value":10 }, { "name":'suntan cream', "weight":11, "value":70 }, { "name":'camera', "weight":32, "value":30 }, { "name":'T-shirt', "weight":24, "value":15 }, { "name":'trousers', "weight":48, "value":10 }, { "name":'umbrella', "weight":73, "value":40 }]
            maxWeight = 200

            maxValue = problemOne(knapsack, maxWeight)

            print(f"""
            Test Case 4: (Problem 1, 0/1 Knapsack)
            The Maximum Value of Knapsack is: {maxValue}
            """)
            self.assertEqual(maxValue, 185)    
        
        def testFive(self):
            # Test Case 5
            knapsack = [{ "name":'waterproof trousers', "weight":42, "value":70 }, { "name":'waterproof overclothes', "weight":43, "value":75 }, { "name":'note-case', "weight":22, "value":80 }, { "name":'sunglasses', "weight":7, "value":20 }, { "name":'towel', "weight":18, "value":12 }, { "name":'socks', "weight":4, "value":50 }, { "name":'book', "weight":30, "value":10 }]
            maxWeight = 100

            maxValue = problemOne(knapsack, maxWeight)

            print(f"""
            Test Case 5: (Problem 1, 0/1 Knapsack)
            The Maximum Value of Knapsack is: {maxValue}
            """)
            self.assertEqual(maxValue, 237)   
        
        def testSix(self):
            # Test Case 6
            knapsack = [{ "name":'waterproof trousers', "weight":42, "value":70 }, { "name":'waterproof overclothes', "weight":43, "value":75 }, { "name":'note-case', "weight":22, "value":80 }, { "name":'sunglasses', "weight":7, "value":20 }, { "name":'towel', "weight":18, "value":12 }, { "name":'socks', "weight":4, "value":50 }, { "name":'book', "weight":30, "value":10 }]
            maxWeight = 200

            maxValue = problemOne(knapsack, maxWeight)

            print(f"""
            Test Case 6: (Problem 1, 0/1 Knapsack)
            The Maximum Value of Knapsack is: {maxValue}
            """)
            self.assertEqual(maxValue, 317)   
        
    class TestIsProblemTwo(unittest.TestCase):
        """
        This class contains unit tests for the `problemTwo` function, which checks whether a string of parentheses, brackets, and braces is valid.

        Each test case in this class calls the `problemTwo` function with a specific string of parentheses, brackets, and braces, and verifies that the function returns the expected result.

        Attributes:
            None

        Methods:
            testOne: Tests whether the string "()[]{}" is a valid string of parentheses, brackets, and braces.
            testTwo: Tests whether the string "([)]" is a valid string of parentheses, brackets, and braces.
            testThree: Tests whether the string "{{[](}})" is a valid string of parentheses, brackets, and braces.
            testFour: Tests whether the string "{[()]}" is a valid string of parentheses, brackets, and braces.
        """

        def testOne(self):
            # Test Case 1
            brackets = "()[]{}"
            isValid = problemTwo(brackets)
            print(f"""
            Test Case 1: (Problem 2, Valid Paranthesis)
            Is the paranthesis string valid: {isValid}
            """)
            self.assertEqual(isValid, True)   
        
        def testTwo(self):
            # Test Case 2
            brackets = "([)]"
            isValid = problemTwo(brackets)
            print(f"""
            Test Case 2: (Problem 2, Valid Paranthesis)
            Is the paranthesis string valid: {isValid}
            """)
            self.assertEqual(isValid, False)   
        
        def testThree(self):
            # Test Case 3
            brackets = "{{[](}})"
            isValid = problemTwo(brackets)
            print(f"""
            Test Case 3: (Problem 2, Valid Paranthesis)
            Is the paranthesis string valid: {isValid}
            """)
            self.assertEqual(isValid, False)   
        
        def testFour(self):
            # Test Case 4
            brackets = "{[()]}"
            isValid = problemTwo(brackets)
            print(f"""
            Test Case 4: (Problem 2, Valid Paranthesis)
            Is the paranthesis string valid: {isValid}
            """)
            self.assertEqual(isValid, True)   
        

    unittest.main()
