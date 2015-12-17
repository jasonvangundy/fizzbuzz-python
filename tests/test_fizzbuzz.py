from robber import expect

from src import fizzbuzz


def test_returns_fizz_when_divisible_by_3():
    expect(fizzbuzz.get(3)).to.eq("fizz")


def test_returns_buzz_when_divisable_by_5():
    expect(fizzbuzz.get(5)).to.eq("buzz")


def test_returns_fizzbuzz_when_divisable_by_15():
    expect(fizzbuzz.get(15)).to.eq("fizzbuzz")


def test_returns_the_number_when_not_otherwise_divisable():
    expect(fizzbuzz.get(1)).to.eq(1)
    expect(fizzbuzz.get(7)).to.eq(7)
