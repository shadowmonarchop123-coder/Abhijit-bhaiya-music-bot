from collections import defaultdict, deque

queues = defaultdict(deque)

def add(chat_id, data):
    queues[chat_id].append(data)

def get(chat_id):
    if queues[chat_id]:
        return queues[chat_id][0]
    return None

def pop(chat_id):
    if queues[chat_id]:
        return queues[chat_id].popleft()
    return None

def clear(chat_id):
    queues[chat_id].clear()

def is_empty(chat_id):
    return len(queues[chat_id]) == 0
