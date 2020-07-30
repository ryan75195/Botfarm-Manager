package Farming;

import main.Node;
import main.main;
import org.osbot.rs07.api.Bank;
import org.osbot.rs07.api.map.Position;
import org.osbot.rs07.script.MethodProvider;

import java.util.ArrayList;
import java.util.HashMap;

public class buyRunSupplies extends Node {
    public buyRunSupplies(main m) {
        super(m);
    }

    Position grandExchange = new Position(3165, 3487, 0);

    ArrayList<String> Items = new ArrayList<>();
    HashMap<String, Integer> itemPrice = new HashMap<>();
    HashMap<String, Integer> itemID = new HashMap<>();
    HashMap<String, Integer> itemQuantity = new HashMap<>();


    @Override
    public boolean validate() {
        return m.isTimeToBuy();
    }

    @Override
    public int execute() throws InterruptedException {
        m.log("Buyrunsupplies ");

        Items.add("Fire rune");
        Items.add("Law rune");
        Items.add("Trout");
        Items.add("Energy potion(4)");

        itemPrice.put("Fire rune", 6);
        itemPrice.put("Law rune", 165);
        itemPrice.put("Trout", 150);
        itemPrice.put("Energy potion(4)", 600);

        itemID.put("Fire rune",554);
        itemID.put("Law rune",563);
        itemID.put("Trout",333);
        itemID.put("Energy potion(4)",3008);









        if(grandExchange.distance(m.myPosition()) > 20){
            m.setCurrentAction("Walking to ge");
            m.getWalking().webWalk(grandExchange);
        }else if(!m.getInventory().contains("Coins")){
            m.setCurrentAction("getting items");

            m.getBank().open();
            m.getBank().withdrawAll("Coins");
            m.getBank().enableMode(Bank.BankMode.WITHDRAW_NOTE);
            MethodProvider.sleep(500);
            m.getBank().withdrawAll("Fire rune");
            MethodProvider.sleep(500);
            m.getBank().withdrawAll("Law rune");
            MethodProvider.sleep(500);
            m.getBank().withdrawAll("Trout");
            MethodProvider.sleep(500);
            m.getBank().withdrawAll("Energy potion(4)");
            MethodProvider.sleep(500);
            m.getBank().close();
        }else if(!m.getGrandExchange().isOpen()){
            m.getNpcs().closest("Grand Exchange Clerk").interact("Exchange");
            MethodProvider.sleep(5000);
        }else if(m.getGrandExchange().isOpen()){


                for(String item : Items){

                    m.setCurrentAction("buying " + item);

                    if(m.getInventory().getAmount("Coins") < 10000){
                        itemQuantity.put("Fire rune", 2);
                        itemQuantity.put("Law rune", 2);
                        itemQuantity.put("Trout", 8);
                        itemQuantity.put("Energy potion(4)", 6);
                    }else if(m.getInventory().getAmount("Coins") < 50000){
                        itemQuantity.put("Fire rune", 30);
                        itemQuantity.put("Law rune", 30);
                        itemQuantity.put("Trout", 200);
                        itemQuantity.put("Energy potion(4)", 150);
                    }else{
                        itemQuantity.put("Fire rune", 100);
                        itemQuantity.put("Law rune", 100);
                        itemQuantity.put("Trout", 400);
                        itemQuantity.put("Energy potion(4)", 300);
                    }

                    if (m.getInventory().getAmount(item) < itemQuantity.get(item)) {
                        m.getGrandExchange().buyItem(itemID.get(item), item, itemPrice.get(item), itemQuantity.get(item) - (int) m.getInventory().getAmount(item));
                        MethodProvider.sleep(3000);
                        m.getGrandExchange().collect();
                    }


                }


            m.getGrandExchange().collect();

                if(m.getGrandExchange().isOpen()){
                    m.getGrandExchange().close();
                }

        }

        if(m.getInventory().contains("Fire rune") && m.getInventory().contains("Law rune") && m.getInventory().getAmount("Trout") > 1 && m.getInventory().contains("Energy potion(4)")){
            m.setTimeToBuy(false);
        }




        return 0;
    }
}

