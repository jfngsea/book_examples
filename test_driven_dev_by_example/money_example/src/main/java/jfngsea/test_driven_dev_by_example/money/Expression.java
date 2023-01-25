package jfngsea.test_driven_dev_by_example.money;

public interface Expression {
    Money reduce(Bank bank, String to);
    Expression plus(Expression addend);

    Expression times(int multiplier);
}
