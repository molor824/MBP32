from typing import TypeVar, Iterator
from peekable import Peekable

T = TypeVar('T')

def try_next(iterator: Iterator[T]) -> T | None:
    try:
        return next(iterator)
    except StopIteration:
        return None
def try_peek(peekable: Peekable[T]) -> T | None:
    try:
        return peekable.peek()
    except StopIteration:
        return None