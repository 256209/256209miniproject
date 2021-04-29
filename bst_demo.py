from datetime import datetime, timedelta

class JOB:
    def __init__(self, key):
        time_scheduled, job_duration, job_name = key.split(",")
        raw_time_scheduled = datetime.strptime(time_scheduled, '%H:%M')
        key = raw_time_scheduled.time()
        end_time = (raw_time_scheduled + timedelta(minutes=int(job_duration))).time()
        self.end = end_time
        self.job_duration = job_duration
        self.data = key
        self.job_name = job_name.rstrip()
        self.left_node = None
        self.right_node = None

    def __str__(self):
        return f"Time: {self.data}, job_duration: {self.job_duration}, End: {self.end}, Jobname: {self.job_name}"

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, JOB):
            key = JOB(key)
        if self.root == None:
            self.root = key
            self.print1(key, True)
        else:
            self._insert(self.root, key)

    def _insert(self, curr, key):
        if key.data > curr.data and key.data >= curr.end:
            if curr.right_node == None:
                curr.right_node = key
                self.print1(key, True)
            else:
                self._insert(curr.right_node, key)
        elif key.data < curr.data and key.end <= curr.data:
            if curr.left_node == None:
                curr.left_node = key
                self.print1(key, True)
            else:
                self._insert(curr.left_node, key)
        else:
            self.print1(key, False)

    def print1(self, key, succeeded):
        if succeeded:
            print(f"Added:\t\t {key.job_name}")
            print(f"Begin:\t\t {key.data}")
            print(f"End:\t\t {key.end}")
            print("-"*60)
        else:
            print(f"Rejected:\t {key.job_name}")
            print(f"Begin:\t\t {key.data}")
            print(f"End:\t\t {key.end}")
            print("Reason:\t Time slot overlap, please verify")
            print("-"*60)

    def in_order(self):
        print("Full job schedule for today")
        print("-"*60)
        self._in_order(self.root)
        print("-"*60)

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left_node)
            print(curr)
            self._in_order(curr.right_node)

    def length(self):
        return self._length(self.root)

    def _length(self, curr):
        if curr is None:
            return 0
        return 1 + self._length(curr.left_node) + self._length(curr.right_node)

    def find_val(self, key):
        return self._find_val(self.root, key)

    def _find_val(self, curr, key):
        if curr:
            if key == curr.data:
                return curr
            elif key < curr.data:
                return self._find_val(curr.left_node, key)
            else:
                return self._find_val(curr.right_node, key)
        return

    def minimum_subtree(self, curr):
        if curr.left_node == None:
            return curr
        else:
            return self.minimum_subtree(curr.left_node)

    def delete_val(self, key):
        self._delete_val(self.root, None, None, key)

    def _delete_val(self, curr, prev, is_left, key):
        if curr:
            if key == curr.data:
                if curr.left_node and curr.right_node:
                    min_child = self.minimum_subtree(curr.right_node)
                    curr.data = min_child.data
                    self._delete_val(curr.right_node, curr, False, min_child.data)
                elif curr.left_node == None and curr.right_node == None:
                    if prev:
                        if is_left:
                            prev.left_node = None
                        else:
                            prev.right_node = None
                    else:
                        self.root = None
                elif curr.left_node == None:
                    if prev:
                        if is_left:
                            prev.left_node = curr.right_node
                        else:
                            prev.right_node = curr.right_node
                    else:
                        self.root = curr.right_node
                else:
                    if prev:
                        if is_left:
                            prev.left_node = curr.left_node
                        else:
                            prev.right_node = curr.left_node
                    else:
                        self.root = curr.left_node
            elif key < curr.data:
                self._delete_val(curr.left_node, curr, True, key)
            elif key > curr.data:
                self._delete_val(curr.right_node, curr, False, key)
        else:
            print(f"{key} not found in Tree")