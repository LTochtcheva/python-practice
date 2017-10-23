# to run tests $pytest
#count = 0;
def palindrome_chain_length(num):
    print('num: ',num)
    count = 0
# check if num is already a palindrome
# if it is return 0
    if(is_palindrome(num) == True):
        print('count: ', count)
        return count;
# if not make a palindrome and count steps
    else:
        while (is_palindrome(num) == False):
            count += 1
            # num_list = [int(i) for i in str(num)]
            # reversed_list = list(reversed(num_list))
            # num = num + int(''.join(str(i) for i in reversed_list))

            num += int(str(num)[::-1])
            print('count in else: ', count)
        return count

def is_palindrome(num):
    # num_list = [int(i) for i in str(num)]
    # reversed_list = list(reversed(num_list))
    # if(reversed_list == num_list):
    #     return True
    # else:
    #     return False

# start at the end, count down to the beginning, stepping backwards
# one step at a time. [::-1]
    return str(num) == str(num)[::-1]

def test_answer():
    assert palindrome_chain_length(363) == 0
    assert palindrome_chain_length(36) == 1
    assert palindrome_chain_length(87) == 4
