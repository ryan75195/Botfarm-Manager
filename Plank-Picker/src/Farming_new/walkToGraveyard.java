package Farming_new;

import main.Node;
import main.main;
import org.osbot.rs07.api.map.Area;
import org.osbot.rs07.api.map.Position;
import org.osbot.rs07.event.WebWalkEvent;
import org.osbot.rs07.script.MethodProvider;
import org.osbot.rs07.utility.Condition;

public class walkToGraveyard extends Node {
    public walkToGraveyard(main m) {
        super(m);
    }
    Area town = new Area(3123, 3639, 3154, 3617);

    @Override
    public boolean validate() {
        return !m.inGraveyard() && !m.getInventory().isFull() && m.myPlayer().getHealthPercent() > 40 && !m.isTimeToBuy() && (m.getStarterCash() || m.getInventory().getAmount("Trout") > 1) && !town.contains(m.myPosition());

    }

    @Override
    public int execute() throws InterruptedException {
        m.log("walkingtoGraveyard Node");

        m.setCurrentAction("Walking to the graveyard.");


        WebWalkEvent w = new WebWalkEvent(new Position(3148, 3671, 0));
        w.setBreakCondition(new Condition() {
            @Override
            public boolean evaluate() {
                return m.getObjects().get(3134,3639) != null && new Position(3134,3639,0).distance(m.myPosition()) < 5 && m.myPosition().getY() < 3639;
            }
        });
        m.execute(w);
        if (m.getObjects().closest("Barrier") != null && m.getObjects().get(3134,3639).get(0).getPosition().distance(m.myPosition()) < 5 && m.myPosition().getY() < m.getObjects().get(3134,3639).get(0).getY()) {
            m.getObjects().closest("Barrier").interact("Pass-Through");
            MethodProvider.sleep(1500);
        }


        return 0;
    }
}
