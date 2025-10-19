class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency  # 1 = most urgent, 10 = least

    def __repr__(self):
        return f"{self.name} ({self.urgency})"


class MinHeap:
    def __init__(self):
        self.data = []

    def insert(self, patient):
        self.data.append(patient)
        self._heapify_up(len(self.data) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        size = len(self.data)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right

            if smallest == index:
                break
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest

    def remove_min(self):
        if not self.data:
            print("Error: No patients in queue.")
            return None
        if len(self.data) == 1:
            return self.data.pop()
        root = self.data[0]
        self.data[0] = self.data.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        return self.data[0] if self.data else None

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")


# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.insert(Patient("Casey", 2))

    heap.print_heap()
    print("\nNext up:", heap.peek())

    served = heap.remove_min()
    print(f"\nServed patient: {served.name}")
    heap.print_heap()

while heap.data:
    heap.remove_min()
heap.remove_min()  # Removing from empty queue


"""
DESIGN MEMO

This project models two hospital systems using trees and heaps. A tree is appropriate for the doctor reporting
structure because it naturally represents hierarchical relationships — one doctor can oversee multiple others, 
forming branches that reflect lines of supervision. Each node connects directly to its reports, which makes it 
easy to visualize management and perform recursive traversals.

Different traversal methods serve different purposes. Preorder can show top-down decision flow, where supervisors
appear before their teams. Inorder is often used for balanced or sorted relationships, which could represent
workflow or scheduling order. Postorder works best for summarizing performance or processing data from the bottom
up, since it visits subordinates before their manager.

The emergency priority queue uses a min-heap because it efficiently retrieves the most urgent patient. Each insert
or removal keeps the smallest urgency value at the top (representing the most critical patient). This mirrors how
real emergency rooms triage care — the most severe cases must always be handled first, even when new patients
arrive. Using heaps ensures fast, reliable updates and helps simulate the real-time decision-making process needed 
in hospitals.
"""
