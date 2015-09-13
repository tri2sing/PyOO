'''
Created on Sep 4, 2015

@author: Sameer Adhikari
'''

# First set of classes to highlight the diamond problem.
# The method in the top class gets called twice.

print(32*'=')
print('Naive handling of the diamond problem')
 
class TopClassNaive:
    num_base_calls = 0
    def common_method(self):
        print("Calling method on TopClassNaive")
        self.num_base_calls += 1

class LeftClassNaive(TopClassNaive):
    num_left_calls = 0
    def common_method(self):
        TopClassNaive.common_method(self)
        print("Calling method on LeftClassNaive")
        self.num_left_calls += 1

class RightClassNaive(TopClassNaive):
    num_right_calls = 0
    def common_method(self):
        TopClassNaive.common_method(self)
        print("Calling method on RightClassNaive")
        self.num_right_calls += 1

class BottomClassNaive(LeftClassNaive, RightClassNaive):
    num_sub_calls = 0
    def common_method(self):
        LeftClassNaive.common_method(self)
        RightClassNaive.common_method(self)
        print("Calling method on BottomClassNaive")
        self.num_sub_calls += 1
        
bnaive = BottomClassNaive()
bnaive.common_method()
print(bnaive.num_sub_calls, bnaive.num_left_calls, bnaive.num_right_calls, bnaive.num_base_calls)

# Second set of classes that handle the diamond problem.
# The use of super() handles ordering of the common_method.
# This solution works only when the arguments passed to the  
# two superclass (Left and Right) from subclass (Bottom) are 
# the same.  This solution breaks down in case if Bottom has  
# to pass different arguments to Left and Right superclass.

print(32*'=')
print('Aware handling of the diamond problem')

class TopClassAware:
    num_base_calls = 0
    def common_method(self):
        print("Calling method on TopClassAware")
        self.num_base_calls += 1

class LeftClassAware(TopClassAware):
    num_left_calls = 0
    def common_method(self):
        super().common_method()
        print("Calling method on LeftClassAware")
        self.num_left_calls += 1

class RightClassAware(TopClassAware):
    num_right_calls = 0
    def common_method(self):
        super().common_method()
        print("Calling method on RightClassAware")
        self.num_right_calls += 1

class BottomClassAware(LeftClassAware, RightClassAware):
    num_sub_calls = 0
    def common_method(self):
        super().common_method()
        print("Calling method on BottomClassAware")
        self.num_sub_calls += 1
        
baware = BottomClassAware()
baware.common_method()
print(baware.num_sub_calls, baware.num_left_calls, baware.num_right_calls, baware.num_base_calls)

print(32*'=')
