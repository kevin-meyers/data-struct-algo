from dataclasses import dataclass

from linked_lists.singly_linked_list import SinglyLinkedList

@dataclass
class KV_pair:
    key: object
    value: object

    def __eq__(self, other):
        return self.key == other.key


class HashTable(object):

    def __init__(self, init_size=8):
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [SinglyLinkedList() for _ in range(init_size)]
        # For faster length times
        self.length = 0

    def __iter__(self):
        return self.items()

    def _bucket_index(self, key):
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def _find_by_key(self, key):
        bucket = self.buckets[self._bucket_index(key)]
        return bucket, bucket.find(lambda x: x.key == key)

    def keys(self):
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for pair in bucket.items():
                all_keys.append(pair.key)

        return all_keys

    def values(self):
        all_values = []
        for bucket in self.buckets:
            for pair in bucket.items():
                all_values.append(pair.value)

        return all_values

    def items(self):
        all_items = []
        for bucket in self.buckets:
            all_items.extend([(pair.key, pair.value) for pair in bucket.items()])
        return all_items

    def __len__(self):
        return self.length

    def __contains__(self, key):
        if self._find_by_key(key)[1]:
           return True

        return False

    def get(self, key):
        _, pair = self._find_by_key(key)
        if pair:
            return pair.value

        raise KeyError('Key not found: {}'.format(key))

    def __getitem__(self, key):
        return self.get(key)

    def set(self, key, value):
        bucket, pair = self._find_by_key(key)
        if pair:
            pair.value = value

        else:
            bucket.append(KV_pair(key=key, value=value))
            self.length += 1

    def __setitem__(self, key, value):
        self.set(key, value)

    def delete(self, key):
        bucket, pair_to_delete = self._find_by_key(key)
        if pair_to_delete:
            bucket.delete(pair_to_delete)
            self.length -= 1

        else:
            raise KeyError('Key not found: {}'.format(key))
