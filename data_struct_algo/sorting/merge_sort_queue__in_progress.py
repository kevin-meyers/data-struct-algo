from queues.node_queue import NodeQueue


def merge(q1, q2):
    merged = NodeQueue()
    while len(q1) and len(q2):
        if q1.peek() < q2.peek():
            merged.enqueue(q1.dequeue())

        else:
            merged.enqueue(q2.dequeue())

    if len(q1) == 0:
        for item in q2:
            merged.enqueue(item)

    else:
        for item in q1:
            merged.enqueue(item)

    return merged


def merge_sort()
