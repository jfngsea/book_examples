package jfngsea.test_driven_dev_by_example;

public class Sum implements Expression{
    Money augend;
    Money addend;

    public Sum(Money augend, Money addend) {
        this.augend = augend;
        this.addend = addend;
    }

    public Money reduce(Bank bank, String to) {
        int amount= augend.amount + addend.amount;
        return new Money(amount, to);
    }
}
