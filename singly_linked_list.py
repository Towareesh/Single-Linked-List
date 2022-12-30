class ListNode:
    def __init__(self, val=0, _next=None):
        self.val  = val
        self.next = _next

    def __repr__(self):
        node   = self
        result = ''
        while node:
            result += f'[{node.val}]'
            node    = node.next

        return f'[{None}]{result}[{None}]'

    def append(self, val):
        end_elem   = ListNode(val)
        first_elem = self
        while first_elem.next:
            first_elem = first_elem.next
        first_elem.next = end_elem

    def length(self):
        result = 0
        if self.val:
            result = 1
        while self.next:
            self = self.next
            result += 1

        return result



def sllist(data):
    node = ListNode()
    if data:
        node.val = data[0]
        for i in range(1, len(data)):
            node.append(data[i])
    return node

def mergeTwoLists(l1, l2):
    dum = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dum.next

def convert(sllist):
    result = [sllist.val]
    while sllist.next:
        sllist = sllist.next
        result.append(sllist.val)
    return result

def reverseList(sllist):
    tail = None
    while sllist:
        sllist.next, tail, sllist = tail, sllist, sllist.next
    return tail

def length(sllist):
    result = 0
    if sllist.val:
        result = 1
    while sllist.next:
        sllist = sllist.next
        result += 1
    return result

def middle_list(sllist):
    for i in range(length(sllist) // 2):
        sllist.next, sllist = sllist, sllist.next
    return sllist

def detectCycle(sllist):
    # я сам не до конца понимаю как работает это шайтан-алгоритм
    # fast идет вперед на две головы
    # slow в трае идет с начала, а вне трая идет вперед на одну голову
    # в итоге елси slow догонит fast то список цикличный
    # я хуй его знает че это значит
    try:
        fast = sllist.next
        slow = sllist
        while fast is not slow:
            fast = fast.next.next
            slow = slow.next
    except:
        return None

    slow = slow.next
    while sllist is not slow:
        sllist = sllist.next
        slow   = slow.next

    return sllist

x = [3,2,0,-4, 1]
l = sllist(x)
print(l.length())

