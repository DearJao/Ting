from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    pq = PriorityQueue()
#  99876636719 // https://app.sli.do/event/1E3nDTpqY51JrQeLW48XrW
    seventh_item_nopreferred = {'qtd_linhas': 7}
    sixth_item_nopreferred = {'qtd_linhas': 6}
    first_item_preferred = {'qtd_linhas': 1}
    second_item_preferred = {'qtd_linhas': 2}
    third_item_preferred = {'qtd_linhas': 3}

    pq.enqueue(sixth_item_nopreferred)
    pq.enqueue(first_item_preferred)
    pq.enqueue(second_item_preferred)
    pq.enqueue(third_item_preferred)
    pq.enqueue(seventh_item_nopreferred)
    assert len(pq) == 5

    assert pq.search(2) == third_item_preferred
    assert pq.search(3) == sixth_item_nopreferred
    with pytest.raises(IndexError):
        pq.search(10)

    assert pq.dequeue() == first_item_preferred
    assert pq.dequeue() == second_item_preferred
    assert pq.dequeue() == third_item_preferred
    assert pq.dequeue() == sixth_item_nopreferred
    assert pq.dequeue() == seventh_item_nopreferred

    assert len(pq) == 0

    pq.enqueue(seventh_item_nopreferred)
    pq.enqueue(sixth_item_nopreferred)

    assert len(pq) == 2
