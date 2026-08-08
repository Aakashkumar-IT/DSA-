# Node of Linked List
class Node:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.next = None


# Function to find Two Sum
def twoSum(nums, target):

    # -------------------------------
    # Step 1: Convert Array to Linked List
    # -------------------------------
    head = None
    tail = None

    for i in range(len(nums)):
        new_node = Node(nums[i], i)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    # -------------------------------
    # Step 2: Traverse the Linked List
    # -------------------------------
    first = head

    while first is not None:

        second = first.next

        while second is not None:

            if first.value + second.value == target:
                return [first.index, second.index]

            second = second.next

        first = first.next

    return []


# -------------------------------
# User Input
# -------------------------------

nums = list(map(int, input("Enter the numbers: ").split()))

target = int(input("Enter the target: "))

# Call the function
result = twoSum(nums, target)

# Display result
if result:
    print("Indices:", result)
    print("Values:", nums[result[0]], "and", nums[result[1]])
else:
    print(f"No two numbers found whose sum equals the target {target}.")