package jfngsea.test_driven_dev_by_example.money;

import java.util.Hashtable;

public class Bank {
    private final Hashtable<Pair, Integer> rates= new Hashtable<>();

    void addRate(String from, String to, int rate) {
        rates.put(new Pair(from, to), rate);
    }
    int rate(String from, String to) {
        if (from.equals(to)) return 1;
        Integer rate= rates.get(new Pair(from, to));
        return rate;
    }
    Money reduce(Expression source, String to){
        return source.reduce(this, to);
    }
}
